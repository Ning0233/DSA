from typing import Optional

def divide(numerator: int, denominator: int) -> Optional[float]:
  """Divides two numbers.

  Args:
    numerator: The dividend.
    denominator: The divisor.

  Returns:
    The quotient if the denominator is not zero, otherwise None.
  """

  if denominator == 0:
    return None
  else:
    return numerator / denominator

result = divide(10, 2)  # Output: 5.0
result = divide(5, 0)  # Output: None
