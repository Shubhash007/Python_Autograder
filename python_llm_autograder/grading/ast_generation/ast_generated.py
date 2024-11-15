import ast

def evaluate_code_ast(code, rubric):
    tree = ast.parse(code)
    results = {
        "Criteria": rubric["Criteria"],
        "Marks": [0] * len(rubric["Marks"]),
        "Description": rubric["Description"],
        "Total": 0
    }

    uses_input = False
    uses_int = False
    uses_for_loop = False

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == 'input':
                uses_input = True
            elif node.func.id == 'int':
                uses_int = True
        elif isinstance(node, ast.For):
            uses_for_loop = True

    if uses_input:
        results["Marks"][0] = rubric["Marks"][0]  # Input Handling

    if uses_int:
        results["Marks"][1] = rubric["Marks"][1]  # Integer

    if uses_for_loop:
        results["Marks"][2] = rubric["Marks"][2]  # No loops

    results["Total"] = sum(results["Marks"])
    return results

def evaluate_output(submitted_output, expected_output, output_rubric):
    results = {
        "Criteria": output_rubric["Criteria"],
        "Marks": [0] * len(output_rubric["Marks"]),
        "Description": output_rubric["Description"],
        "Total": 0
    }

    submitted_lines = submitted_output.strip().split('\n')
    expected_lines = expected_output.strip().split('\n')

    correct_number_of_rows = len(submitted_lines) == len(expected_lines)
    if correct_number_of_rows:
        results["Marks"][0] = output_rubric["Marks"][0]

    correct_elements_per_row = True
    for s_line, e_line in zip(submitted_lines, expected_lines):
        s_line_stripped = s_line.strip()
        e_line_stripped = e_line.strip()
        if len(s_line_stripped) != len(e_line_stripped):
            correct_elements_per_row = False
            break
    if correct_elements_per_row:
        results["Marks"][1] = output_rubric["Marks"][1]

    results["Total"] = sum(results["Marks"])
    return results