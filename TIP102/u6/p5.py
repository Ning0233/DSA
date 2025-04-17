class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Function to reorganize the linked list into odd and even groups
def odd_even_experiments(exp_results):
    """
    Time Complexity
    Traversal:

    Each node is visited exactly once, so the time complexity is O(n), where n is the number of nodes in the linked list.
    Pointer Updates:

    Updating pointers is a constant-time operation, so it does not affect the overall complexity.
    Total Time Complexity: O(n).

    Space Complexity
    The algorithm uses a constant amount of extra space for pointers (odd, even, even_head).
    No additional data structures are used.
    Total Space Complexity: O(1).
    """
    if not exp_results or not exp_results.next:
        return exp_results  # If the list is empty or has only one node, return it as is

    # Initialize pointers
    odd = exp_results
    even = exp_results.next
    even_head = even  # Keep track of the head of the even group

    # Traverse the list
    while even and even.next:
        odd.next = even.next  # Connect the next odd node
        odd = odd.next        # Move the odd pointer forward
        even.next = odd.next  # Connect the next even node
        even = even.next      # Move the even pointer forward

    # Connect the odd group to the even group
    odd.next = even_head

    return exp_results

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Example experiment results
experiment_results1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
experiment_results2 = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))

# Test the function
print_linked_list(odd_even_experiments(experiment_results1))  # Output: 1 -> 3 -> 5 -> 2 -> 4
print_linked_list(odd_even_experiments(experiment_results2))  # Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
