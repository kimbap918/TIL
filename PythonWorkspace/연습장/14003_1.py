import sys
input = sys.stdin.readline

def binary_search(start, end, arr_num):
    while start < end:
        mid = (start+end) // 2
        if lis[mid] < arr_num:
            start = mid + 1
        else:
            end = mid
    return end

N = int(input()) # 삽입할 숫자의 개수
A = list(map(int, input().split())) # 숫자의 리스트
lis = [A[0], ] # 증가하는 부분 수열의 개수를 담을 리스트
idx_val = [[0,0] for _ in range(N)] # 증가하는 부분 수와 인덱스를 담는 리스트
idx_val[0][1] = A[0] # 각 원소 2번째칸에 A[0] 저장

for i in range(1, N):
    idx_val[i][1] = A[i] # 순회하는 원소의 2번째 칸에 증가하는 부분 수 저장
    # A[i]가 lis의 마지막보다 클 경우
    if lis[-1] < A[i]: # lis의 마지막과 A[i]원소 비교
        idx_val[i][0] = len(lis) # 길이 저장
        lis.append(A[i]) # A[i] lis에 저장
    else: # A[i]가 lis의 마지막보다 작을 경우
        idx = binary_search(0, len(lis)-1, A[i])
        idx_val[i][0] = idx
        lis[idx] = A[i]

idx = len(lis)-1
res = []
for i in range(N-1, -1, -1):
    if idx == -1:
        break
    if idx == idx_val[i][0]:
        res.append(idx_val[i][1])
        idx -= 1

print(len(res))
print(*res[::-1])
