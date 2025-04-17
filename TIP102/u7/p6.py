def evaluate_ternary_expression_iterative(expression):
    stack = []
    
    # Traverse the expression from right to left
    for i in range(len(expression) - 1, -1, -1):
        char = expression[i]
        
        if stack and stack[-1] == '?':
            stack.pop()  # Remove the '?'
            true_expr = stack.pop()  # True expression
            stack.pop()  # Remove the ':'
            false_expr = stack.pop()  # False expression
            
            if char == 'T':
                stack.append(true_expr)
            else:
                stack.append(false_expr)
        else:
            stack.append(char)
    
    return stack[0]

def evaluate_ternary_expression_recursive(expression):
    # Base case: if the expression is a single character, return it
    if len(expression) == 1:
        return expression

    # Find the rightmost '?'
    question_mark_index = expression.rfind('?')

    # Extract the condition, true_choice, and false_choice
    condition = expression[question_mark_index - 1]
    true_choice = expression[question_mark_index + 1]
    false_choice = expression[question_mark_index + 3]

    # Evaluate the condition and recursively evaluate the chosen branch
    if condition == 'T':
        return evaluate_ternary_expression_recursive(expression[:question_mark_index - 1] + true_choice + expression[question_mark_index + 4:])
    else:
        return evaluate_ternary_expression_recursive(expression[:question_mark_index - 1] + false_choice + expression[question_mark_index + 4:])

# Example usage
print(evaluate_ternary_expression_recursive("T?2:3"))  # Output: "2"
print(evaluate_ternary_expression_recursive("F?1:T?4:5"))  # Output: "4"
print(evaluate_ternary_expression_recursive("T?T?F:5:3"))  # Output: "F"