class BinaryTree:
    def __init__(self,size):
        self.customList =size*[None]
        self.lastUsedIndex =0
        self.maxsize =0
    def insertNode(self,value):
        if self.lastUsedIndex +1 ==self.maxsize:
            return "the binary tree is full"
        self.customList[self.lastUsedIndex +1] =value
        self.lastUsedIndex +=1
        return "the value has been successfully inserted"
    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] ==nodeValue:
                return "success"
        return "not found"
    def preOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 +1)
     

    def postOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 +1)
        print(self.customList[index])
    
    def inOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.inOrderTraversal(index *2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 +1)
  
    def levelOrderTraversal(self,index):
        for i in range(index,self.lastUsedIndex +1):
            print(self.customList[i])
        
    def deleteNodeBt(self,value):
        if self.lastUsedIndex ==0:
            return "there is not any node to delete"
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i] ==value:
                self.customList[i] =self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]=None
                self.lastUsedIndex -=1
                return "the node has been successfully deleted"

    def deleteBt(self):
        self.customList =None
        return "the bt is successfully deleted"        



newBt =BinaryTree(8)
print(newBt.insertNode("Drinks"))
print(newBt.insertNode("hot"))
print(newBt.insertNode("cold"))
print(newBt.searchNode("hot"))
newBt.preOrderTraversal(1)
newBt.postOrderTraversal(1)
newBt.inOrderTraversal(1)
newBt.levelOrderTraversal(1)
print(newBt.deleteNodeBt("cold"))
print(newBt.deleteBt())