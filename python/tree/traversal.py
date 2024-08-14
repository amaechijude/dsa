from tree import root

class treeTraversal:
    def __init__(self) -> None:
        pass
    
    def preOrderTraversal(self, rootNode):
        if rootNode is None:
            return None
        print(rootNode.data, end=" -> ")
        self.preOrderTraversal(rootNode.left)
        self.preOrderTraversal(rootNode.right)

    
    def inOrderTraversal(self, rootNode):
        if rootNode is None:
            return None
        self.inOrderTraversal(rootNode.left)
        print(rootNode.data, end=" -> ")
        self.inOrderTraversal(rootNode.right)

    def postOrderTraversal(self, rootNode):
        if rootNode is None:
            return None
        self.postOrderTraversal(rootNode.left)
        self.postOrderTraversal(rootNode.right)
        print(rootNode.data, end=" -> ")


trav = treeTraversal()

print("\npreOrder:->")
trav.preOrderTraversal(root)

print("\n\ninOrder:->")
trav.inOrderTraversal(root)

print("\n\npostOrder:->")
trav.postOrderTraversal(root)

print()