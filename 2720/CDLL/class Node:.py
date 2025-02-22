class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CDLL:
    def __init__(self):
        self.head = None

    def prepend(self, x):
        p = Node(x)
        if self.head is None:
            self.head = p
            p.prev = p  # Changed from p.prev = self.head to p.prev = p
            p.next = p  # Changed from p.next = p to p.next = p
        else:
            p.next = self.head
            p.prev = self.head.prev
            self.head.prev.next = p
            self.head.prev = p
            self.head = p
            # Removed redundant line: self.head.prev.next = p