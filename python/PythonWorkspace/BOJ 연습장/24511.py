import sys
from collections import deque

input = sys.stdin.readline

# 입력 처리
n = int(input())  # queuestack 개수
structure_types = list(map(int, input().split()))  # 자료구조 타입 (0: 큐, 1: 스택)
initial_values = deque(map(int, input().split()))  # 초기 B 값
m = int(input())  # 삽입할 원소 개수
insert_values = deque(map(int, input().split()))  # 삽입할 원소 리스트

# 큐(0)인 원소만 저장 (역순으로 저장)
queue_values = deque()
for i in range(n):
    if structure_types[i] == 0:
        queue_values.append(initial_values[i])

# 결과 계산
result = []
for value in insert_values:
    queue_values.appendleft(value)  # 새로운 값 추가
    result.append(str(queue_values.pop()))  # 가장 마지막 값 출력

# 최종 출력 (빠른 출력)
sys.stdout.write(" ".join(result) + "\n")
