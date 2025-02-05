# this is a python list queue class
class QueueList:
    def __init__(self) -> None:
        self.queue = []
    
    def append(self,x):
        self.queue.append(x)    
    
    def dequeue(self):
        if self.is_Empty(): return "queue underflow"
        q = self.queue.pop(0)
        return q
    
    def is_Empty(self):
        return not self.queue

    def printQueue(self):
        if self.is_Empty(): 
            print("Empty queue")
            return
        for _ in self.queue:
            print(_, end=" -> ")
        print("None")


if __name__ == "__main__":
    #main script for second class
    queue2 = QueueList()
    queue2.append(5)
    queue2.append(6)
    queue2.append(7)
    queue2.append(8)
    queue2.printQueue()
    queue2.dequeue()
    queue2.printQueue()
    queue2.dequeue()
    queue2.printQueue()
    queue2.dequeue()
    queue2.printQueue()
    queue2.dequeue()
    queue2.printQueue()
        
    
    

    

