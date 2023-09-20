import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = []

def binary_search(arr):
    # N만큼 반복
    for i in range(N):
        # 시작지점, 끝지점 지정
        start, end = 0, len(dp)-1
        while start <= end:
            mid = (start+end) // 2
            if dp[mid] < arr[i]:
                start = mid + 1
            else:
                end = mid - 1
        # dp 의 길이보다 시작점이 길면
        if start >= len(dp):
            # A[i] 추가
            dp.append(arr[i])
            print(dp)
        else:
            # dp[0] = A[0]
            dp[start] = arr[i]

    return len(dp)

print(binary_search(A))


# n = int(input()) # 6
# a = list(map(int, input().split())) # 10 20 10 30 20 50
# dp = [0 for i in range(n)] # [0, 0, 0, 0, 0, 0]
# for i in range(n): # 6
#     for j in range(i):
#         print(i, j)
#         if a[i] > a[j] and dp[i] < dp[j]: 
#             dp[i] = dp[j] # 최댓값 저장
#     dp[i] += 1 # 1씩 누적
# print(max(dp))


