class Node:
    def __init__ (self ,value =None):
        self.value =value
        self.next =None
        self.prev =None
class DoublyLinkedList:
    def __init__ (self):
        self.head =None
        self.tail =None
    
    def __iter__(self):
        node =self.head
        while node:
            yield node
            node =node.next
    
    def CreateDLL(self,nodeValue):
        node =Node(nodeValue)
        node.prev =None
        node.next =None
        self.head =node
        self.tail =node
        return "the node is created successfully"

    def insertDll(self,nodeValue,location):
        if self.head is None:
            print("we can not add any element in the dll")
        else:
            newNode =Node(nodeValue)
            if location ==0:
                newNode.prev =None
                newNode.next =self.head
                self.head.prev =newNode
                self.head =newNode
            elif location ==1:
                newNode.next =None
                newNode.prev =self.tail
                self.tail.next =newNode
                self.tail =newNode
            else:
                tempNode =self.head
                index =0
                while index < location-1:
                    index +=1
                newNode.next =tempNode.next
                newNode.prev =tempNode
                newNode.prev.next =newNode
                tempNode.next = newNode
    
    def traverseDll(self):
        if self.head is None:
            print("there is not any more element for taverse")
        else:
            tempNode =self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    #def searchDLL(self ,nodeValue):
     #   if self.head is None:
      #      print("there is no element in the dll")
       # else:
        #    tempNode =self.head
         #   while tempNode:
          #      if tempNode.value ==nodeValue:
           #         return tempNode.value
            #        tempNode =tempNode.next
             #       return "the node does not exist"
    
    def deleteNode(self ,location):
        if self.head is None:
            print("there is nothing for delete")
        else:
            if location ==0:
                if self.head ==self.tail:
                    self.head =None
                    self.tail =None
                else:
                    self.head =self.head.next
                    self.head.prev =None
            elif location==1:
                if self.head == self.tail:
                    self.head =None
                    self.tail =None
                else:
                    self.tail =self.tail.prev
                    self.tail.next =None
            else:
                curNode =self.head
                index =0
                while index<location-1:
                    index +=1
                curNode.next =curNode.next.next
                curNode.next.prev =curNode
                print("the node is successfully deleted")                

doublyLL=DoublyLinkedList()
doublyLL.CreateDLL(5)
print([Node.value for Node in doublyLL])
doublyLL.insertDll(0,0)
doublyLL.insertDll(1,1)
doublyLL.insertDll(3,2)
print([Node.value for Node in doublyLL])
#doublyLL.traverseDll()
#print(doublyLL.searchDLL(6))
doublyLL.deleteNode(0)
print([Node.value for Node in doublyLL])