def linear(arr,value):
    for i in range (len(arr)):
        if arr[i]==value:
            return i
    return -1
array =[10,3,44,21,22,12,9]
value =44
print(linear(array,value))

import math
def binarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    while not(array[middle]==value) and start<=end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1 
        middle = math.floor((start+end)/2)
        # print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1
        



custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))