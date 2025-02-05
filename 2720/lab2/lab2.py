class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
# tranversal 
    def __init__(self) -> None:
        self.head = None

    def insertBeginning(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
        return self.head
    
    def insertEnd(self, new_value):
        new_node = Node(new_value)
        if not self.head: 
            self.head = new_node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        return self.head

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def insertSpecific(self, new_value, position=None):
        if position == 1: self.insertBeginning(self, new_value)

        new_node = Node(new_value)
        temp = self.head
        for _ in range(1, position):
            if not temp: 
                print("position out of bound")
                return self.head
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        return self.head
        
    def insertMiddle(self, new_value):
        middle=self.length()//2
        
        #this function inserts in the middle of a linked list, it counts the total length; takes the half. if even insert in middle, if odd insert after round down to half
        self.insertSpecific(new_value, position=middle+1)

    def deleteValue(self, value):
        #error handling
        if not self.head: 
            print("-1")
        #if head node
        if self.head.data == value: 
            self.head = self.head.next
            return self.head
        
        pre_key = self.head
        key = self.head.next

        while key:
            if key.data == value: 
                pre_key.next = key.next
                return self.head
            pre_key = key
            key = key.next
        print(f"{value} not found")
        return self.head

    def search(self, value):

        if not self.head:
            print("empty list")

        #if self.head.data == value: print("1")

        count = 0
        key = self.head
        while key:
            count += 1
            if key.data == value:
                print(f"{value} is a postion {count}")
                return
            key = key.next
        print(f"{value} not found")

    def reverse(self):
        prev = None
        current = self.head

        # before: prev-> current -> after . save after, current.next -> prev; saved after -> pre 
        while current:
            after = current.next
            current.next = prev
            prev = current
            current = after
        self.head = prev
        return self.head
    
    def findMiddle(self):
        # this function returns 2 middle values if it's an even indexed list
        if not self.head: return "Empty list"

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if not fast: return (slow.data, slow.next.data)
        else:  return slow.data 

    def traverse_linked_list(self):
        current = self.head
        if not current: print("linked list is empty")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")


def main():
    #creating empty list
    linked_list = SingleLinkedList()
    linked_list.traverse_linked_list()
    # insert from beginning
    linked_list.insertBeginning(40)
    linked_list.traverse_linked_list()
    linked_list.insertBeginning(30)
    linked_list.traverse_linked_list()
    linked_list.insertBeginning(20)
    linked_list.traverse_linked_list()
    linked_list.insertBeginning(10)
    linked_list.traverse_linked_list()

    #insert from end
    linked_list.insertEnd(90)
    linked_list.traverse_linked_list()
    linked_list.insertEnd(100)
    linked_list.traverse_linked_list()
    linked_list.insertEnd(110)
    linked_list.traverse_linked_list()
    linked_list.insertEnd(120)
    linked_list.traverse_linked_list()

    #insert from position OR middle
    linked_list.insertSpecific(50, position=4)
    linked_list.traverse_linked_list()
    linked_list.insertMiddle(60)
    linked_list.traverse_linked_list()
    linked_list.insertMiddle(70)
    linked_list.traverse_linked_list()
    linked_list.insertSpecific(80, position=7)
    linked_list.traverse_linked_list()

    # delete
    linked_list.deleteValue(10)
    linked_list.traverse_linked_list()
    linked_list.deleteValue(10)
    linked_list.traverse_linked_list()
    linked_list.deleteValue(120)
    linked_list.traverse_linked_list()
    linked_list.deleteValue(70)
    linked_list.traverse_linked_list()

    # search
    linked_list.search(10)
    linked_list.search(20)
    linked_list.search(110)

    #length
    linked_list.traverse_linked_list()
    print(linked_list.length())

    #reverse
    linked_list.reverse()
    linked_list.traverse_linked_list()

    #find middle
    print(linked_list.length())
    print(linked_list.findMiddle())
    linked_list.insertEnd(10)
    linked_list.traverse_linked_list()
    print(linked_list.length())
    print(linked_list.findMiddle())



if __name__ == "__main__":
    main()