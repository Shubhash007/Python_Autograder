import ast

def evaluate_code_ast(code, rubric):
    tree = ast.parse(code)
    results = {
        "Criteria": rubric["Criteria"],
        "Marks": [0] * len(rubric["Marks"]),
        "Description": rubric["Description"],
        "Total": 0
    }

    def check_input_handling(node):
        return isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'input'

    def check_strip_function(node):
        return isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'strip'

    def check_upper_function(node):
        return isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'upper'

    def check_for_loop_int_conversion(node):
        if isinstance(node, ast.For):
            for inner_node in ast.walk(node):
                if isinstance(inner_node, ast.Call) and isinstance(inner_node.func, ast.Name) and inner_node.func.id == 'int':
                    return True
        return False

    def check_list_comprehension_int_conversion(node):
        return isinstance(node, ast.ListComp) and any(isinstance(inner_node, ast.Call) and isinstance(inner_node.func, ast.Name) and inner_node.func.id == 'int' for inner_node in ast.walk(node))

    def check_weights_list(node):
        return isinstance(node, ast.List) and all(isinstance(elt, ast.Constant) and elt.value in [2, 7, 6, 5, 4, 3, 2] for elt in node.elts)

    def check_for_loop_weighted_sum(node):
        if isinstance(node, ast.For):
            for inner_node in ast.walk(node):
                if isinstance(inner_node, ast.BinOp) and isinstance(inner_node.op, ast.Mult):
                    return True
        return False

    def check_list_comprehension_weighted_sum(node):
        return isinstance(node, ast.ListComp) and any(isinstance(inner_node, ast.BinOp) and isinstance(inner_node.op, ast.Mult) for inner_node in ast.walk(node))

    def check_modulo_11(node):
        return isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod) and isinstance(node.right, ast.Constant) and node.right.value == 11

    def check_if_else(node):
        return isinstance(node, ast.If)

    def check_checksum_list_s_f(node):
        return isinstance(node, ast.List) and all(isinstance(elt, ast.Constant) and elt.value in ['J','Z','I','H','G','F','E','D','C','B','A'] for elt in node.elts)

    def check_checksum_list_t_g(node):
        return isinstance(node, ast.List) and all(isinstance(elt, ast.Constant) and elt.value in ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'J', 'Z', 'I', 'H'] for elt in node.elts)

    for node in ast.walk(tree):
        if check_input_handling(node):
            results["Marks"][0] = rubric["Marks"][0]
        if check_strip_function(node):
            results["Marks"][1] = rubric["Marks"][1]
        if check_upper_function(node):
            results["Marks"][2] = rubric["Marks"][2]
        if check_for_loop_int_conversion(node):
            results["Marks"][3] = rubric["Marks"][3]
        if check_list_comprehension_int_conversion(node):
            results["Marks"][4] = rubric["Marks"][4]
        if check_weights_list(node):
            results["Marks"][5] = rubric["Marks"][5]
        if check_for_loop_weighted_sum(node):
            results["Marks"][6] = rubric["Marks"][6]
        if check_list_comprehension_weighted_sum(node):
            results["Marks"][7] = rubric["Marks"][7]
        if check_modulo_11(node):
            results["Marks"][8] = rubric["Marks"][8]
        if check_if_else(node):
            results["Marks"][9] = rubric["Marks"][9]
        if check_checksum_list_s_f(node):
            results["Marks"][10] = rubric["Marks"][10]
        if check_checksum_list_t_g(node):
            results["Marks"][11] = rubric["Marks"][11]

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