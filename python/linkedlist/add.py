class Node1:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None

class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

fnode1, fnode2, fnode3  = Node1(3), Node1(4), Node1(5)
fnode1.next = fnode2
fnode2.next = fnode3

fnode3.previous = fnode2
fnode2.previous = fnode1

# secone linked list
snode1, snode2, snode3 = Node2(6), Node2(7), Node2(8)
snode1.next = snode2
snode2.next = snode3

snode3.previous = snode2
snode2.previous = snode1



currentnNode = fnode3

while currentnNode:
    print(currentnNode.data, end=" -> ")
    currentnNode = currentnNode.previous
print("\n")

currentnNode = snode3

while currentnNode:
    print(currentnNode.data, end=" -> ")
    currentnNode = currentnNode.previous
print()