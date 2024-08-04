class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class Solution:
#     def minNodeValue(head):

node1 = Node(-12)
node2 = Node(7)
node3 = Node(9)
node4 = Node(3)
node5 = -1

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = Node(node5)

# how to check for the minimum value
# transverse the whole list,
# keep one constant (head) and start the transversal from the second element
# compare with the head to return or swap
# 
head = node1

currentNode = head.next

while currentNode:
    minValue = head.data
    if minValue < currentNode.data:
        currentNode = currentNode.next
    else:
        minValue = currentNode.data
        currentNode = currentNode.next

print(f"The min value is {minValue}")


