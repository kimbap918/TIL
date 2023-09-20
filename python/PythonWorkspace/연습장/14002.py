import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0 for i in range(N+1)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

ans1 = max(dp)
res = []
for i in range(N-1, -1, -1):
    if dp[i] == ans1:
        res.append(A[i])
        ans1 -= 1
res.reverse()
print(len(res))
for i in res:
    print(i, end=' ')


# def binary_search(arr):
#     for i in range(N):
#         start, end = 0, len(dp)-1
#         while start <= end:
#             mid = (start+end) // 2
#             if dp[mid] < arr[i]:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         if start >= len(dp):
#             dp.append(arr[i])
#         else:
#             dp[start] = arr[i]
#     return len(dp)

# print(binary_search(A))
# print(*dp)