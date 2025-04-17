class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def edit_dna_sequence(dna_strand, m, n):
    """

    Time Complexity
    Traversal: Each node is visited once, either to retain or skip it.
    Total Time Complexity: O(n), where n is the number of nodes in the linked list.
    Space Complexity
    The algorithm uses a constant amount of extra space (pointers current and temp).
    Total Space Complexity: O(1).
    """
    current = dna_strand
    while current:
        # Retain the first m nodes
        for _ in range(m - 1):
            if current is None:
                return dna_strand
            current = current.next

        # Skip the next n nodes
        temp = current.next if current else None
        for _ in range(n):
            if temp is None:
                break
            temp = temp.next

        # Connect the retained part to the remaining part
        if current:
            current.next = temp
            current = temp

    return dna_strand
dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))