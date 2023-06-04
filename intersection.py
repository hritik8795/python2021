from LinkedList import LinkedList,Node
def intersection(llA,llB):
    if llA.tail is not llB.tail:
        return False
        #for length
    lenA =len(llA)
    lenB =len(llB)
    #for choosing which is larger 

    shorter =llA if lenA<lenB else llB
    longer =llB if lenA<lenB else llA

    #for finding difference,esse pata chalega ki kitne node ko ignore karna hai joki doosre node se jada hai
    diff =len(longer)-len(shorter)
    longerNode =longer.head
    shorterNode =shorter.head

    #for ignore the extra node
    for i  in range(diff):
        longerNode =longerNode.next

    while shorterNode is not longerNode:
        shorterNode =shorterNode.next
        longerNode =longerNode.next
        
    return longerNode

    #helper addition method 
def addSameNode(llA,llB,value):
    tempNode = Node(value)
    llA.tail.next =tempNode
    llA.tail =tempNode
    llB.tail.next =tempNode
    llB.tail =tempNode
llA =LinkedList()
llA.generate(3,0,10)

llB =LinkedList()
llB.generate(4,0,10)

addSameNode(llA,llB,11)
addSameNode(llA,llB,7)

print(llA)
print(llB)
print(intersection(llA,llB))