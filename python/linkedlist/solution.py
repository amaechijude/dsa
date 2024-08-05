
class Solution():

    def transverseAndPrint(self, head):
        currentNode = head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode =currentNode.next
        print('end')


    def delete_node(self, headNode, nodeToDelete):
        if headNode == nodeToDelete:
            return headNode.next
        
        currentNode = headNode
        while currentNode.next and currentNode.next != nodeToDelete:
            currentNode = currentNode.next

        if currentNode.next == None:
            return headNode
        
        currentNode.next = currentNode.next.next

        return headNode
    
    def insertNode(self, headNode, newNode, position:int):
        if position == 1:
            newNode.next = headNode
            return newNode
        
        currentNode = headNode
        # for _ in range(position - 2):
        #     pass

        # # Swap node position
        newNode.next = currentNode.next
        currentNode.next = newNode

        return headNode
    
    def InsertAtEnd(self, headNode, newNode):
        currentNode = headNode
        while currentNode:
            if currentNode.next is None:
                currentNode.next = newNode
                break

            currentNode = currentNode.next

        return headNode
