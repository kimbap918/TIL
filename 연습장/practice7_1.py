# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
arr1 = [0 for _ in range(N)]
visited = [0 for _ in range(N)]
ans = 1e18

# arr리스트에서 숫자 카드를 재배치하여 만들 수 있는 수를 계산하는 함수
def calculate(arr):
    # arr의 첫번째 원소로 초기화
    res = arr[0]

    # arr의 두번째 원소부터 마지막 원소까지
    for i in range(1, N):
        # 이전에 선택한 카드와 현재 카드가 합쳐질수 있는지 검사
        if res % 10 == arr[i] // 10:
            res = res * 10 + arr[i] % 10
        # 합쳐질 수 없는 경우
        else:
            # 77, 42?
            # 7700 + 42 = 7742
            res = res * 100 + arr[i]
    return res

# A리스트에서 가능한 모든 순열을 구하는 함수
def permutation(A, arr, N):
    global ans
    # A의 길이와 카드의 개수가 같아지면
    if len(A) == N:
        # ans와 arr을 calculate 함수에서 반환된 값 중에서 작은것 저장
        ans = min(ans, calculate(arr))
        return
    # 0부터 A길이까지 
    for i in range(0, len(A)):
        # 방문한 숫자 카드 체크
        # visited 리스트에서 i번째 인덱스를 체크해서
        # 방문한적이 있으면(visited[i] = 1) 다음 반복문을 실행
        if visited[i]:
            continue
        visited[i] = 1
        arr[N] = A[i]
        permutation(A, arr, N+1)
        visited[i] = 0

permutation(A, arr1, 0)
print(ans)


from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 1e18
for order in permutations(A, N):
    cur = order[0]
    for i in range(1, N):
        if cur % 10 == order[i] // 10:
            cur = cur * 10 + order[i] % 10
        else:
            cur = cur * 100 + order[i]
    ans = min(ans, cur)

print(ans)