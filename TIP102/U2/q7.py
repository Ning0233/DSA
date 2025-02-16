def min_steps_to_match_maps(map1, map2):
    lmap1 = list(map1)
    print(lmap1)
    for l in map2:
        if l in lmap1:
            lmap1.remove(l)
        
    return len(lmap1)

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))