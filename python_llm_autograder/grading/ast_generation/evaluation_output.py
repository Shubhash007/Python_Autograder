import pandas as pd
from ast_generated import evaluate_code_ast, evaluate_output  # Import the updated functions
from Upload_rubrics import new_rubrics, output_rubrics  # Import both rubrics
import subprocess  # For running solutions

# Paths to the model solution and submitted code
model_solution_path = "C:/Users/Andrew/OneDrive - Singapore Management University/SMU stuff/4.1/FYP/35_Equinox_Python_Autograder/Template files for AST generation/Upload_model_solution.py"
submitted_code_path = "C:/Users/Andrew/OneDrive - Singapore Management University/SMU stuff/4.1/FYP/35_Equinox_Python_Autograder/Template files for AST generation/submitted_solution.py"  # Replace with your actual path



# Function to run code and capture output
def run_code(file_path, input_value):
    try:
        result = subprocess.run(
            ["python", file_path],
            input=input_value,
            capture_output=True,
            text=True,
            timeout=5  # Prevent infinite loops
        )
        if result.returncode != 0:
            print(f"Error running {file_path}:\n{result.stderr}")
            return None
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print(f"Execution of {file_path} timed out.")
        return None
    except Exception as e:
        print(f"An error occurred while running {file_path}: {e}")
        return None

# Input value for testing
test_input = input("Enter test number: ")

# Run the model solution
print("This is the expected result:")
expected_output = run_code(model_solution_path, test_input)
if expected_output is not None:
    print(expected_output)
else:
    print("Failed to run the model solution.")

# Run the submitted code
print("\nThis is the submitted result:")
submitted_output = run_code(submitted_code_path, test_input)
if submitted_output is not None:
    print(submitted_output)
else:
    print("Failed to run the submitted code.")

# Evaluate the outputs using the output rubrics
if expected_output is not None and submitted_output is not None:
    output_evaluation_result = evaluate_output(submitted_output, expected_output, output_rubrics)
else:
    # If either output is None, we cannot evaluate the output criteria
    output_evaluation_result = {
        "Criteria": output_rubrics["Criteria"],
        "Marks": [0] * len(output_rubrics["Marks"]),
        "Description": output_rubrics["Description"],
        "Total": 0
    }

# Create DataFrame for output evaluation
output_criteria_df = pd.DataFrame({
    "Criteria": output_evaluation_result["Criteria"],
    "Description": output_evaluation_result["Description"],
    "Marks": output_evaluation_result["Marks"]
})

# Add the "Total" as a separate row
output_total_df = pd.DataFrame({
    "Criteria": ["Total"],
    "Description": [""],
    "Marks": [output_evaluation_result["Total"]]
})

# Combine the criteria DataFrame and the total row
output_final_df = pd.concat([output_criteria_df, output_total_df], ignore_index=True)

# Output only the DataFrame for output evaluation
print("\nOutput Evaluation Results:")
print(output_final_df)





# Read the submitted code
with open(submitted_code_path, "r") as file:
    submitted_code = file.read()

# Evaluate the submission using the AST
ast_evaluation_result = evaluate_code_ast(submitted_code, new_rubrics)

# Create DataFrames for both evaluations
ast_criteria_df = pd.DataFrame({
    "Criteria": ast_evaluation_result["Criteria"],
    "Description": ast_evaluation_result["Description"],
    "Marks": ast_evaluation_result["Marks"]
})

# Add the "Total" as a separate row
ast_total_df = pd.DataFrame({
    "Criteria": ["Total"],
    "Description": [""],
    "Marks": [ast_evaluation_result["Total"]]
})

# Combine the criteria DataFrame and the total row
ast_final_df = pd.concat([ast_criteria_df, ast_total_df], ignore_index=True)

# Output only the DataFrame for AST evaluation if error does not appear
if submitted_output is not None:
    print("\nAST Evaluation Results:")
    print(ast_final_df)
else:
    print("")
    print("Manual checking and grading is required")
    print("")

