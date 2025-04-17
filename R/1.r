# Dataset: Hours of sleep for 15 college students
sleep_hours <- c(5, 6, 6, 8, 7, 7, 9, 5, 4, 8, 11, 6, 7, 8, 7)

# Create a boxplot
boxplot(sleep_hours,
        main = "Boxplot of Hours of Sleep",
        ylab = "Hours",
        col = "lightblue",
        border = "darkblue")