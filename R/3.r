# Dataset: Ground temperatures in Death Valley (°F)
temperatures <- c(146, 152, 168, 174, 180, 178, 179, 180, 178, 178, 168, 165, 152, 144)

# Calculate the mean
mean_temp <- mean(temperatures)
print(paste("Mean:", mean_temp))

# Calculate the median
median_temp <- median(temperatures)
print(paste("Median:", median_temp))

# Calculate the variance
variance_temp <- var(temperatures)
print(paste("Variance:", variance_temp))

# Calculate the standard deviation
sd_temp <- sd(temperatures)
print(paste("Standard Deviation:", sd_temp))