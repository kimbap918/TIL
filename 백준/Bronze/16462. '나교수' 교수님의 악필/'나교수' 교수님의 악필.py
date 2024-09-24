import math
cnt=0
n=int(input())
for _ in range(n):
    tmp=input()
    if tmp=='100' : cnt+=100
    else:
        tmpnew = ''
        for i in range(len(tmp)):
 
            if tmp[i] == '6' : tmpnew+='9'
            elif tmp[i] == '0' : tmpnew+='9'
            else: tmpnew+=tmp[i]
        cnt+=int(tmpnew)
ans=cnt/n
if ans- int(ans) >=0.5 : print(math.ceil(ans))
else: print(math.floor(ans))