# Parameters of the normal distribution
mean_diameter <- 3      # Mean diameter in cm
sd_diameter <- 0.1      # Standard deviation in cm

# Find the 75th percentile
diameter_75th <- qnorm(0.75, mean = mean_diameter, sd = sd_diameter)

# Print the result
print(paste("Diameter below which 75% of corks fall:", round(diameter_75th, 4)))