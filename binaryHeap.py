#creation
class Heap:
    def __init__(self,size):
        self.customList =(size+1)*[None]
        self.heapsize =0
        self.maxsize =size+1
    
    def peekOfHeap(rootNode):
        if not rootNode:
            return
        else:
            return rootNode.customList[1]
    
def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapsize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapsize+1):
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode,index,heapType):
    parentIndex =int(index/2)
    if index<=1:
        return
    if heapType =="min":
        if rootNode.customList[index]<rootNode.costumList[parentIndex]:
            temp =rootNode.customList[index]
            rootNode.customList[parentIndex]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
            heapifyTreeInsert(rootNode,parentIndex,heapType)
        elif heaptype =="max":
            if rootNode.customList[index]>rootNode.customList[parentIndex]:
                temp =rootNode.customList[index]
                rootNode.customList[index] =rootNode.customList[parentIndex]
                rootNode.customList[parentIndex]=temp
            heapifyTreeInsert(rootNode,parentIndex,heapType)
def inserNode(rootNode,nodeValue,heapType):
    if rootNode.heapsize+1 ==rootNode.maxsize:
        return"the binary heap is full"
    rootNode.customList[rootNode.heapsize+1]=nodeValue
    rootNode.heapsize +=1
    heapifyTreeInsert(rootNode,rootNode.heapsize,heapType)

    return "the value has been successfully inserted"

def heapifyTreeExtract(rootNode,index,heapType):
    leftIndex =index*2
    rightChild =index*2+1
    swapChild =0
    if rootNode.heapsize<leftIndex:
        return
    elif rootNode.heapsize==leftIndex:
        if heapType =="min":
            if rootNode.customList[index]>rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] =temp
                return
            else:
                if rootNode.customList[index]<rootNode.customList[leftIndex]:
                    temp= rootNode.customList[index]
                    rootNode.customList[index]=rootNode.customList[leftIndex]
                    rootNode.customList[leftIndex]=temp
                    return
                else:
                    if heapType =="min":
                        if rootNode.customList[leftIndex]<rootNode.customList[rightIndex]:
                            swapChild =leftIndex
                        else:
                            swapChild =rightIndex
                            if rootNode.customList[index]<rootNode.customList[swapChild]:
                                temp =rootNode.customList[index]
                            rootNode.customList[index] =rootNode.customList[swapChild]
                            rootNode.customList[swapChild]=temp
                        heapifyTreeExtract(rootNode,swapChild,heapType)

def extractNode(rootNode,heapType):
    if rootNode.heapsize ==0:
        return
    else:
        extractNode =rootNode.customList[1]
        rootNode.customList[1] =rootNode.customList[rootNode.heapsize]
        rootNode.customList[rootNode.heapsize]  =None
        rootNode.heapsize -=1
        heapifyTreeExtract(rootNode,1,heapType)
        return extractNode        
def deleteEntireBp(rootNode):
    rootNode.customList=None



newBinaryHeap =Heap(5)
print(sizeOfHeap(newBinaryHeap))
inserNode(newBinaryHeap,4,"max")
inserNode(newBinaryHeap,5,"max")
inserNode(newBinaryHeap,2,"max")
inserNode(newBinaryHeap,1,"max")
print(extractNode(newBinaryHeap,"max"))
print(deleteEntireBp(newBinaryHeap))
levelOrderTraversal(newBinaryHeap)
