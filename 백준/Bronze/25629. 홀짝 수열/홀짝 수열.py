import math
N=int(input())
List=list(map(int,input().split()))
a=0
b=0
for i in range(len(List)):
    if(List[i]%2!=0):
        a+=1
    else:
        b+=1
if(a==math.ceil(N/2) and b==N//2):
    print(1)
else:
    print(0)
