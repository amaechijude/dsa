# Implementing stack with array
# Aray is known as list in python

class Stack():
    def __init__(self) -> None:
        self.stack = []

    def push(self, element) -> list:
        self.stack.append(element)
        return self.stack
    
    def pop(self):
        element = self.stack.pop()
        return element
    
    def peek(self):
        topElement = self.stack[-1]
        return topElement
    
    def isEmpty(self) -> bool:
        sz = len(self.stack)
        return True if sz <= 0 else False
    
    def size(self):
        sz = len(self.stack)
        return sz
    
testStack = Stack()
testStack.push("hia")
print(testStack.isEmpty())