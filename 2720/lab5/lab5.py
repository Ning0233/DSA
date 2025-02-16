class ListNode:
    def __init__(self, data: any) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def printdll(self):
        if not self.head: print("Empty")
        p = self.head
        while p.next:
            print(p.data, sep="->")
            p = p.next
        print(None)
    def insert_first(self, value: int) -> None:
        p = ListNode(value)
        if not self.head:
            self.head = self.tail = p
            return
        p.next = self.head
        self.head.prev = p
        self.head = p



#main script
ddl = DoublyLinkedList()
ddl.insert_first(1)
ddl.printdll()
ddl.insert_first(2)
ddl.printdll()


        