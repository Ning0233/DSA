def merge_two_lists(l1, l2):
    # Write your code here
    
    dummy = SinglyLinkedList()
    if not l1 and not l2: return None
    #pointers
    cl1 = l1
    cl2 = l2
    lm_head = dummy.next
    clm = lm_head

    while cl1 and cl2:
        if cl1.data <= cl2.data:
            # non list
            if not lm_head:
                lm_head = cl1
            # if lm
            if lm_head:
                clm.next = cl1
                clm = clm.next
            cl1 = cl1.next
        else:
            if not lm_head:
                lm_head = cl2
            # if lm
            if lm_head:
                clm.next = cl2
                clm = clm.next
            cl2 = cl2.next
    
    while cl1:
        clm.next = cl1
        clm = clm.next
        cl1 = cl1.next
      
    
    clm.next = cl2
    clm = clm.next
    cl2 = cl2.next
    
    
    return dummy.next
    