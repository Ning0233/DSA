def dfs(airline, is_connected,  visited):
    visited.add(airline)
    for neighor in range(len(is_connected)):
        if is_connected[airline][neighor] == 1 and neighor not in visited:
            dfs(neighor, is_connected, visited)



def num_airline_regions(is_connected):
    visited = set()
    regions = 0

    for airline in range(len(is_connected)):
        if airline not in visited:
            dfs(airline, is_connected, visited)
            regions += 1
    
    return regions

            



is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2)) 