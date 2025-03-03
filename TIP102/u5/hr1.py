class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_list(head):
    current = head
    while current:
        print(current.data, end="->")
        current = current.next
    print("None")


def remove_elements(head, val):
    # Write your code here
    #if not list:
    if not head: 
        return None
    #if head:
    while head and head.data == val: 
        head = head.next
    current = head
    while current and current.next:
        if current.next.data == val: 
            current.next = current.next.next
            current = current.next
        else: 
            current = current.next

    return head
# Create the linked list 1->2->6->3->4->5->6
values = [1, 2, 6, 3, 4, 5, 6]
ll1 = create_linked_list(values)

# Print the linked list
print_list(ll1)

remove_elements(ll1, 6)
print_list(ll1)
