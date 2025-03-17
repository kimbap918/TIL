import sys

def LCS(A, B):
    n, m = len(A), len(B)
    
    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # DP 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS 길이 출력
    print(dp[n][m])

    # LCS 문자열 역추적
    lcs = []
    i, j = n, m
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:  # 같은 문자를 만나면 LCS에 추가
            lcs.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # 위쪽 값이 더 크면 위로 이동
            i -= 1
        else:  # 왼쪽 값이 더 크면 왼쪽으로 이동
            j -= 1

    # LCS 문자열 출력
    print("".join(reversed(lcs)))

# 입력 처리
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
LCS(A, B)
