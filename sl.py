#second step we need to initialize node with reference to value 
class Node:
    def __init__(self,value=None):
        self.value =value
        self.next = None

#frist step in single linked list
#create head and tail and assign null reference to it
class SLinkedList:
    def __init__(self):
        self.head  = None
        self.tail = None
    def __iter__(self):
        newNode =self.node 
        while node:
            yield node
            node=node.next
#insert in linked list
    def insertSLL(self , value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location ==0:
                newNode.next = self.head
                self.head = newNode
            elif location==1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                newNode = tempNode.next
                tempNode.next =newNode
                newNode.next= nextNode

                #traverse the lin
singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(5,1)
singlyLinkedList.insertSLL(3,1)


print([node.value for node in singlyLinkedList])
#now we should create a new linked list with two node
#singlyLinkedList = SLinkedList()
#node1 = Node(1)
#node2 = Node(2)

#yahan par head node1 hoga aur head.next hoga node2 aur wo hi tail hoga 
#singlyLinkedList.head = node1
#singlyLinkedList.head.next = node2
#singlyLinkedList.tail = node2

