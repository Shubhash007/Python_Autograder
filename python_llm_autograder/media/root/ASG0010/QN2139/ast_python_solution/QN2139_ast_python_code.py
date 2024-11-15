import ast

def evaluate_code_ast(code, rubric):
    tree = ast.parse(code)
    results = {
        "Criteria": rubric["Criteria"],
        "Marks": [0] * len(rubric["Marks"]),
        "Description": rubric["Description"],
        "Total": 0
    }

    def contains_input(node):
        return any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'input' for n in ast.walk(node))

    def contains_loops(node):
        return any(isinstance(n, (ast.For, ast.While)) for n in ast.walk(node))

    def contains_hardcoding(node):
        for n in ast.walk(node):
            if isinstance(n, ast.List) and len(n.elts) > 5:
                return True
        return False

    if contains_input(tree):
        results["Marks"][0] = rubric["Marks"][0]

    if contains_loops(tree):
        results["Marks"][1] = rubric["Marks"][1]

    if not contains_hardcoding(tree):
        results["Marks"][2] = rubric["Marks"][2]

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

    correct_elements_per_row = all(s_line.strip() == e_line.strip() for s_line, e_line in zip(submitted_lines, expected_lines))
    if correct_elements_per_row:
        results["Marks"][1] = output_rubric["Marks"][1]

    results["Total"] = sum(results["Marks"])
    return results