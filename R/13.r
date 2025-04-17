# Sample data
x <- 11       # Number of boxes with vouchers
n <- 65       # Total number of boxes
p_null <- 0.2 # Null hypothesis proportion

# Perform the one-sided proportion test
result <- prop.test(x = x, n = n, p = p_null, alternative = "less", correct = FALSE)

# Print the results
print(result)