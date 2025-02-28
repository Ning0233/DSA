class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def fish_chances(head, fish_name):
    current = head
    length = 0
    #this is flag True: if fish is in list; False: if fish is not in list
    flag = None
    while current:
        length += 1
        if current.fish_name == fish_name: flag = True
        current = current.next
    return f"{1/length:.2f}" if flag else f"{0:.2f}"

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print(fish_chances(fish_list, "Dace"))
print(fish_chances(fish_list, "Rainbow Trout"))