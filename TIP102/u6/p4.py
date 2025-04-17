class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Function to reverse a linked list
def reverse_linked_list(head):
    """
    Time Complexity
    Find the Length:

    Traversing the linked list takes O(n) time.
    Reverse the Second Half:

    Reversing the second half takes O(n/2) time.
    Calculate Twin Sums:

    Traversing the first half and the reversed second half takes O(n/2) time.
    Total Time Complexity:

    O(n).
    Space Complexity
    The algorithm uses a constant amount of extra space for pointers (current, prev, next_node, etc.).
    Total Space Complexity: O(1).
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Function to find the maximum twin stability sum
def max_protein_pair_stability(head):
    # Step 1: Find the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Step 2: Find the middle of the linked list
    mid = length // 2
    current = head
    for _ in range(mid - 1):
        current = current.next

    # Step 3: Reverse the second half of the linked list
    second_half = reverse_linked_list(current.next)
    current.next = None  # Split the list into two halves

    # Step 4: Calculate the maximum twin sum
    max_twin_sum = 0
    first_half = head
    while second_half:
        twin_sum = first_half.value + second_half.value
        max_twin_sum = max(max_twin_sum, twin_sum)
        first_half = first_half.next
        second_half = second_half.next

    # Step 5: Return the maximum twin sum
    return max_twin_sum

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Example protein chains
head1 = Node(5, Node(4, Node(2, Node(1))))
head2 = Node(4, Node(2, Node(2, Node(3))))

print(max_protein_pair_stability(head1))  # Output: 6 (5 + 1 or 4 + 2)
print(max_protein_pair_stability(head2))  # Output: 6 (4 + 2 or 3 + 3)
