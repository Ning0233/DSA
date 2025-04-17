def organize_fabric_rolls(fabric_rolls):
    fabric_rolls.sort()

    pairs = []
    leftover = None
    for i in range(0, len(fabric_rolls)-1, 2):
        pairs.append((fabric_rolls[i], fabric_rolls[i+1]))

    if len(fabric_rolls) % 2 != 0:
        leftover = fabric_rolls[-1]
    
    return pairs + [leftover] if leftover else pairs
    #time: n
    #space: n

fabric_rolls = [15, 10, 25, 30, 22]
fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
fabric_rolls_3 = [40, 10, 25, 15, 30]

print(organize_fabric_rolls(fabric_rolls))
print(organize_fabric_rolls(fabric_rolls_2))
print(organize_fabric_rolls(fabric_rolls_3))