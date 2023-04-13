import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = [0]

def binary_search(arr):
    for i in range(N):
        start, end = 0, len(dp)-1
        while start <= end:
            mid = (start+end) // 2
            if dp[mid] < A[i]:
                start = mid + 1
            else:
                end = mid - 1
        if start >= len(dp):
            dp.append(A[i])
        else:
            dp[start] = A[i]
    # print(dp)
    return len(dp)-1

print(binary_search(A))
