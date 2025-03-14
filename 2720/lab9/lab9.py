class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self, postfix_expr: str) -> None:
        self.root = self.construct_expression_tree(postfix_expr)

    def construct_expression_tree(self, postfix: str) -> TreeNode:
        stack = []
        for char in postfix.split():
            if char.isdigit():
                stack.append(TreeNode(int(char)))
            else:
                node = TreeNode(char)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        return stack.pop() if stack else None

    def evaluate_expression(self, node: TreeNode = None) -> int | float:
        if node is None:
            node = self.root
        if node.left is None and node.right is None:
            return node.value
        left_val = self.evaluate_expression(node.left)
        right_val = self.evaluate_expression(node.right)
        try:
            if node.value == '+':
                return left_val + right_val
            elif node.value == '-':
                return left_val - right_val
            elif node.value == '*':
                return left_val * right_val
            elif node.value == '/':
                return left_val / right_val
        except ZeroDivisionError:
            return float('inf')

    def get_inorder_expression(self, node: TreeNode = None) -> str:
        if node is None:
            node = self.root
        if node.left is None and node.right is None:
            return str(node.value)
        left_expr = self.get_inorder_expression(node.left)
        right_expr = self.get_inorder_expression(node.right)
        return f"({left_expr}{node.value}{right_expr})"
