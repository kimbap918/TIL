N, K = map(int, input().split())

bmp = [input().split() for _ in range(N)]

for row in bmp:
    temp = []

    for col in row:
        temp += list(col * K)
    
    for _ in range(K):
        print(*temp)