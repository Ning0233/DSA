# Parameters of the normal distribution
mean_diameter <- 3      # Mean diameter in cm
sd_diameter <- 0.1      # Standard deviation in cm

# Specifications for acceptable corks
lower_limit <- 2.9      # Lower bound of acceptable diameter
upper_limit <- 3.1      # Upper bound of acceptable diameter

# Calculate the proportion of corks within the acceptable range
within_spec <- pnorm(upper_limit, mean = mean_diameter, sd = sd_diameter) - 
               pnorm(lower_limit, mean = mean_diameter, sd = sd_diameter)

# Proportion of defective corks
proportion_defective <- 1 - within_spec

# Print the result
print(paste("Proportion of defective corks:", round(proportion_defective, 4)))