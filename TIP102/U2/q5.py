def find_treasure_indices(gold_amounts, target):
    hash = {}
    for _ in range(len(gold_amounts)):
        hash[gold_amounts[_]] = _
    
    for _ in range(len(gold_amounts)):
        complement = target - gold_amounts[_]
        if complement in hash and hash[complement] != _:
            return [_, hash[complement]]
    return None
    
gold_amounts1 = [2, 7, 11, 15]

target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))
print(find_treasure_indices(gold_amounts2, target2))
print(find_treasure_indices(gold_amounts3, target3))