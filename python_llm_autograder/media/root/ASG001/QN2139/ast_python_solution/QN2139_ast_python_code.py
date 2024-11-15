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
        return isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'input'

    def contains_fibonacci_approach(node):
        if isinstance(node, ast.For) or isinstance(node, ast.While):
            return True
        if isinstance(node, ast.FunctionDef):
            for n in ast.walk(node):
                if isinstance(n, ast.Yield):
                    return True
        return False

    def contains_hardcoded_fibonacci(node):
        if isinstance(node, ast.List):
            elements = [e for e in node.elts if isinstance(e, ast.Constant) and isinstance(e.value, int)]
            return len(elements) > 5
        return False

    uses_input = any(contains_input(node) for node in ast.walk(tree))
    uses_fibonacci_approach = any(contains_fibonacci_approach(node) for node in ast.walk(tree))
    uses_hardcoded_fibonacci = any(contains_hardcoded_fibonacci(node) for node in ast.walk(tree))

    if uses_input:
        results["Marks"][0] = rubric["Marks"][0]

    if uses_fibonacci_approach:
        results["Marks"][1] = rubric["Marks"][1]

    if not uses_hardcoded_fibonacci:
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