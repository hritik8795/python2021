class Node:
    def __init__(self,value=None):
        self.value =value
        self.next= next
    
class LinkedList:
    def __init__(self):
        self.head =None
    def __iter__(self):
        curNode =self.head
        while curNode:
            yield curNode
            curNode=curNode.next
    
class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()
    def __str__(self):
        values =[str(x)for x in self.LinkedList]
        return '\n'.join(values)
    
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
            return "this stack is empty"
        else:
            nodevalue =self.LinkedList.head.value
            self.LinkedList.head =self.LinkedList.head.next
            return nodevalue
            
    def peek(self):
        if self.isEmpty():
            return "this stack is empty"
        else:
            nodevalue =self.LinkedList.head.value
            return nodevalue
CustomStack =Stack()
CustomStack.push(1)
CustomStack.push(2)
CustomStack.push(3)
print(CustomStack)
print(CustomStack.peek())
print(CustomStack.pop())
