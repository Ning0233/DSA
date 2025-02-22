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
        while p:
            print(p.data, end="->")
            p = p.next
        print("None") if self.head else None

    def insert_first(self, value: int) -> None:
        p = ListNode(value)
        if not self.head:
            self.head = self.tail = p
            return
        p.next = self.head
        self.head.prev = p
        self.head = p
    def insert_last(self, value: int) -> None:
        p = ListNode(value)
        if not self.head:
            self.head = self.tail = p
            return
        self.tail.next = p
        p.prev = self.tail
        self.tail = p
    def delete_node(self, value: int) -> None:    
        p = self.head
        if not p: return "empty list"
        while p:
            if p.data == value:
                if p.prev: #none head handle next node
                    p.prev.next = p.next
                else: # head
                    self.head = p.next
                if p.next: # none tail handle prev node
                    p.next.prev = p.prev
                else: # tail
                    self.tail = p.prev
                return
            p = p.next
        print("not found")
        return
    
    def search_node(self, value: int) -> bool:
        p = self.head
        if not p: return False
        
        elif self.head.data == value or self.tail.data == value:
            return True
            
        while p:
            if p.data == value:
                return True
            p = p.next
        return False
    
    def insert_after(self, node: int, value: int) -> None:
        if not self.search_node(node): 
            print("node is not found") 
            return
        p = self.head
        n = ListNode(value)
        if not p: 
            return "node is not found"
        while p:
            if p.data == node:
                n.next = p.next
                n.prev = p
                if p.next: # none tail handle prev node
                    p.next.prev= n
                else: # tail
                    self.tail = n
                p.next = n
                return
            p = p.next
        print("not found")
        return
    def length(self) -> int:
        p = self.head
        count = 0
        if not p: 
            return count
        while p:
            count += 1
            p = p.next
        return count
    
    def reverse(self) -> None:
        p = self.head
        temp = None
        while p:
            temp = p.prev
            p.prev = p.next
            p.next = temp
            p = p.prev
        if temp:
            self.head, self.tail = self.tail, self.head
            self.head = temp.prev

    def remove_duplicates(self) -> None:
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                duplicate = current.next
                current.next = duplicate.next
                if duplicate.next:
                    duplicate.next.prev = current
                else:
                    self.tail = current
            else:
                current = current.next

    def rotate(self, n: int) -> None:
        if not self.head or n == 0:
            return
        
        length = self.length()

        
        n = n % length
        if n == 0:
            return
        
        current = self.head
        for _ in range(length - n - 1):
            current = current.next
        
        new_head = current.next
        new_tail = current
        
        new_head.prev = None
        new_tail.next = None
        
        self.tail.next = self.head
        self.head.prev = self.tail
        
        self.head = new_head
        self.tail = new_tail





        