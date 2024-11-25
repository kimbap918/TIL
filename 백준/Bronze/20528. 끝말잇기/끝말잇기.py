N = int(input())
li = input().split()
s = set()
for i in range(N):
    s.add(li[i][0])
print(1 if len(s) == 1 else 0)