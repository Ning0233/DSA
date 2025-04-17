def find_best_fabric_pair(fabrics, budget):
    fabrics.sort(key=lambda x:x[1])

    left, right = 0, len(fabrics) - 1
    best_pair = None
    max_cost = 0 

    while left < right:
        cost = fabrics[left][1] + fabrics[right][1]
        if cost <= budget:
            if cost > max_cost:
                max_cost = cost
                best_pair = (fabrics[left][0], fabrics[right][0])
            left += 1
        else:
            right -= 1
    return best_pair
    #Time Complexity: O(nlogn)
    #Space Complexity: o(1)

fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))