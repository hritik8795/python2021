#yahhan par n = number diya hoga jise hu number of way batan ahhai ex-n=4, {4},{1,3},{3,1},{1,1,1,1}
def numofway(n):
    if n in (0,1,2):
        return 1
    elif n==3:
        return 2
    else:
        subP1 =numofway(n-1)
        subP2 =numofway(n-3)
        subP3 =numofway(n-4)
        return subP1+subP2+subP3
print(numofway(8))