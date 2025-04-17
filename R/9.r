# Parameters for the binomial distribution
n <- 4       # Number of trials (gauges)
p <- 0.1     # Probability of defect
x <- 1       # Number of defective gauges

# Probability that only 1 is defective
probability_one_defective <- dbinom(x, size = n, prob = p)

# Probability that more than 1 is defective
probability_more_than_one <- 1 - (dbinom(0, size = n, prob = p) + dbinom(1, size = n, prob = p))

# Print the results
print(paste("Probability that only 1 is defective:", round(probability_one_defective, 4)))
print(paste("Probability that more than 1 is defective:", round(probability_more_than_one, 4)))