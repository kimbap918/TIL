def calPerimeter(x1, y1, x2, y2):
    return ((x2 - x1) + (y2 - y1)) * 2


N = int(input())
a, b, c, d = map(int, input().split())
print(calPerimeter(a, b, c, d))

for _ in range(N - 1):
    newA, newB, newC, newD = map(int, input().split())
    a, b = min(a, newA), min(b, newB)
    c, d = max(c, newC), max(d, newD)
    print(calPerimeter(a, b, c, d))
