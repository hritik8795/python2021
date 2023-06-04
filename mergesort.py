def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l+i]
    
    for j in range(0, n2):
        R[j] = customList[m+1+j]
    
    i = 0 
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

def mergeSort(customList, l, r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)
    return customList

#cList =[10,23,22,14,54,9,11,33,222]
#print(mergeSort(cList,0,8))

def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low,high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i+1)
def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi-1)
        quickSort(customList, pi+1, high)


cList =[2,1,4,3,5,77,88,54,3]
quickSort(cList,0,8)
print(cList)

def heapify(customList,n,i):
    smallest =i
    l =2 * i + 1
    r =2 * i + 2

    if l<n and customList[l]<customList[smallest]:
        smallest =l
    if r<n and customList[r]<customList[smallest]:
        smallest =r
    if smallest != i:
        customList[i],customList[smallest] =customList[smallest],customList[i]
        heapify(customList,n,smallest)
def heapSort(customList):
    n =len(customList)
    for i in range(int(n/2)-1,-1,-1):
        heapify(customList,n,i)
    for i in range(n-1,0,-1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    customList.reverse()
hList =[2,3,8,6,5,4]
heapSort(hList)
print(hList)

