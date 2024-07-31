import sys
while True:
    try:
        tmp=list(map(int,sys.stdin.readline().split()))
        ans=[]
        ans.append(tmp[1])
        for i in range(2,len(tmp)):
            if ans[-1]!=tmp[i] :ans.append(tmp[i])
        for i in range(len(ans)):
            print(ans[i],end=' ')
        print("$")
    except: exit()
