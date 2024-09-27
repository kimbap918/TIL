import sys
 
def newfactorial(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
        ans%=1000000000000
        while ans%10==0 : ans/=10
    return int (ans%10)
for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    print(newfactorial(n))