import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 주어지는 배열의 크기
# M개의 정수로 배열이 주어질 리스트
N_list = [list(map(int, input().split())) for _ in range(N)]

K = int(input()) # 합을 구할 부분의 개수
for _ in range(K):
    # i행 j열 위치, x, y위치 
    i, j, x, y = map(int, input().split())
    cnt = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            cnt += N_list[a][b]
    print(cnt)

