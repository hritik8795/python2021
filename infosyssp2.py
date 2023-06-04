from itertools import combinations
def fun(arr,N):
    s=[]
    max_xor =max(arr)
    for i in range(1,N//2):
        comb =combinations(arr,i+1)
        for i in comb:
            s.append(list(i))

        for a in s:
            z=0
            for b in a:
                z =z^b

            if z>max_xor:
                max_xor =z
        return max_xor

N =int(input("enter the num"))
arr =[]
for i in range(N):
    arr.append(int(input(f"enter list elemet")))

if N<3:
    print("output"max(arr,N))
else:
    print("output",fun(arr,N))


