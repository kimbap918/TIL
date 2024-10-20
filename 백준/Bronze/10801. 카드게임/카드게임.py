s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
a,b = 0,0
for i in range(10):
    if s1[i] > s2[i]:
        a+=1
    elif s1[i] < s2[i]:
        b+=1
print('A' if a>b else 'B' if a<b else 'D')