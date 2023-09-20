# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from pprint import pprint 
from collections import deque
input = sys.stdin.readline

N = int(input())
cafe = [[0 for _ in range(3)] for _ in range(N)]
dx = [0, 0, 1, -1] 
dy = [1, -1, 0, 0]
cnt = 0 

def BFS(i, j):
    global cnt
    Q = deque([i, j])
    while Q:
        a, b = Q.popleft()
        for k in range(4):
            x = b + dx[k]
            y = a + dy[k]
            if 0 <= x < 3 and 0 <= y < N:
                Q.append([y, x])
                cnt += 1

for i in range(N):
    for j in range(3):
        if cafe[i][j] == 0:
            cafe[i][j] = 1
            BFS(i, j)

pprint(cafe)