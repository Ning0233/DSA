from collections import deque
def validate_shelter_sequence(admitted, adopted):
    adopted_d = deque(adopted)
    admitted_d = deque()
    for i in admitted:
        admitted_d.append(i)
        if admitted_d and admitted_d[-1] == adopted_d[0]:
            admitted_d.pop()
            adopted_d.popleft()
    while admitted_d:
        if admitted_d[-1] == adopted_d[0]:
            admitted_d.pop() 
            adopted_d.popleft()
        else:
            break
    return not admitted_d

    

    
print(validate_shelter_sequence([1,2,3,4,5], [4,5,3,2,1]))
print(validate_shelter_sequence([1,2,3,4,5], [4,3,5,1,2])) 