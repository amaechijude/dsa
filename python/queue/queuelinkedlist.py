# Queue follows first in first out like in resturant
# Method enqueue adds ne element to the last one in the queue called rear
# Method dequeue removes the first element, otherwise known as front
# Method isEmpty checks if the queue is empty. returns a bool
# Method Size returns the size of the Queue
# Method Front reurns the first element on the Queue
# Method Rear reurns the last element on the Queue

# NB: Make dequeue and enqueue O(1) operation
#Try using doubly linked list

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.rear =None

class Queue:
    def __init__(self) -> None:
        self.firstNode = None
        self.length = 0

    def show(self):
        if self.firstNode is None:
            print("Show:-> Empty queue")
        else:
            currentNode = self.firstNode
            while currentNode:
                print(currentNode.data, end=" -> ")
                currentNode = currentNode.next
            print(" ")

    def enqueue(self, element) -> None:
        newRearNode = Node(element)
        if self.firstNode is None:
            self.firstNode = newRearNode
            return
        currentNode = self.firstNode
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = newRearNode

    
    def dequeue(self):
        temp = self.firstNode
        if self.firstNode is None:
            return "Empty queue"
        self.firstNode = self.firstNode.next
        return f"Popped:-> {temp.data}"
    
    def isEmpty(self) -> bool:
        return self.firstNode is None
    
    def size(self) -> int:
        if self.firstNode is None:
            return self.length
        currentNode = self.firstNode
        while currentNode:
            self.length += 1
            currentNode = currentNode.next
        return self.length
    
    def front(self):
        return self.firstNode.data
    
    def rear(self):
        if self.size() == 1 or self.firstNode is None:
            return self.firstNode.data
        currentNode = self.firstNode
        while currentNode:
            currentNode = currentNode.next
        return currentNode.data
    

print("Queue with Linked List\n")

myQueue = Queue()
print(f"isEmpty: -> {myQueue.isEmpty()}")
print(f"Size: -> {myQueue.size()}")
myQueue.show()

myQueue.enqueue("chai")
myQueue.enqueue("ewoo!")
myQueue.enqueue("too")
myQueue.enqueue("shock")

print("\nenqueued 4 elemnts\n")

print(f"isEmpty: -> {myQueue.isEmpty()}")
print(f"Size: -> {myQueue.size()}")
myQueue.show()
print(f"dequed: -> {myQueue.dequeue()}")
print(f"isEmpty: -> {myQueue.isEmpty()}")
print(f"Size: -> {myQueue.size()}")
myQueue.show()