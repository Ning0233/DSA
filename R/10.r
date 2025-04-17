# Probability of passing the bar exam
p <- 0.57

# (a) Probability that Bob passes on his second try
prob_second_try <- (1 - p)^(2 - 1) * p

# (b) Probability that Bob needs 3 attempts to pass
prob_third_try <- (1 - p)^(3 - 1) * p

# (c) Probability that Bob needs more than 3 attempts to pass
prob_more_than_three <- 1 - ( (1 - p)^(1 - 1) * p + (1 - p)^(2 - 1) * p + (1 - p)^(3 - 1) * p )

# Print the results
print(paste("Probability that Bob passes on his second try:", round(prob_second_try, 4)))
print(paste("Probability that Bob needs 3 attempts to pass:", round(prob_third_try, 4)))
print(paste("Probability that Bob needs more than 3 attempts to pass:", round(prob_more_than_three, 4)))