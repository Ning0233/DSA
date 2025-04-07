def find_itinerary(boarding_passes):

    def dfs(city, itinerary):
        if city not in root: return itinerary
        next_city = root[city]
        itinerary.append(next_city)
        dfs(next_city, itinerary)

    root = {}
    itineraries = {}
    for departture, arrival in boarding_passes:
        root[departture] = arrival
        itineraries[departture] = []
    for city in itineraries:
        itinerary = []
        dfs(city, itinerary)
        itineraries[city] = itinerary
        if len(itinerary) == len(boarding_passes):
            return [city] + itinerary

                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))