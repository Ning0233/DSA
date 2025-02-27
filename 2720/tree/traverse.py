class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Preorder Traversal (Root, Left, Right)
def preorder(root):
    if root:
        print(root.value, end=" ")  # Visit the root node
        preorder(root.left)         # Traverse the left subtree
        preorder(root.right)        # Traverse the right subtree

# Inorder Traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)          # Traverse the left subtree
        print(root.value, end=" ")  # Visit the root node
        inorder(root.right)         # Traverse the right subtree

# Postorder Traversal (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)        # Traverse the left subtree
        postorder(root.right)       # Traverse the right subtree
        print(root.value, end=" ")  # Visit the root node

# Example of constructing a bin
