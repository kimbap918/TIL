# 1. 일단 초기화 
# 2. 입력을 그대로 2d list
from pprint import pprint

# matrix = [list(input()) for _ in range(8)]

# matrix = []

# for _ in range(8):
#     line = list(input())
#     matrix.append(line)

# print(matrix)


#matrix = [list(map(int, input().split())) for _ in range(3)]

# M x 3 리스트 입력받기
# matrix = []
# for _ in range(3):
#     line = list(map(int, input().split()))
#     matrix.append(line)
#pprint(matrix)

# M x N 의 리스트 입력받기 
matrix = []
N, M = map(int, input().split())
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)
pprint(matrix)

# M x N 의 리스트 입력받기 컴프리헨션
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
pprint(matrix)