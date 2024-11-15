import pandas as pd
from ast_generated import evaluate_code_ast  # Replace 'ast_function' with the correct module name
from Upload_rubrics import new_rubrics, output_rubrics  # Replace 'rubric_file' with the correct module name
import subprocess  # for running solutions

# Run the model solution to see if it matches
model_solution_path = "C:/Users/Andrew/OneDrive - Singapore Management University/SMU stuff/4.1/FYP/35_Equinox_Python_Autograder/Template files for AST generation/Upload_model_solution.py"

# Run the file in the terminal in real-time (prompt will appear in order)
print("This is the expected result: ")
expected_result = subprocess.run(["python", model_solution_path], capture_output=False, text=True)


# Path to the Python file you want to run
submitted_code_path = "C:/Users/Andrew/OneDrive - Singapore Management University/SMU stuff/4.1/FYP/35_Equinox_Python_Autograder/Template files for AST generation/submitted_solution.py"  # Replace with your actual path

# Run the file in the terminal in real-time (prompt will appear in order)
print("This is the submitted result: ")

try:
    result = subprocess.run(["python", submitted_code_path], capture_output=False, text=True, timeout=20)
except subprocess.TimeoutExpired:
    print("Error: The program took too long to execute (possible infinite loop).")
except Exception as e:
    print(f"An error occurred: {e}")

# Open the solution file and read its contents
with open(submitted_code_path, "r") as file:
    function_text = file.read()

# Evaluate the submission (no print statements for the raw result dictionary)
evaluation_result = evaluate_code_ast(function_text, new_rubrics)

# Convert the result to a DataFrame for better readability
criteria_df = pd.DataFrame({
    "Criteria": evaluation_result["Criteria"],
    "Description": evaluation_result["Description"],
    "Marks": evaluation_result["Marks"]
})

# Add the "Total" as a separate row
total_df = pd.DataFrame({"Criteria": ["Total"], "Description": [""], "Marks": [evaluation_result["Total"]]})

# Combine the criteria DataFrame and the total row
final_df = pd.concat([criteria_df, total_df], ignore_index=True)

# Output only the DataFrame (this will avoid printing the rubrics)
print(final_df)

