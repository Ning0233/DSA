#

def get_sum_of_odds(matrix):
    counter = 0
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] % 2 == 0: continue
            current = matrix[i][j]
            counter += 0
            total += 0
    return [counter, total]
            