
N=int(input())
res=0
fin=1
while True:
    fin+=6*res
    res+=1
    if fin>=N: break
print(res)