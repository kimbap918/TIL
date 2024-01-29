import sys
input = sys.stdin.readline

for _ in range(int(input())):
    mymax=0
    for i in range(int(input())):
        tmp=list(map(int, input().split()))
        if max(tmp)>=0: mymax+=max(tmp)
    print(mymax)