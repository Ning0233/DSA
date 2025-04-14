from collections import deque
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    queue = deque(design)
    result = []
    level = 0
    while queue:
        level = []
        current = queue.popleft()



croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(listify_design(croquembouche))