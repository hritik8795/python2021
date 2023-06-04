class Node:
    def __init__(self,value =None):
        self.value =value
        self.next =next
class LinkedList:
    def __init__(self):
        self.head =None

class stack:
    def __init__(self):
        self.LinkedList =LinkedList()
    def isEmpty(self):
        if self.LinkedList.head ==None:
            return True
        else:
            return False
    def push(self,value):
        node =Node(value)
        node.next =self.LinkedList.head
        self.LinkedList.head =node

    def pop(self):
        if self.isEmpty():
            return "the list is empty"
        else:
            nodevalue =self.LinkedList.head.value
            self.LinkedList.head =self.LinkedList.head.next
            return nodevalue
    def peek(self):
        if self.isEmpty():
            return "this LIst is empty"
        else:
            nodevalue =self.LinkedList.head.value
            return nodevalue


customStack =stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print(customStack.pop())
print(customStack)