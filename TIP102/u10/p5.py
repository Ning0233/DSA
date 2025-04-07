from collections import deque
def find_itinerary(boarding_passes):
    itinerary = deque(list(boarding_passes.pop()))
    while boarding_passes:
        for trip in boarding_passes[::-1]:
            departure = trip[0]
            destination = trip[-1]
            if departure in itinerary:
                boarding_passes.remove(trip)
                itinerary.extend([destination])
                continue
            if destination in itinerary:
                boarding_passes.remove(trip)
                itinerary.extendleft([departure])
                continue
    return list(itinerary)
                





boarding_passes_1 = [
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
['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
['LHR', 'DFW', 'JFK', 'LAX', 'DXB']