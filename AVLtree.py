import QueueLinkedList as Queue
class AvlNode:
    def __init__(self,data):
        self.data =data
        self.leftChild =None
        self.rightChild =None
        self.height =1
    
    def preOrderTraversal(rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

    def inOrderTraversal(rootNode):
        if not rootNode:
            return
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightChild)

    def preOrderTraversal(rootNode):
        if not rootNode:
            return
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

    def levelOrderTraversal(rootNode):
        if not rootNode:
            return
        customQueue =queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root =customQueue.dequeue()
            print(root.value.data)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.rightChild)
        
    def searchNode(rootNode,nodeValue):
        if rootNode.data ==nodeValue:
            print("the value is found")
        elif nodeValue< rootNode.data:
            if rootNode.leftChild.data ==nodeValue:
                print("the value is found")
            else:
                searchNode(rootNode.leftChild,nodeValue)
        else:
            if rootNode.rightChild.data ==nodeValue:
                print("the value is found")
            else:
                searchNode(rootNode.rightChild,nodeValue)
    
    def getHieght(rootNode):
        if not rootNode:
            return 0
        return rootNode.height
    
    def rightRotate(disbalancedNode):
        newRoot =disbalancedNode.leftChild
        disbalancedNode.leftChild =disbalancedNode.leftChild.rightChild
        newRoot.righchild =disbalancedNode

        disbalancedNode.height =1 +max(getHieght(disbalancedNode.leftChild),getheight(disbalancedNode.rightChild))
        newroot.height =1+ max(getHieght(newRoot.leftChild),getHieght(newRoot.rightChild))
        return newRoot
    
    def leftRotate(disbalancedNode):
        newRoot =disbalancedNode.rightChild
        disbalancedNode.rightChild =disbalancedNode.rightChild.leftChild
        newRoot.leftChild = disbalancedNode
        disbalancedNode.height =1+max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
        newNode.height =1 +max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
        return newRoot
    
    def getbalance(rootNode):
        if not rootNode:
            return 0
        return getHeight(rootNode.leftChild)-getHeight(rootNode.rightChild)
    
    def insertNode(rootNode,nodeValue):
        if not rootNode:
            return AvlNode(nodeValue)
        elif nodeValue < rootNode.data:
            rootNode.leftChild =insertNode(rootNode.leftChild,nodeValue)
        
        else:
            rootNode.rightChild =insertNode(rootNode.rightChild,nodeValue)
            
        rootNode.height =1+ max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
        balance =getbalance(rootNode)

        if balance > 1 and nodeValue < rootNode.leftChild.data:
            return rightRotate(rootNode)
        if balance > 1 and nodeValue > rootNode.leftChild.data:
            rootNode.leftChild =leftRotate(rootNode.leftChild)
            return rightRotate(rootNode)
        if balance < -1 and nodeValue > rootNode.rightChild.data:
            return leftRotate(rootNode)
        if balance < -1 and  nodeValue < rootNode.rightchild.data :
            rootNode.rightChild =rightRotate(rootNode.rightChild)
            return lefttRotate(rootNode)
        return rootNode
    
    def getminValue(rootNode):
        if rootNode is None or rootNode.leftChild is None:
            return rootNode
        return getminValue(rootNode.leftChild)
    def deleteNode(rootNode,nodeValue):
        if not rootNode:
            return rootNode
        elif nodeValue < rootNode.data:
            rootNode.leftChild =deleteNode(rootNode.leftChild,nodeValue)
        elif  nodeValue>rootNode.data:
            rootNode.rightChild =deleteNode(rootNode.rightChild,nodeValue)
        else:
            if rootNode.leftChild is None:
                temp =rootNode.rightChild
                rootNode=None
                return temp
            elif rootNode.rightChild is None:
                temp =rootNode.leftChild
                rootNode =None
                return temp
            temp =getminValue(rootNode,rightChild)
            rootNode.data =temp.data
            rootNode.rightChild =deleteNode(rootNode.rightChild,temp.data)
        balance =getbalance(rootNode)
        if balance>1 and getbalance(rootNode.leftChild)>=0:
            return rightRotate(rootNode)
        if balance<-1 and getbalance(rootNode.rightChild)<=0:
            return lefttRotate(rootNode)
        if balance>1 and getbalance(rotate.leftChild)<0:
            rootNode.leftChild =leftRotate(rootNode.leftChild)
            return rightRotate(rootNode)
        if balance<-1 and getbalance(rootNode.rightChild)>0:
            rootNode.rightChild =rightRotate(rootNode.rightChild)
            return leftRotate(rootNode)
        return rootNode

    

newAvl =AvlNode(5)
newAvl =insertNode(newAvl, 10)
newAvl =insertNode(newAvl, 15)
newAvl =insertNode(newAvl, 20)
levelOrderTraversal(newAvl)