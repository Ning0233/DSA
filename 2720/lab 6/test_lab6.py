from lab6 import getUnbalancedPositions
# Test case 1
s1 = "()"
expected1 = []
result1 = getUnbalancedPositions(s1)
assert result1 == expected1, f"Expected {expected1}, but got {result1}"

# Test case 2
s2 = "(]"
expected2 = [0, 1]
result2 = getUnbalancedPositions(s2)
assert result2 == expected2, f"Expected {expected2}, but got {result2}"

# Test case 3
s3 = "(a+b"
expected3 = [0]
result3 = getUnbalancedPositions(s3)
assert result3 == expected3, f"Expected {expected3}, but got {result3}"

# Test case 4
s4 = "a + (b * c] - {d / e)"
expected4 = [4, 10, 14, 20]
result4 = getUnbalancedPositions(s4)
assert result4 == expected4, f"Expected {expected4}, but got {result4}"