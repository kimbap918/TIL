import sys

T=int(input())
N=[0]*T
maxN=0
for i in range(T):
    _=int(sys.stdin.readline())
    N[i]=_

    if maxN<_:
        maxN=_

prime=[True]*(maxN+1)
prime[1]=False


for i in range(2,int(maxN**0.5)+1):
    if prime[i]:
        for j in range(i+i,maxN+1,i):
            prime[j]=False
    print(prime)



for i in N:
    print(i)
    ck=0
    for j in range(2,i//2+1):
        if prime[j] and prime[i-j]:
            ck+=1

    # print(ck)