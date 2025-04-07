from collections import Counter


def find_center(terminals):
    root = [-1] * (len(terminals)+1)
    for edge in terminals:
        edge = sorted(edge)
        root[edge[-1]-1] = edge[0]
    count = Counter(root)
    most_common = count.most_common(1)
    print(root)
    return most_common[0][0] if most_common != -1 else None
terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))