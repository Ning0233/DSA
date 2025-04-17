# Sample size and number of people who responded "Make some major changes"
n <- 1026  # Total sample size
p_major_changes <- 0.39  # Proportion selecting "Make some major changes"
x <- n * p_major_changes  # Number of people selecting "Make some major changes"

# Perform the proportion test
result <- prop.test(x = x, n = n, conf.level = 0.95, correct = FALSE)

# Print the confidence interval
print(result$conf.int)

# Print the interpretation
print(paste("The 95% confidence interval for the proportion of adults who would respond 'Make some major changes' is:",
            round(result$conf.int[1], 4), "to", round(result$conf.int[2], 4)))