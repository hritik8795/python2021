import QueueLinkedList as queue
class BstNode:
    def __init__(self,data):
        self.data =data
        self.leftchild =None
        self.rightchild =None
    
def insertNode(rootNode,nodevalue):
    if rootNode.data ==None:
        rootNode.data =nodevalue
    elif nodevalue<=rootNode.data:
        if rootNode.leftchild is None:
                rootNode.leftchild =BstNode(nodevalue)
        else:
                insertNode(rootNode.leftchild,nodevalue)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild =BstNode(nodevalue)
        else:
            insertNode(rootNode.rightchild,nodevalue)
    return "the node is inserted success fully"

def preOrderTraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preOrderTraversal(rootnode.leftchild)
    preOrderTraversal(rootnode.rightchild)

#in order 
def InOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        InOrderTraversal(rootNode.leftchild)
        print(rootNode.data)
        InOrderTraversal(rootNode.rightchild)

def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        postOrderTraversal(rootNode.leftchild)
        postOrderTraversal(rootNode.rightchild)
        print(rootNode.data)
    
def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    customQueue =queue.Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root =customQueue.dequeue()
        print(root.value.data)
    if root.value.rightchild is not None:
        customQueue.enqueue(root.value.leftchild)
    if root.value.rightchild is not None:
        customQueue.enqueue(root.value.rightchild)
      
newBst =BstNode(None)
insertNode(newBst,70)
insertNode(newBst,60)
insertNode(newBst,50)
insertNode(newBst,90)
insertNode(newBst,30)
insertNode(newBst,60)
insertNode(newBst,20)

#print(newBst.data)
#print(newBst.leftchild.data)
preOrderTraversal(newBst)                
InOrderTraversal(newBst)
postOrderTraversal(newBst)
levelOrderTraversal(newBst)
