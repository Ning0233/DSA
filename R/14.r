# Data: Measurements of crankshaft dimensions (mm)
measurements <- c(224.120, 224.001, 224.017, 223.982, 223.960, 224.089, 
                  223.987, 223.976, 224.098, 224.057, 223.913, 223.999, 
                  223.989, 223.902, 223.961, 223.980)

# Perform a one-sided t-test
result <- t.test(measurements, mu = 224, alternative = "greater", conf.level = 0.90)

# Print the results
print(result)