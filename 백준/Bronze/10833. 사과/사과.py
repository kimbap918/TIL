res = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    res += b%a
print(res)