class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

#this is queue class using single linked list
class Queue:
    def __init__(self, head = None) -> None:
        self.head = head
        self.tail = None
    
    # isEmpty check is the queue is empty: returns true if empty, false if not empty
    def isEmpty(self):
        return not self.head 
    
    #enqueue is to add a node at end of linked list
    def enqueue(self, x):
        node = Node(x)
        if self.isEmpty(): 
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node
    
    #dequeue is to delete the first node of a linked list
    def dequeue(self):
        if self.isEmpty():
            return "queue underflow"
        q = self.head
        self.head = self.head.next
        
        if not self.head:
            self.tail = None
        return q.data
    
    #this is a visualization function
    def printQueue(self)->bool:
        if self.isEmpty():
            print("Queue is Empty")
            return
        q = self.head
        while q:
            print(q.data, end=" -> ")
            q = q.next
        print(None)
        # if self.head.next: # checking if linked list is properlly linked
            # print(self.head.next.data)

if __name__ == "__main__":
    #main script for frist class
    queue1 = Queue()
    queue1.enqueue(1)
    queue1.printQueue()
    queue1.enqueue(2)
    queue1.printQueue()
    queue1.enqueue(3)
    queue1.printQueue()
    queue1.enqueue(4)
    queue1.printQueue()
    queue1.dequeue()
    queue1.printQueue()
    queue1.dequeue()
    queue1.printQueue()
    queue1.dequeue()
    queue1.printQueue()
    queue1.dequeue()
    queue1.printQueue()

        