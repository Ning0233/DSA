class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def insert_into_sorted_circular_list(head, insert_val):
    # Case 1: Empty list
    if not head:
        new_node = ListNode(insert_val)
        new_node.next = new_node  # Point to itself to form a circular list
        return new_node

    # Case 2: Traverse the list to find the correct position
    prev, current = head, head.next
    while True:
        # Case 2a: Insert between two nodes
        if prev.val <= insert_val <= current.val:
            break

        # Case 2b: Insert at the boundary (largest or smallest value)
        if prev.val > current.val:  # We're at the boundary between max and min
            if insert_val >= prev.val or insert_val <= current.val:
                break

        prev, current = current, current.next

        # Case 2c: Full traversal without finding a position
        if prev == head:
            break

    # Insert the new node
    new_node = ListNode(insert_val, current)
    prev.next = new_node

    return head

# For testing
def print_circular_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while True:
        print(current.val, end=" -> ")
        current = current.next
        if current == head:
            break
    print("(back to head)")

# Example 1
head = ListNode(3, ListNode(4, ListNode(1)))
head.next.next.next = head  # Make it circular
print_circular_list(insert_into_sorted_circular_list(head, 2))  # Output: 3 -> 4 -> 1 -> 2 -> (back to head)

# Example 2
head = None
print_circular_list(insert_into_sorted_circular_list(head, 1))  # Output: 1 -> (back to head)