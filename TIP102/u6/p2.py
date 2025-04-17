class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_values(protein):
    """
    Time Complexity
    Cycle Detection: The slow and fast pointers traverse the list at most twice. This takes O(n) time, where n is the number of nodes in the list.
    Finding the Start of the Cycle: This takes O(n) time in the worst case.
    Collecting Cycle Values: Traversing the cycle takes O(k) time, where k is the number of nodes in the cycle.
    Total Time Complexity: O(n), where n is the number of nodes in the list.
    Space Complexity
    The algorithm uses a constant amount of extra space for the pointers (slow, fast, current).
    Total Space Complexity: O(1).
    """
    # Step 1: Detect the cycle using Floyd's Cycle Detection Algorithm
    slow, fast = protein, protein
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Cycle detected
            break
    else:
        # No cycle found
        return []

    # Step 2: Find the start of the cycle
    slow = protein
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Step 3: Collect the values in the cycle
    cycle_start = slow
    cycle_values = []
    current = cycle_start
    while True:
        cycle_values.append(current.value)
        current = current.next
        if current == cycle_start:
            break

    return cycle_values


# Example usage
protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next  # Create a cycle: Val -> Gly

print(cycle_values(protein_head))  # Output: ['Gly', 'Leu', 'Val'] (order may vary)