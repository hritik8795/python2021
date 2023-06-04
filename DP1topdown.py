#topdown method
def Fibonacci(n,memo):
    if n ==1:
        return 0
    if n==2:
        return 1
    if not n in memo:
        return Fibonacci(n-1,memo) +Fibonacci(n-2,memo)
    return memo[n]
myDict ={}
print(Fibonacci(6,myDict))
    

#buttomup approcth
def Fibonacci1(n):
    tb =[0,1]
    for i in range(2,n+1):
        tb.append(tb[i-1]+tb[i-2])
    return tb[n-1]
print(Fibonacci1(6))


#number factor
def NumberFactor(n,tempDict):
    if n in (0,1,2):
        return 1
    elif n ==3:
        return 2
    else:
        if n not in tempDict:
            subP1 =NumberFactor(n-1,tempDict)
            subP2 =NumberFactor(n-3,tempDict)
            subP3 =NumberFactor(n-4,tempDict)
            tempDict[n]=subP1+subP2+subP3
        return tempDict[n]

print(NumberFactor(4,{}))

#bottoms up

def numberFactorbu(n):
    tempArr=[1,1,1,2]
    for i in range(4,n+1):
        tempArr.append(tempArr[i-1]+tempArr[i-3]+tempArr[i-4])
    return tempArr[n]
print(numberFactorbu(5))