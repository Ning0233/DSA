class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            n.next = n
            return
        n.next = self.head
        p = self.head
        while p.next != self.head:
            p = p.next
        p.next = n
        self.head = n
    
    def insert_last(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            n.next = self.head
            return
        p = self.head
        while p.next != self.head:
            p = p.next
        p.next = n
        n.next = self.head
    
    def delete_first(self):
        if not self.head: 
            return
        if self.head.next ==  self.head:
            self.head = None
            return
        p = self.head
        while p.next != self.head:
            p = p.next
        p.next = self.head.next
        self.head = self.head.next
    
    def delete_last(self):
        if not self.head: 
            return
        if self.head.next ==  self.head:
            self.head = None
            return
        p = self.head
        while p.next.next != self.head:
            p = p.next
        p.next = self.head
        
        
        


        
    
       