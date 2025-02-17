from collections import deque
def append_animals(available, preferred):
    d = deque()
    j = deque(preferred)
    for i in available:
        if j and i == j[0]:
            d.append(i)
            j.popleft()
    return len(j)
print(append_animals("catsdogs", "cows")) 
print(append_animals("rabbit", "r")) 
print(append_animals("fish", "bird"))