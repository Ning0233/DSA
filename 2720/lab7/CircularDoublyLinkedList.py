class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            n.next = n
            n.prev = n
            return
        n.next = self.head
        p = self.head
        while p.next != self.head:
            p = p.next
        n.prev = p
        p.next = n
        self.head.prev = n
        self.head = n
    
    def insert_last(self, data):
        n = Node(data)
        if not self.head:
            n.next = n
            n.prev = n
            self.head = n
            return
        last = self.head.prev
        last.next = n
        n.prev = last
        n.next = self.head
        self.head.prev = n
    
    def delete_first(self):
        if not self.head: 
            print("Empty")
            return
        if self.head == self.head.next:
            self.head = None
            return
        p = self.head
        while p.next != self.head:
            p = p.next
        p.next = p.next.next
        self.head.next.prev = p
        self.head = self.head.next
    
    def delete_last(self):
        if not self.head: 
            return
        if self.head == self.head.next:
            self.head = None
            return
        last = self.head.prev
        last.prev.next = self.head
        self.head.prev = last.prev
        
        
        
