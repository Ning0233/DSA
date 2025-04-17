# Temperature changes before the generator was added
before <- c(6, 8, 4, 5, 10, 3, 9, 11, 7, 9)

# Temperature changes after the generator was added
after <- c(9, 11, 15, 12, 7, 12, 10, 13, 8, 11, 14, 8)

# (a) Perform a two-sample t-test (two-sided) at the 2% significance level
test_result <- t.test(before, after, alternative = "two.sided", conf.level = 0.98, var.equal = FALSE)

# Print the test results
print(test_result)

# (b) Extract and print the 98% confidence interval
conf_interval <- test_result$conf.int
print(paste("98% Confidence Interval for the difference in means:", 
            round(conf_interval[1], 4), "to", round(conf_interval[2], 4)))