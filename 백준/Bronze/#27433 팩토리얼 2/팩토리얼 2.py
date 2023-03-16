n = int(input())
ans = 1
num = 0
while num!=n:
    ans *= n-num
    num += 1
print(ans)
