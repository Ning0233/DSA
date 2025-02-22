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
            p.prev = p
            p.next = p
        else:
            p.next = self.head
            p.prev = self.head.prev
            self.head.prev.next = p
            self.head.prev = p
            self.head = p
    
    def append(self, x):
        p = Node(x)
        if self.head is None:
            self.head = p
            p.prev = p
            p.next = p
        else:
            p.next = self.head
            p.prev = self.head.prev
            self.head.prev.next = p
            self.head.prev = p
    
    def deletef(self):
        if self.head is None:
            print("List is empty")
        if self.head.next is self.head:
            self.head = None
            return
        else:
            p = self.head
            self.head = p.next
            self.head.prev = p.prev
            p.prev.next = self.head.next
            p.next = None
            p.prev = None
