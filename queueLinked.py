class Node:
    def __init__(self,value=None):
        self.value =value
        self.next =None
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self):
        self.head =None
        self.tail =None
    def __iter__(self):
        curNode =self.head
        while curNode:
            yield curNode
            curNode=curNode.next

class queue:
    def __init__(self):
        self.LinkedList =LinkedList()

    def __str__(self):
        values =[str(x) for x in self.LinkedList]
        return ''.join(values)
    
    def enqueue(self,value):
        newNode =Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head =newNode
            self.LinkedList.tail =newNode
        else:
            self.LinkedList.tail.next =newNode


    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False


    def dequeue(self):
        if self.isEmpty():
            return 'the queue is empty'
        else:
            TempNode=self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head =None
                self.LinkedList.tail =None
            else:
                self.LinkedList.head =self.LinkedList.head.next
                return TempNode

    def peek(self):
        if self.isEmpty():
            return 'there is no element in the queue'
        else:
            self.LinkedList.head


    def delete(self):
        self.LinkedList.head=None
        self.LinkedList.tail=None
customqueue =queue()
customqueue.enqueue(1)
customqueue.enqueue(2)
customqueue.enqueue(3)
print(customqueue)
print(customqueue.peek())
print(customqueue.isEmpty())