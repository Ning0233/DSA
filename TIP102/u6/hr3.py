def odd_even_list(head):
    if not head or not head.next:
        return head

    # Initialize pointers for odd and even lists
    odd = head
    even = head.next
    even_head = even  # Keep track of the start of the even list

    # Rearrange nodes into odd and even lists
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    # Connect the odd list to the even list
    odd.next = even_head

    return head