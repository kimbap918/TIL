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
        else:
            # dp[0] = A[0]
            dp[start] = arr[i]
    # print(dp)
    return len(dp)

print(binary_search(A))