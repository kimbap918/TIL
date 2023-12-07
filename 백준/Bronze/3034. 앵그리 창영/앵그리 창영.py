N, W, H = map(int, input().split())
d = (W**2 + H**2)**0.5
for _ in range(N):
    n = int(input())
    print("DA" if n <= d else "NE")