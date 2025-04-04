# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(0, head)
        dummy = result

        for _ in range(n): head = head.next

        while head: 
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return result.next
