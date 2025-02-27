from collections import deque
p_dict = {")":"(", "]":"[", "}":"{"}

def checkBalancedParenthesis(s):
    d = deque()
    if not s: raise TypeError

    for char in s:
        if char in p_dict.values():
            d.append(char)
        elif char in p_dict and (not d or d[-1] != p_dict[char]):
            return "Unbalanced"
        elif char in p_dict and d[-1] == p_dict[char]:
            d.pop()
    return "Balanced" if not d else "Unbalanced"


def getUnbalancedPositions(s):
    d = deque()
    if not s: raise TypeError
    r = []

    for index, char in enumerate(s):
        if char in p_dict.values():
            d.append(char)
            r.append(index)
        elif char in p_dict and (not d or d[-1] != p_dict[char]):
            r.append(index)
        elif char in p_dict and d[-1] == p_dict[char]:
            d.pop()
            r.pop()
    return r
