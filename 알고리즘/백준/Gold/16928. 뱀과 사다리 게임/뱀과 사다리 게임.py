from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

board = [0] * 101
visited = [False] * 101 
ladders, snakes = dict(), dict()
dice = [1, 2, 3, 4, 5, 6]

# N = 뱀의 수 = 뱀은 밟으면 뱀을따라 내려간다
# M = 사다리의 수 = 사다리는 밟으면 사다리를 타고 올라간다.
N, M = map(int, input().split())

for i in range(N):
    # start, end
    x, y = map(int, input().split())
    # [키] = 값
    ladders[x] = y

for i in range(M):
    # start, end
    u, v = map(int, input().split())
    snakes[u] = v

# 시작지점
Q = deque()
Q.append(1)

def BFS():
    while Q:
        a = Q.popleft()
        # 마지막칸에 도착하면
        if a == 100:
            print(board[a])
            break
        for i in dice:
            next_block = a + i
            if next_block <= 100 and not visited[next_block]:
                if next_block in ladders.keys():
                    next_block = ladders[next_block]
                if next_block in snakes.keys():
                    next_block = snakes[next_block]
                if not visited[next_block]:
                    visited[next_block] = True
                    board[next_block] = board[a] + 1
                    Q.append(next_block)

BFS()