class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None


root = TreeNode("root")
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(7)
node7 = TreeNode(8)
node8 = TreeNode(9)

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5
node2.right = node6

node3.left = node7
node3.right = node8

node7.left = TreeNode("rLend")
node6.right = TreeNode("rRend")

