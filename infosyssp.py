N = int(input("enter the number of string"))
S = list(input("enter the binary string len n"))
Cash = int(input("how manycash you have"))
A = int(input("amount spend to swap A"))
B = int(input("amount spend to flip B"))
#N = 6
#S = list("111011")
#Cash = 7
#A = 1
#B = 3


def swap():
   global Cash
   Rs = S.copy()
   S[S.index('1')], S[''.join(S).rindex('0')] = S[''.join(S).rindex('0')], S[S.index('1')]
   if Rs == S:
       flip()
   else:
       Cash -= A


def flip():
   global Cash
   S[S.index('1')] = '0'
   Cash -= B


while Cash > A or Cash > B:
   if A < B and '0' in S:
       swap()
   else:
       flip()
print(int(''.join(S), 2))
