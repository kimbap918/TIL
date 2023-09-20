X = int(input())
N = int(input())
goods = []

for _ in range(N):
    a, b = map(int, input().split())
    goods.append(a*b)

if sum(goods) != X:
    print("No")
else:
    print("Yes")
