#

def two_sum(numbers, target):
    print(numbers, target)
    h = {numbers[i]: i for i in range(len(numbers))}
    
    for i in range(len(numbers)):
        c = target - numbers[i]
        if c in numbers:
            return sorted([i+1, h[c]+1])
        else: continue
    
    return None     