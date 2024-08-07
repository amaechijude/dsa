# Queue follows first in first out like in resturant
# Method enqueue adds ne element to the last one in the queue called rear
# Method dequeue removes the first element, otherwise known as front
# Method isEmpty checks if the queue is empty. returns a bool
# Method Size returns the size of the Queue
# Method Front reurns the first element on the Queue
# Method Rear reurns the last element on the Queue

# NB: Make dequeue and enqueue O(1) operation

class Queue:
    def __init__(self) -> None:
        self.queue = []

    def show(self): # shows the queue
        return f"List: -> {self.queue}"

    def enqueue(self, element) -> None: # insert element
        self.queue.append(element)
        return

    def dequeue(self): #Removes the first element
        if self.isEmpty():
            return "Empty list"
        rem = self.queue.pop(0)
        return rem

    def isEmpty(self) -> bool:
        return len(self.queue) < 1

    def size(self)  -> int: #returns the size
        return len(self.queue)

    def front(self):
        if self.isEmpty():
            return "empty list"
        return self.queue[0]
    
    def rear(self):
        if self.isEmpty():
            return "empty list"
        return self.queue[-1]
    

print("Queue with Array List\n")

myQueue = Queue()
print(f"isEmpty: -> {myQueue.isEmpty()}")
print(f"Size: -> {myQueue.size()}")
print(f"{myQueue.show()}")

myQueue.enqueue("chai")
myQueue.enqueue("ewoo!")
myQueue.enqueue("too")
myQueue.enqueue("shock")

print("\nenqueued 4 elemnts\n")

print(f"isEmpty: -> {myQueue.isEmpty()}")
print(f"Size: -> {myQueue.size()}")
print(f"{myQueue.show()}")
print(f"dequed: -> {myQueue.dequeue()}")
print(f"isEmpty: -> {myQueue.isEmpty()}")
print(f"Size: -> {myQueue.size()}")
print(f"{myQueue.show()}")