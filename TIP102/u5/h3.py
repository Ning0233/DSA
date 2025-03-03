
def is_palindrome(head): 

    # if length 0:
    if not head: return False
    if not head.next: return True
    
    while head.head and head.tail:
        if head.data == head.tail.data:
            head = head.next
            p = head
            while p.next:
                p.next = p.next.next
            
            tail = p.next
    return True + is_palindrome(head)