def middle_node(head):
    def get_middle(head, end):
        if head == end or head.next == end:
            return head
        slow = head
        fast = head
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        return slow

    return get_middle(head, None)


def middle_node(head):
    slow = fast = head
    current = head
    while fast and fast.next:
        fast = current.next.next
        slow = current.next
    return slow