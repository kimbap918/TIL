s=list(input())
for _ in range(int(input())):
    a,b=map(int, input().split())
    tmp=s[a]
    s[a]=s[b]
    s[b]=tmp
for i in range(len(s)):
    print(s[i],end='')