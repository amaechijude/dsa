class Node:
    def __init__(self, data:int) -> None:
        self.data = data
        self.next = None

      
node1 = Node(-12)
node2 = Node(7)
node3 = Node(9)
node4 = Node(3)
node5 = Node(-1)

xnode = Node(43)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


from solution import Solution

solution = Solution()
solution.transverseAndPrint(node1)
node1 = solution.sortNode(node1)
solution.transverseAndPrint(node1)


