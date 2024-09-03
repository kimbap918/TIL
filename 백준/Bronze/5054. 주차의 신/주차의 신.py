t = int(input())

for _ in range(t):
    n = int(input())
    store = sorted(map(int, input().split()))
    print((store[-1] - store[0]) * 2)
