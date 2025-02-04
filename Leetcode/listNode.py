class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def add_to_beginning(head: Optional[ListNode], val: int) -> Optional[ListNode]:
  """
  This function adds a new node with the given value to the beginning of the linked list.

  Args:
      head: The head node of the existing linked list (or None if empty).
      val: The value to be added in the new node.

  Returns:
      The head node of the modified linked list.
  """
  # Create a new node with the given value
  new_node = ListNode(val)

  # If the list is empty (head is None), set the dummy node as the new node
  if head is None:
    return new_node

  # Create a dummy node (not storing data)
  dummy = ListNode()

  # Set the dummy node's next to point to the current head
  dummy.next = head

  # Now, the new node can be inserted at the beginning by pointing the dummy's next to the new node
  dummy.next = new_node

  # Return the dummy node (which points to the actual head of the modified list)
  return dummy.next

# Example usage
head = None  # Initially, the list is empty

# Add elements to the beginning
head = add_to_beginning(head, 3)
head = add_to_beginning(head, 2)
head = add_to_beginning(head, 1)

# Now the linked list is: 1 -> 2 -> 3
