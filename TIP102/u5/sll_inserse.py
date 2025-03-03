# Function to reverse the linked list
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next # save the next node
        current.next = prev #reverse the pointer of the current node to the point to the previous node
        prev = current #move prev to the current node
        current = next_node #move current to the next node
    return prev