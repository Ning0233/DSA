# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2: # constrain for None lists
            if list1.val > list2.val:
                curr.nest = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            
            curr = curr.next
        
        if list1: # for only list1 exist
            curr.next = list1
        else: curr.next = list2 # for only list2 exist

        return dummy.next

