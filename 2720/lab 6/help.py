    p_dict = {")": "(", "]": "[", "}": "{"}
    if not s:
        raise TypeError("Empty string")

    for char in s:
        if char in p_dict.values():
            d.append(char)
        elif char in p_dict and (not d or d[-1] != p_dict[char]):
            return "Unbalanced"
        elif char in p_dict and d[-1] == p_dict[char]:
            d.pop()

    return "Balanced" if not d else "Unbalanced"