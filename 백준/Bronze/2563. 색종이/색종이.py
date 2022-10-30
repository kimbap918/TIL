N = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]
cnt = 0
for i in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

for i in paper:
    cnt += i.count(1)
print(cnt)