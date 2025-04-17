# Sample statistics
n <- 30                # Sample size
mean_incubation <- 17.83  # Sample mean
sd_incubation <- 2.20     # Sample standard deviation
confidence_level <- 0.99  # Confidence level

# Calculate the critical t-value
t_critical <- qt((1 + confidence_level) / 2, df = n - 1)

# Calculate the margin of error
margin_of_error <- t_critical * (sd_incubation / sqrt(n))

# Calculate the confidence interval
lower_bound <- mean_incubation - margin_of_error
upper_bound <- mean_incubation + margin_of_error

# Print the results
print(paste("The 99% confidence interval for the mean incubation time is:",
            round(lower_bound, 4), "to", round(upper_bound, 4)))