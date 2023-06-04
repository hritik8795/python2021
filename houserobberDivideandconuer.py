#robbers problem me n number of houuses honge jisme robbery ,1,3,5,7,9... me ya2,4,6,8.....me honi hai
#  agar do adjacent me chori ho gai to alarm bajega .
# par hume maximum amount ko chori karna hai 
#-------------------------------------------------------------   
def houseRobber(houses,currentIndex):
    if currentIndex>=len(houses):
        return 0
    else:
        stealFirstHouse =houses[currentIndex]+houseRobber(houses,currentIndex+2)
        skipFristHouse =houseRobber(houses,currentIndex+1)
        return max(stealFirstHouse,skipFristHouse)
houses =[6,7,1,30,8,2,4]
print(houseRobber(houses,0))