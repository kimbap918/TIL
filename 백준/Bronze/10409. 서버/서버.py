n, T = map(int, input().split())
li = list(map(int, input().split()))
for i in range(n):
    if sum(li[:i+1]) > T:
        print(i)
        break
    elif i == n-1:
        print(n)