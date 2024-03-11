N,T = map(int,input().split())
cnt = 0
x = 1
for i in range(T):
    cnt +=x
    if(cnt==2*N):
        x = -1
    if(cnt==1):
        x = 1
print(cnt)
