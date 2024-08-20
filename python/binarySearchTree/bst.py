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


class Solution:
    def __init__(self) -> None:
        pass

    def insert(self, rootNode: TreeNode, val:int) -> TreeNode:
        if rootNode is None:
            return TreeNode(val)
        else:
            if val < rootNode.data:
                rootNode.left = self.insert(rootNode.left, val)
            elif val > rootNode.data:
                rootNode.right = self.insert(rootNode.right, val)
            return rootNode
        
    def maxValue(self, rootNode:TreeNode):
        currentNode = rootNode
        while currentNode.right is not None:
            currentNode = currentNode.right
        return f"The Max value is:-> {currentNode.data}"
    
    def minValue(self, rootNode:TreeNode) -> str:
        currentNode = rootNode
        while currentNode.left is not None:
            currentNode = currentNode.left
        return f"The Min value is:-> {currentNode.data}"

    



root = TreeNode(21)
s = Solution()
s.insert(root, 44)
s.insert(root, 51)
s.insert(root, 71)
s.insert(root, 10)
s.insert(root, 2)
s.insert(root, 1)
s.insert(root, 0)
s.insert(root, 69)
print(s.maxValue(root))
print(s.minValue(root))

def inOrderTraversal(rootNod: TreeNode):
    if rootNod is None:
        return None
    inOrderTraversal(rootNod.left)
    print(rootNod.data, end=" -> ")
    inOrderTraversal(rootNod.right)


inOrderTraversal(root)
print()