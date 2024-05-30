N = int(input())
li = list(map(int, input().split()))
res = 0
for n in li:
    res += 2 if n == 0 else 1/n
print(res)