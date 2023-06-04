class Node:
    def __init__(self,value =None):
        self.value =value
        self.next =None
        self.prev =None
    
class circularDLL:
    def __init__(self):
        self.head =None
        self.tail =None
    
    def __iter__ (self):
        node =self.head
        while node:
            yield node
            node =node.next
            if node == self.tail.next:
                break

#creation of a node in circular dll
    def CreateCDLL(self,nodeValue):
        newNode =Node(nodeValue)
        self.head =newNode
        self.tail =newNode
        newNode.prev = newNode
        newNode.next =newNode
        return "the node is created successfully"

#insertCDLL
    def insertCDLL(self,value,location):
        if self.head is None:
            print("the cdll is noot exists")
        else:
            newNode =Node(value)
            if location ==0:
                newNode.next =self.head
                newNode.prev =self.tail
                self.head.prev =newNode
                self.head =newNode
                self.tail.next =newNode
            elif location ==1:
                newNode.next =self.head
                newNode.prev =self.head
                self.head.prev =newNode
                self.tail.next =newNode
                self.tail =newNode
            
            else:
                tempNode =self.head
                index =0
                while index<location-1:
                    tempNode =tempNode.next
                    index +=1
                newNode.next =tempNode.next
                newNode.prev =tempNode
                newNode.next.prev =newNode
                tempNode.next =newNode
                return "the node has been created"
    def traverseCDLL(self):
        if self.head is None :
            print("othing to traverse")
        else:
            tempNode =self.head
            while tempNode:
                print(tempNode.value)
                if tempNode ==self.tail:
                    break
                tempNode =tempNode.next
    def revtraverseCDLL(self):
        if self.head is None:
            print("the cdll is empty")
        else:
            tempNode =self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode ==self.head:
                    break
                tempNode =tempNode.prev
    
#search any node from a cdll
    def searchCDLL(self,nodeValue):
        if self.head is None:
            return"there is no element for search"
        else:
            tempNode =self.head
            while tempNode:
                if tempNode ==nodeValue:
                    return tempNode.value
                if tempNode ==self.tail:
                    return "the node is not exist in the cdll"
                tempNode =tempNode.next
#deleting the node
    def deleteCDLL(self,location):
        if self.head is None:
            print("there is no element for delete")
        else:
            if location ==0:
                if self.head ==self.tail:
                    self.head.prev =None
                    self.head.next =None
                    self.head =None
                    self.tail =None
                else:
                    self.head =self.head.next
                    self.head.prev =self.tail
                    self.tail.next =self.head
            elif location ==1:
                if self.head==self.tail:
                    self.head.prev =None
                    self.head.next =None
                    self.head =None
                    self.tail =None
                else:
                    self.tail =self.tail.prev
                    self.tail.next =self.head
                    self.head.prev =self.tail

            else:
                curNode =self.head
                index =0
                curNode =curNode.next
                index +=1
                curNode.next =curNode.next.next
                curNode.next.prev =curNode
            print("the node is success fully deleted")
    
    def deleteALL(self):
        if self.head is None:
            print("there is no element fo r delete")
        else:
            self.tail.next =None
            tempNode =self.head
            while tempNode:
                tempNode.prev =None
                tempNode =tempNode.next
                self.head =None
                self.tail =None
                print("the cdll is been deleteed")






circularDLL = circularDLL()
print(circularDLL.CreateCDLL(5))
print([node.value for node in circularDLL])
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
circularDLL.insertCDLL(3,3)
circularDLL.insertCDLL(4,4)
circularDLL.deleteALL()
print([node.value for node in circularDLL])

#circularDLL.traverseCDLL()
#circularDLL.revtraverseCDLL()
print(circularDLL.searchCDLL(4))
circularDLL.deleteCDLL(1)
print([node.value for node in circularDLL])