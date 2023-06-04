#when we want to  take input for a fixed length
n =int(input("enter the length of the list\n"))
lst =list(map(int,input("\n enter the number \n").strip().split()))[:n]
lst.sort()
print(lst)

# list  =[]
# lst =[int (i) for i in input("enter the item\n").split()]
# lst.sort()
# l =lst[-1]
# print(lst)
# print(l)