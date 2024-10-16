import sys
li=[i+1 for i in range(20)]

for i in range(10):
    m, n = map(int, sys.stdin.readline().split())
    a=li[:m-1]
    b=li[m-1:n][::-1]
    c=li[n:]
    li=a+b+c
    
for i in li:
    print(i, end=' ')