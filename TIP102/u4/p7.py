def calculate_fabric_waste(items, fabric_rolls):
    waste = 0
    for i in range(len(items)):
        waste += (fabric_rolls[i] - items[i][1])
    return waste
    #time: n
    #space: 1
items_1 = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
fabric_rolls_1 = [5, 5, 5]

items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
fabric_rolls_2 = [4, 4, 4]

items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
fabric_rolls_3 = [7, 5, 5]

print(calculate_fabric_waste(items_1, fabric_rolls_1))
print(calculate_fabric_waste(items_2, fabric_rolls_2))
print(calculate_fabric_waste(items_3, fabric_rolls_3))