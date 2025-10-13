def are_parentheses_balanced(expression: str) -> bool:
    """
    Checks if an expression has balanced parentheses using a stack.
    Supports (), [], and {}.
    """
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False  # Closing bracket with no opening one
            if stack.pop() != bracket_map[char]:
                return False  # Mismatched brackets

    return not stack  # True if stack is empty, False otherwise

if __name__ == '__main__':
    expr1 = "{[()()]}"
    expr2 = "{[(])}"
    expr3 = "(()"
    
    print(f"'{expr1}' is balanced: {are_parentheses_balanced(expr1)}")
    print(f"'{expr2}' is balanced: {are_parentheses_balanced(expr2)}")
    print(f"'{expr3}' is balanced: {are_parentheses_balanced(expr3)}")
