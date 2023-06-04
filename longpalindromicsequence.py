#yahan par longest palindromic nikalna hai 2 strigng me se sequence does not matter
def longestPalindrom(S,startIndex,endIndex):
    if startIndex>endIndex:
        return 0
    elif startIndex==endIndex:
        return 1

    elif S[startIndex]==S[endIndex]:
        return 2+longestPalindrom(S,startIndex+1,endIndex-1)
    
    else:
        op1 =longestPalindrom(S,startIndex,endIndex-1)
        op2 =longestPalindrom(S,startIndex+1,endIndex)
        return max(op1,op2)
print(longestPalindrom("elrmenmet",0,8))