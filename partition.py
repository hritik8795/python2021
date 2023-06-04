#yahan hum linked list me ek element x lenge aur jo element xvse bada
#  hoga wo wo x ke right aayega aur jo chota hoga wo left me ayega 
from LinkedList import LinkedList
def partition(ll,x):
    curNode =ll.head
    ll.tail =ll.head

    while curNode:
        nextNode =curNode.next
        curNode.next =None
        if curNode.value < x:
            curNode.next =ll.head
            ll.head =curNode
        else:
            ll.tail.next =curNode
            ll.tail =curNode
        scurNode =nextNode
    if ll.tail.next is not None:
        ll.tail.next =None
customLL =LinkedList()
customLL.generate(10,0,99)
print(customLL)
print(customLL,30)
print(len(customLL))
