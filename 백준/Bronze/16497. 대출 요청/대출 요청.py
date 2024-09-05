tmp=[0]*32
for _ in range(int(input())):
    a,b=map(int,input().split())
    for i in range(a,b):
        tmp[i]+=1
if max(tmp)> int(input()): print(0)
else: print(1)
