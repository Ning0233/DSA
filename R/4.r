# Dataset: Heights of plants (in cm)
plant_heights <- c(32, 36, 38, 41, 43, 44, 48, 48, 49, 52, 53, 54, 55, 56, 59, 60, 62, 67, 75)

# Create a QQ plot
qqnorm(plant_heights, 
       main = "QQ Plot of Plant Heights",
       xlab = "Theoretical Quantiles",
       ylab = "Sample Quantiles",
       col = "blue",
       pch = 19)

# Add a reference line
qqline(plant_heights, col = "red", lwd = 2)