# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def DFS(node, height, parent):
#     # DFS(1, [0,0,0,0,0,0,0], [-1,1,1,2,2,3,3])
#     if parent == -1: # parent가 -1이면 0 반환 
#         return 0
    
#     if height[node-1] != 0: # height[0] != 0
#         return height[node-1]
    
#     # height[0] = DFS(-1, )
#     height[node-1] = DFS(i, height, parent)
#     return height[node-1]

# N = int(input())
# height = [0] * (N+1)

# for i in range(1, N+1): # 1, 2, 3, 4, 5, 6, 7
#     parent = int(input())
#     print(DFS(i, height, parent))
#     # DFS(1, [0,0,0,0,0,0,0], [-1,1,1,2,2,3,3])

# print(parent)
# print(height)
from collections import defaultdict

def calculate_heights(node, parent, heights):
    if parent[node] == -1:  # 루트 노드인 경우 높이 0
        heights[node] = 0
    else:
        # 부모 노드의 높이에 1을 더한 값이 현재 노드의 높이
        heights[node] = heights[parent[node]] + 1

    # 현재 노드의 자식 노드들에 대해 재귀적으로 높이 계산
    for child in graph[node]:
        calculate_heights(child, parent, heights)

n = int(input())
parent = []
graph = defaultdict(list)

# 입력 받기
for _ in range(n):
    p = int(input())
    parent.append(p)
    graph[p].append(_)

# 높이 계산을 위한 배열 초기화
heights = [0] * n

# DFS를 통해 높이 계산
root = parent.index(-1)  # 루트 노드 인덱스 찾기
calculate_heights(root, parent, heights)

# 자식이 없는 노드에 대해 높이 0으로 설정
for i in range(n):
    if len(graph[i]) == 0:
        heights[i] = 0

# 노드별 높이 출력
for height in heights:
    print(height)

