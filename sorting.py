import math
def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j]>customList[j+1]:
                customList[j],customList[j+1] =customList[j+1],customList[j]
 #   print(customList)

#cList =[1,4,35,6,7,5,9]
#bubbleSort(cList)

def selectionSort(customList):
    for i in range(len(customList)):
        min_index =i
        for j in range(i+1,len(customList)):
            if customList[min_index]>customList[j]:
                min_index =j
                customList[i],customList[min_index] =customList[min_index],customList[i]
 #   print(customList)

#cList =[3,4,55,667,78,95,34,56,66,32]
#selectionSort(cList)

def insertionSort(customList):
    for i in range(1,len(customList)):
        key =customList[i]
        j =i-1
        while j>=0 and key < customList[j]:
            customList[j+1]=customList[j]
            j -= 1
            customList[j+1] =key
    #print(customList)
#cList =[1,4,32,12,15,18]
#insertionSort(cList)


def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].append(j)
    
    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList
#cList =[1,4,33,22,35,28]
#print(bucketSort(cList))


#----------------------------merge sort ---------------------------
#l =frist index,r =last index, m=mid index of list
def merge (customList ,l,m,r):
    n1 =m - l + 1
    n2 =r - m

    L =[0] * (n1)
    R =[0] * (n2)

    for i in range (0, n1):
        L[i] = customList[l+i]
    for j in range (0,n2):
        R[j] = customList[m+1+j]

    i = 0
    j = 0
    k =l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i +=1
        else:
            customList[k] =R[j]
            j +=1
        k +=1
    while i<n1:
        customList[k]= L[i]
        i += 1
        k += 1
    while j < n2:
        customList[k] = R[j]
        j +=1
        k +=1

def mergeSort(customList,l,r):
    if l < r:
        m =(l+(r-1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m+1, r)
        mergeSort(customList, l, m, r)
    return customList


cList =[2,43,1,22,65,25,5,13,19]
print(mergeSort(cList,0,8))

