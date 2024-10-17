import sys
for i in range(int(sys.stdin.readline())):
    startC=100001
    ans=0
    exb = 0
    for j in range(int(sys.stdin.readline())):
        a,b=map(int,sys.stdin.readline().split())
 
        if startC> b/a :
            startC=b/a
            exb=b
        elif startC== b/a:
            if exb>b: exb=b
    print(exb)
