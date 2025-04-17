class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Function to split the protein chain
def split_protein_chain(protein, k):
    """
    Time Complexity
    Calculate Length:

    Traversing the linked list takes O(n) time, where n is the number of nodes in the list.
    Split the List:

    Traversing the list again to split it into segments also takes O(n) time.
    Total Time Complexity:

    O(n).
    Space Complexity
    The algorithm uses a constant amount of extra space for pointers (current, next_segment).
    Total Space Complexity: O(1).
    """
    # Step 1: Calculate the total length of the protein chain
    length = 0
    current = protein
    while current:
        length += 1
        current = current.next

    # Step 2: Determine the size of each segment
    base_size = length // k
    extra_nodes = length % k

    # Step 3: Split the linked list into k segments
    segments = []
    current = protein
    for i in range(k):
        segment_head = current
        segment_size = base_size + (1 if i < extra_nodes else 0)
        for _ in range(segment_size - 1):
            if current:
                current = current.next
        if current:
            next_segment = current.next
            current.next = None  # Break the chain
            current = next_segment
        segments.append(segment_head)

    # Step 4: Return the segments
    return segments

# For testing
def print_linked_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Example protein chains
protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

# Test the function
parts = split_protein_chain(protein1, 3)
for part in parts:
    print_linked_list(part)

parts = split_protein_chain(protein2, 5)
for part in parts:
    print_linked_list(part)