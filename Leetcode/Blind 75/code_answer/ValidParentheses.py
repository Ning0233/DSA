class Solution:
    def isValid(self, s: str) -> bool:
        # initialize stack and hash
        stack = []
        hash = {')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char in hash:
                if stack and stack[-1] == hash[char]: # matching parentheses
                    stack.pop()
                else: return False 
            else: stack.append(char)
        
        return not stack
        