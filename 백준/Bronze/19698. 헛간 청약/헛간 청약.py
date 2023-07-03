N, W, H, L = map(int, input().split())
print(min((W//L)*(H//L), N))