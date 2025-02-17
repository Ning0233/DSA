def group_animals_by_habitat(habitats):
    last_occurrence = {habitat: idx for idx, habitat in enumerate(habitats)}
    r = []
    start = end = 0
    for idx, habitat in enumerate(habitats):
        end = max(end, last_occurrence[habitat])
        if idx == end:
            r.append(end - start + 1)
            start = end + 1
    return r
        

print(group_animals_by_habitat("ababcbacadefegdehijhklij")) 
print(group_animals_by_habitat("eccbbbbdec"))