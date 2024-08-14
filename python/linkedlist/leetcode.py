class ListNode:
    def __init__(self, data=0) -> None:
        self.data = data
        self.next = None

n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(8)

n1.next = n2
n2.next = n3
n3.next = n4

curr = n1
while curr:
    print(curr.data,end=' -> ')
    curr = curr.next
print('end\n')

m1 = ListNode(5)
m2 = ListNode(6)
m3 = ListNode(4)
m4 = ListNode(5)

m1.next = m2
m2.next = m3
m3.next = m4

currn = m1
while currn:
    print(currn.data,end=' -> ')
    currn = currn.next
print('end\n')

def addNode(l1: ListNode, l2: ListNode) -> ListNode:
    dummyHead = ListNode(0)
    tail = dummyHead
    carry = 0

    while l1 or l2 or carry != 0:
        digit1 = l1.data if l1 else 0
        digit2 = l2.data if l2 else 0

        dsum = digit1 + digit2 + carry
        digit = dsum % 10
        carry = dsum // 10

        # create newNode with the digit
        newNode = ListNode(digit)
        tail.next = newNode
        tail = tail.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    result = dummyHead.next
    while result:
        print(result.data,end=" -> ")
        result = result.next
    print('end')


addNode(n1, m1)
    
