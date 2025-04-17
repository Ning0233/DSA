# Parameters for the binomial distribution
n <- 8       # Number of trials (offspring)
p <- 0.25    # Probability of success (trait appearing)
x <- 3       # Number of successes (trait appearing in exactly 3 offspring)

# Calculate the probability
probability <- dbinom(x, size = n, prob = p)

# Print the result
print(paste("Probability of the trait appearing in exactly 3 offspring:", round(probability, 4)))