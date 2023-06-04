class Node:
    def __init__(self,value=None):
        self.value = value
        self.next= None
class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
#insert in linked list
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head =newNode 
            self.tail =newNode
        else:
            if location ==0:
                newNode.next=self.head
                self.head=newNode
            elif location ==1:
                newNode.next =None
                self.tail.next = newNode
                self.tail=newNode
            else:
                tempNode = self.head
                index=0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                #traverse the singlylinked list
    def traverseSLL(self):
        if self.head is Node:
            print("the link list does not exist")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node = node.next

    #search the element
    def searchElement(self,nodeValue):
        if self.head is None:
            return "the list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                    node = node.next
                return "the value exist at the list"
                #deleetion of node
                def deleteNode(self,location):
                    if self.head ==None:
                        return "linklist is already empty"
                    else:
                        if location ==0:
                            if self.head =self.tail:
                                self.head = None
                                self.tail = None
                            else:
                                self.head = self.head.next
                        elif location==1:
                            if self.head == self.tail:
                                self.head = None
                                self.tail =None
                            else:
                                self.head

 
singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(0,0)
singlyLinkedList.insertSLL(0,4)


print([node.value for node in singlyLinkedList])
singlyLinkedList.traverseSLL()
print(singlyLinkedList.searchElement(3))