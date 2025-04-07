from collections import deque
def get_all_destinations(flights, city):
    destinations = []
    queue = deque(flights[city])
    while queue:
        current = queue.popleft()
        destinations.append(current)
        if current in flights:
            for destination in flights[current]:
                if destination in destinations:
                    continue
                queue.append(destination)
    return destinations
            
            


flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))