#isme first row col se last [row][col]tk jana hai with given value me 
def NumberOfpath(twoDarray,row,col,cost):
    if cost<0:
        return 0
    elif row==0 and col==0:
        if twoDarray[0][0]-cost ==0:
            return 1
        else:
            return 0
    elif row==0:
        return NumberOfpath(twoDarray,0,col-1,cost-twoDarray[row][col])

    elif col==0:
        return NumberOfpath(twoDarray,row-1,0,cost-twoDarray[row][col])

    else:
        op1 =NumberOfpath(twoDarray,row-1,col,cost-twoDarray[row][col])
        op2 =NumberOfpath(twoDarray,row,col-1,cost-twoDarray[row][col])
        return op1+op2
list =[[4,7,1,6],
       [5,7,3,9],
       [3,2,1,2],
       [7,1,6,3]]
print(NumberOfpath(list,3,3,25))