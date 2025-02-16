def minStep(n, slipperySteps, current = 0):
    
    #base case
    if current >= n:
        return 0
    
    # check slipperysteps
    if current in slipperySteps:
        return -1
    
    step1 = minStep(n, slipperySteps, current + 1)    
    step2 = minStep(n, slipperySteps, current + 2)

    if step1 == -1 and step2 == -1: return -1

    if step1 == -1: return step2 + 1
    if step2 == -1: return step1 + 1

    return min(step1, step2) + 1

print(minStep(6,[2,4]))