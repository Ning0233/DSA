# Dataset: Given numbers
data <- c(275, 296, 299, 316, 322, 323, 332, 333, 337, 347, 350, 357, 358, 264, 393)

# Calculate the 5-number summary
summary_stats <- summary(data)
print(summary_stats)

# Create a histogram
hist(data,
     main = "Histogram of Given Data",
     xlab = "Values",
     col = "lightgreen",
     border = "darkgreen",
     breaks = 10)  # Adjust the number of bins as needed