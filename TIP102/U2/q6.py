def organize_pirate_crew(group_sizes):
    hash = {}
    for idx in range(len(group_sizes)):
        hash[group_sizes[idx]] = hash.get(group_sizes[idx], []) + [idx]
    #print(hash)
    groups = []
    sorted_hash = dict(sorted(hash.items()))
    print(sorted_hash)
    for key, items in sorted_hash.items():
        groups += [items[i:i + key] for i in range(0, len(items), key)]
    
    return groups
group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 