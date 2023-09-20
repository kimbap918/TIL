import sys
input = sys.stdin.readline

# 이분 탐색 구현
def binary_search(start, end, arr_num):
    while start < end:
        mid = (start+end) // 2
        if lis[mid] < arr_num:
            start = mid + 1
        else:
            end = mid
    return end

N = int(input())
A = list(map(int, input().split()))

lis = [A[0], ] # 10
index_val = [[0, 0] for _ in range(N)] # [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
index_val[0][1] = A[0] # [[0, 10], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

for i in range(1, N):
    index_val[i][1] = A[i]
    if lis[-1] < A[i]: # lis의 마지막 값보다 A[i] 값이 큰 경우
        index_val[i][0] = len(lis) # index_val에 lis의 길이 기록
        lis.append(A[i]) # lis에 큰 A[i] 값 기록
    else: # lis의 마지막 값보다 A[i]값이 작은 경우
        idx = binary_search(0, len(lis)-1, A[i]) # 들어갈 자리 이진 탐색
        index_val[i][0] = idx # 해당 자리의 이진탐색 인덱스 값 기록
        lis[idx] = A[i] # lis의 이진탐색 해당 자리 A[i]로 변경

idx = len(lis)-1
ans = []
for i in range(N-1, -1, -1): # N의 역순
    if idx == -1: 
        break
    if idx == index_val[i][0]: # index_val의 위치기록값이 idx와 같다면
        ans.append(index_val[i][1]) # ans에 추가
        idx -= 1 # 인덱스 1 감소

print(len(ans))
print(*ans[::-1])

