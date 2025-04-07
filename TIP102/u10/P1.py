def bidirectional_flights(flights):
    for i in range(len(flights)):
        for neighbor in flights[i]:
            if i not in flights[neighbor]:
                return False
    return True
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))