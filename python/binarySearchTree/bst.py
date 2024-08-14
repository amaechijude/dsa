"""
A Binary Search Tree is a Binary Tree where every node's left child has a lower value,
and every node's right child has a higher value.

A clear advantage with Binary Search Trees is that operations like search, delete, 
and insert are fast and done without having to shift values in memory.
"""

class TreeNode:
    def __init__(self, data:int) -> None:
        self.data = data
        self.left = None
        self.right = None

    
def insert(rootNode:TreeNode, val:int):
    newNode = TreeNode(val)
    if rootNode.data is None:
        rootNode = newNode
        return f"Root insert:-> {rootNode.data}"
    if val < rootNode.data:
        if rootNode.left is None:
            rootNode.left = newNode
            return f"None left Insert:-> {val}"
        rootNode.left = insert(rootNode.left, val)
        return f"Other left Insert:-> {val}"
    elif val > rootNode.data:
        if rootNode.right is None:
            rootNode.right = newNode
            return f"None right Insert:-> {val}"
        rootNode.right = insert(rootNode.right, val)
        return f"Other Insert:-> {val}"
    return "Value exists"


root = TreeNode(21)
print(insert(root, 21))
print(insert(root, 20))
print(insert(root, 19))

