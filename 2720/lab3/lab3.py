#part1
class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None

class Stack:
    def __init__(self, head = None) -> None:
        self.head = head if head else None

    def isEmpty(self) -> bool:
        return self.head is None
    def push(self, value):

        push_node = Node(value)
        push_node.next = self.head
        self.head = push_node
    def pop(self):
        if self.isEmpty(): return "Stackoverflow"
        pop_value = self.head.val
        self.head = self.head.next
        return pop_value
    
    def peek(self):
        if self.isEmpty(): return None
        return self.head.val
    
    def print_stack(self):
        if self.isEmpty(): return None
        current = self.head
        while current:
            print(current.val, end="->")
            current = current.next
        print("None")

#driver code

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print_stack()
print(stack.pop())
stack.print_stack()
print(stack.pop())
stack.print_stack()
stack.peek()

    
#part2
class StackList:
    def __init__(self) -> None:
        self.stack = []
    
    def isEmpty(self):
        return not self.stack

    def push(self, value):
        self.stack.append(value)
    def popping(self):
        if self.isEmpty(): return "Stack overflow"
        pop_value = self.stack.pop()
        return pop_value
    def peek(self):
        if self.isEmpty(): return "Stack is Empty"
        return self.stack[-1]
    def print_stack(self):
        if self.isEmpty(): return "Stack is None"
        print(self.stack)

        

stack2 = StackList()
stack2.push(1)
stack2.push(2)
stack2.push(3)
stack2.push(4)
stack2.print_stack()
print(stack2.popping())
stack2.print_stack()
print(stack2.popping())
stack2.print_stack()
stack2.peek()

"""
In using python List method, the elements are stored in contiguous blocks of memory, this allows fast acces to elements via index. But in using Node method, it only gives a reference to the values, which make it harder to access the index of each node.
As compared above, python List uses a big block of memory whereas the Linked List the memory is scattered
Time complexity of the following:
for Accessing by index:
Python list: O(1)\tLinked List O(n)
for push element:
both O(1)
for insertion at specfic position:
both O(n)
for pop:
python List: O(n)\tLinked List: 0(1)

In Conclusion: python list and Node are both good ways of establishing stack, depends on the usage of the data, users can consider if they want a faster access to the data index; they can choose python List or if they would like to constantly manipulating in a lot of deletion, they can use linked list.
"""