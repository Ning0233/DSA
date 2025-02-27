    def delete_first(self):
        if not self.head: 
            print("Empty")
            return
        p = self.head
        while p.next != self.head:
            p = p.next
        p.next = p.next.next
        self.head = self.head.next