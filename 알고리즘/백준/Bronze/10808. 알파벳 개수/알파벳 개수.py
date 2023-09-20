arr=input()
cnt=[0]*26

for i in arr:
    cnt[ord(i)-97]+=1

print(*cnt)