from collections import deque
def counting_flights(flights, i, j):
    if flights[i][j] == 1: return 1
    visited = set()
    queue = deque([[i,0]])
    while queue:
        airport,flight_count = queue.popleft()
        if airport in visited: continue
        visited.add(airport)
        airport_connectivity = flights[airport]
        for next_airport in range(len(airport_connectivity)):
            if airport_connectivity[next_airport] == 1:
                if next_airport == j:
                    return flight_count + 1
                queue.append([next_airport,flight_count+1])
    return -1




# Example usage
flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))