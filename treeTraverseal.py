import QueueLinkedList as queue
class treeNode:
    def __init__(self,data):
        self.data =data
        self.leftchild =None
        self.rightchild =None

newBt =treeNode("drinks")
leftchild=treeNode("hot")
tea =treeNode("tea")    
coffee =treeNode("coffee")
leftchild.leftchild =tea
leftchild.rightchild =coffee
rightchild=treeNode("cold")
cola =treeNode("cola")
fanta =treeNode("fanta")
rightchild.leftchild=cola
rightchild.rightchild=fanta
newBt.leftchild =leftchild
newBt.rightchild=rightchild

def preorderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraversal(rootNode.leftchild)
    preorderTraversal(rootNode.rightchild)
    
#preorderTraversal(newBt)
print("-----------preorder traversal------------------------")
def inorderTraversal(rootNode):
    if not rootNode:
        return
    inorderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightchild)
#inorderTraversal(newBt)
print("-----------------inorder traversal------------------")
def postTraversal(rootNode):
    if not rootNode:
        return
    postTraversal(rootNode.leftchild)
    postTraversal(rootNode.rightchild)
    print(rootNode.data)

#postTraversal(newBt)

#level order traversal

def levelOrderTraversal(rootNode):
    if  not rootNode:
        return "there is not exist any binary tree"
    else:
        customQueue =queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root =customQueue.dequeue()
            print(root.value.data)
            if(root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)
print(levelOrderTraversal(newBt))

print("---------------------level order------------------------")

#finding the node in the tree 

def searchBt(rootNode,nodevalue):
    if not rootNode:
        return "the bt does not exist"
    else:
        customQueue =queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root =customQueue.dequeue()
            if root.value.data ==nodevalue:
                return "success"
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
            if(root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)
        return "not found"
print(searchBt(newBt,"coffe"))

def insertBt(rootNode,newNode):
    if not rootNode:
        rootNode =newNode
    else:
        customQueue =queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root =customQueue.dequeue()
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.rightchild)
            else:
                root.value.leftchild =newNode
                return "successfully inserted"
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)
            else:
                root.value.rightchild = newNode
                return "successfully inserted"

newNode =treeNode("cappiccino")
print(insertBt(newBt,newNode))
levelOrderTraversal(newBt)


#delete a node from binary tree
#step 1-get  the deepest node
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
            
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)
        deepestNode = root.value
        return deepestNode
#deepestNode =getDeepestNode(newBt)
#print(deepestNode.data)

#step-2 delete karna hai deepest node ko 
def deleteDeepestNOde(rootNode,dNode):
    if not rootNode:
        return
    else:
        customQueue =queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root =customQueue.dequeue()
            if root.value.rightchild:
                if root.value.rightchild is dNode:
                    root.value.rightchild =None
                else:
                    customQueue.enqueue(root.value.rightchild)
            if root.value.leftchild:
                if root.value.leftchild is dNode:
                    root.value.leftchild =None
                else:
                    customQueue.enqueue(root.value.leftchild)
#newNode =getDeepestNode(newBt)
#deleteDeepestNOde(newBt,newNode)
#levelOrderTraversal(newBt)

print("------------------following are deleting the node----------")

#ab delete node binary tree
def deleteNodeBT(rootNode,Node):
    if not rootNode:
        return
    else:
        customQueue =queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root =customQueue.dequeue()
            if root.value.data ==Node:
                dNode =getDeepestNode(rootNode)
                root.value.data =dNode.data
                deleteDeepestNOde(rootNode,dNode)
                return "the node has been success fully deleted"
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)
        return "fail to delete"
deleteNodeBT(newBt,'tea')
levelOrderTraversal(newBt)

print("--------------folowing are deleted entire Node------------")

#delete the entire node
def deleteBt(rootNode):
    rootNode.data =None
    rootNode.leftchild =None
    rootNode.rightchild =None
    return "the bt has been success fully deleted"
deleteBt(newBt)
levelOrderTraversal(newBt)