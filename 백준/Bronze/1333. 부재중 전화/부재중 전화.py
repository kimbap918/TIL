n,l,d=map(int,input().split())
l+=5
num=0
time=d
for i in range(n):
    num+=l
    while True:
        if time<num-5: time+=d
        else: break
    if num-5<=time<num: break
print(time)