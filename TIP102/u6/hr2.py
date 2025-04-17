class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse_between(head, left, right):
    if not head or left == right:
        return head

    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move `prev` to the node before the `left` position
    for _ in range(left - 1):
        prev = prev.next

    # Start reversing the sublist
    current = prev.next
    next_node = None
    for _ in range(right - left + 1):
        temp = current.next
        current.next = next_node
        next_node = current
        current = temp

    # Connect the reversed sublist back to the list
    prev.next.next = current
    prev.next = next_node

    return dummy.next