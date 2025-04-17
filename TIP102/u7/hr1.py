def is_nested_parens(paren_s, memo=[], index=0, balance=0):
    # Write your code here
    if index == len(paren_s):
        return balance == 0
    
    if balance < 0: 
        return False
    
    if paren_s[index] == '(': 
        memo.append('(')
        return is_nested_parens(paren_s, memo, index + 1, balance + 1)
    elif paren_s[index] == ')' and '(' in memo: 
        memo.pop('(')
        return is_nested_parens(paren_s, memo,  index + 1, balance - 1)
    else:
        return is_nested_parens(paren_s, memo, index + 1, balance)
    