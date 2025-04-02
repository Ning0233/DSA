class PriorityQueue:
    """
    A class to represent a Min Heap-based Priority Queue.
    """

    def __init__(self):
        """
        Initializes an empty priority queue using a list.
        """
        self.heap = []

    def insert(self, item):
        """
        Inserts a new item into the priority queue.

        Parameters:
        item (int): The item to be inserted.
        """
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def peek(self):
        """
        Returns the minimum element without removing it.

        Returns:
        int: The minimum element in the priority queue.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty priority queue")
        return self.heap[0]

    def extract(self):
        """
        Removes and returns the minimum element.

        Returns:
        int: The minimum element removed from the priority queue.
        """
        if self.is_empty():
            raise IndexError("Extract from an empty priority queue")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def is_empty(self):
        """
        Returns True if the queue is empty, otherwise False.

        Returns:
        bool: True if the priority queue is empty, False otherwise.
        """
        return len(self.heap) == 0

    def length(self):
        """
        Returns the number of elements in the priority queue.

        Returns:
        int: The number of elements in the priority queue.
        """
        return len(self.heap)

    def _heapify_up(self, index):
        """
        Maintains the heap property by moving the element at the given index up.

        Parameters:
        index (int): The index of the element to heapify up.
        """
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        """
        Maintains the heap property by moving the element at the given index down.

        Parameters:
        index (int): The index of the element to heapify down.
        """
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)