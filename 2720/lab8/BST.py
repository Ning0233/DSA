class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, val: int) -> None:
        new_node = TreeNode(val)
        if not self.root: 
            self.root = new_node
            return
        current = self.root
        while current:
            if val <= current.val:
                if current.left_child:
                    current = current.left_child
                else:
                    current.left_child = new_node
                    return
            else: 
                if current.right_child: 
                    current = current.right_child
                else:
                    current.right_child = new_node
                    return

    def search(self, val: int) -> bool:
        current = self.root
        while current:
            if val == current.val:
                return True
            elif val < current.val:
                current = current.left_child
            else:
                current = current.right_child
        return False
    
    def delete(self, val: int) -> None:
        def find_min(node):
            while node.left_child:
                node = node.left_child
            return node

        def delete_node(node, val):
            if not node:
                return node
            if val < node.val:
                node.left_child = delete_node(node.left_child, val)
            elif val > node.val:
                node.right_child = delete_node(node.right_child, val)
            else:
                if not node.left_child:
                    return node.right_child
                elif not node.right_child:
                    return node.left_child
                temp = find_min(node.right_child)
                node.val = temp.val
                node.right_child = delete_node(node.right_child, temp.val)
            return node

        self.root = delete_node(self.root, val)
        
    def inorder_traversal(self) -> list[int]:
        def traverse(node):
            return traverse(node.left_child) + [node.val] + traverse(node.right_child) if node else []
        return traverse(self.root)
    
    def preorder_traversal(self) -> list[int]:
        def traverse(node):
            return [node.val] + traverse(node.left_child) + traverse(node.right_child) if node else []
        return traverse(self.root)
    
    def postorder_traversal(self) -> list[int]:
        def traverse(node):
            return traverse(node.left_child) + traverse(node.right_child) + [node.val] if node else []
        return traverse(self.root)


