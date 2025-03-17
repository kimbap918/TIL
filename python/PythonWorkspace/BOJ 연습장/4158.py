import sys

input = sys.stdin.readline



while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    sang = set(int(input().strip()) for _ in range(N))
    sun = set(int(input().strip()) for _ in range(M))


cnt = len(sang & sun)
print(cnt)

입력은 여러 개의 테스트 케이스로 이루어져 있기 때문에 입력 0 0 이 주어질때까지 입력을 계속 받아야 합니다.

