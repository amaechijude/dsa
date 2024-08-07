# Implementing stack with a linked list

# create a Node class to hold the linked list
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


# Create the stack class and methods
class Stack:
    def __init__(self):
        self.headNode = None
        self.size = 0

    def show(self):
        if self.headNode is None:
            print("Empty")
        else:
            currentNode = self.headNode
            while currentNode:
                print(f"{currentNode.data}", end=" -> ")
                currentNode = currentNode.next
            print('end')
        
    def push(self, element):
        newNode = Node(element)
        newNode.next = self.headNode
        self.headNode = newNode

    def pop(self):
        temp = self.headNode # temporary variable to hold the popped node
        self.headNode = self.headNode.next
        return temp.data

    def peek(self):
        return self.headNode

    def isEmpty(self) -> bool:
        return f"Node isEmpty:-> {self.headNode is None}"

    def listSize(self) -> int:
        if self.headNode is None:
            return f"Total nodes is : {self.size}"
        
        currentNode = self.headNode
        while currentNode:
            self.size += 1
            currentNode = currentNode.next
        return f"Total nodes is : {self.size}"



stack = Stack()
print(stack.isEmpty())
print(stack.listSize())
stack.push("chai")
stack.push("abia")
stack.push("okay")
stack.show()
print(stack.pop())
stack.show()
print(stack.listSize())
stack.push("haha")
stack.push("egwu")
stack.show()
print(stack.listSize())
print(stack.isEmpty())
