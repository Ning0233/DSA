def decode_string(s):
    # Stack to store characters and numbers
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            # Build the current number (handles multi-digit numbers)
            current_number = current_number * 10 + int(char)
        elif char == '[':
            # Push the current string and number onto the stack
            stack.append((current_string, current_number))
            # Reset current string and number
            current_string = ""
            current_number = 0
        elif char == ']':
            # Pop from the stack and decode the string
            last_string, repeat_count = stack.pop()
            current_string = last_string + current_string * repeat_count
        else:
            # Append the character to the current string
            current_string += char

    return current_string

# Example usage
print(decode_string("3[a]2[bc]"))  # Expected: "aaabcbc"
print(decode_string("3[a2[c]]"))   # Expected: "accaccacc"
print(decode_string("2[abc]3[cd]ef"))  # Expected: "abcabccdcdcdef"