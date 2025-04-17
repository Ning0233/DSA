def prime_frequency_map(matrix):
    # Initialize a list to store the frequency of primes for each row
    prime_frequencies = {}

    # Iterate through each row in the matrix
    for row in range(len(matrix)):
        # Count the number of prime numbers in the current row
        for column in range(len(matrix)):
            prime_frequencies[matrix[row][column]] = prime_frequencies.get([matrix[row][column]], 0) + 1 if is_prime(matrix[row][column]) else continue 
        
        # Append the count to the result list

    return prime_frequencies