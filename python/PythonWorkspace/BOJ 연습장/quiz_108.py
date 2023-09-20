import sys
input = sys.stdin.readline
N, M = map(int, input().split())

N_list = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

for k in range(K):
    sum = 0
    i, j, x, y = map(int, input().split())


    for a in range(i-1, x):
        for b in range(j-1, y):
            sum += N_list[a][b]
    print(sum)