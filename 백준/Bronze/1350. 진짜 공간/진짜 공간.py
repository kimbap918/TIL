a= int(input())
arr = list(map(int, input().split()))
b=int(input())
x=0
for i in range(a):
    if arr[i]!=0 and arr[i]<=b:
        x+=1
    elif arr[i]==0:
        continue
    else:
        if arr[i]%b!=0:
            x+=(arr[i]//b)+1
        else:
            x+=(arr[i]//b)
print(b*x)