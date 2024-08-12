class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None


root = TreeNode("Head")
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(4)

root.left = node1
root.right = node2

node1.left = node3

print(root.left.left.data)

def traverse(node = None):
    if node is None:
        return None
    print(node.data, end=" -> ")
    traverse(node.left)
    traverse(node.right)

traverse(root)