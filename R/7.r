# Distribution for number of visits to dentists in one year
X <- c(0, 1, 2, 3, 4)          # Number of visits
P <- c(0.1, 0.3, 0.4, 0.15, 0.05)  # Corresponding probabilities

# Calculate the expected value (mean)
expected_value <- sum(X * P)

# Calculate the variance
variance <- sum((X - expected_value)^2 * P)

# Calculate the standard deviation
std_deviation <- sqrt(variance)

# Print the results
print(paste("Expected Value:", round(expected_value, 4)))
print(paste("Variance:", round(variance, 4)))
print(paste("Standard Deviation:", round(std_deviation, 4)))