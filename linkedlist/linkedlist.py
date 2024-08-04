class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

month1 = Node("jan")
month2 = Node("feb")
month3 = Node("mar")
month4 = Node("apr")

month1.next = month2

month2.next = month3
month2.previous = month1

month3.next = month4
month3.previous = month2


month4.previous = month3

# forward transversal
currentNode = month1
print("forward transversal")
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print('')

# backward transversal
currentNode = month4
print("backward transversal")
while currentNode:
    print(currentNode.data, end=" <- ")
    currentNode = currentNode.previous

print('')