def is_nested_parens(paren_s, index=0, balance=0, has_parens=False):
    print(paren_s)
    # Write your code here
    if index == len(paren_s) and has_parens:
        return balance == 0
    
    if balance < 0: return False
    
    if paren_s[index] == '(': 
        return is_nested_parens(paren_s, index + 1, balance + 1, has_parens=True)
    elif paren_s[index] == ')': 
        return is_nested_parens(paren_s, index + 1, balance - 1, has_parens=True)
    else:
        return is_nested_parens(paren_s, index + 1, balance, has_parens)

# Example usage
print(is_nested_parens("abc"))  # Output: True
# print(is_nested_parens("(()"))   # Output: False
# print(is_nested_parens(")("))    # Output: False
# print(is_nested_parens("()()"))  # Output: True