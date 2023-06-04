class Node:
    def __init__(self,value=None):
        self.value =value
        self.next = None
        self.prev = None
class DoublyLinnkedList:
    def __init__(self):
        self.head =None
        self.tail =None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    #creation
    def createDLL(self,nodeValue):
        node = Node(nodeValue)
        node.prev =None
        node.next = None
        self.head = node
        self.tail=node
        return "doubly linkedlist ceated successfully"

doublyLL =DoublyLinnkedList()
doublyLL.createDLL(5)

print([node.value for node in doublyLL])