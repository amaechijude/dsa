# Implementing stack with a linked list

# create a Node class to hold the linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


# Create the stack class and methods
class Stack:
    def __init__(self) -> None:
        self.headNode = None
        self.size = 0
        
    def push(self, element=None):
        newNode = Node(element)
        currentNode = self.headNode
        
        if self.headNode == None:
            return newNode
        
        while currentNode and currentNode.next == None:
            self.headNode.next = newNode
            currentNode = currentNode.next

        return self.headNode
    
    def pop(self):
        currentNode = self.headNode
        if currentNode == None:
            return "Empty stack"
        while currentNode.next and currentNode.next.next != None:
            currentNode = currentNode.next
        temp = currentNode.next.data
        currentNode = None
        return temp

stack = Stack()
stack.push("chai")

stack.push("chai")

print(stack.pop())