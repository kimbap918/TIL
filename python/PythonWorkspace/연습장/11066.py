
# N = int(input())
# for _ in range(N):
#     K = int(input())
#     files = [0] + list(map(int, input().split()))
#     sum_num = [0 for _ in range(N+1)]
#     for i in range(1, N+1):
#         # sum_num[i]는 1번부터 i번까지 누적합
#         sum_num[i] = sum_num[i-1] + files[i]

#     # DP[i][k] + DP[k+1][j] + sum(A[i]~A[j])
#     dp = [[0 for i in range(N+1)] for _ in range(N+1)]
#     for i in range(2, N+1):
#         for j in range(1, N+2-i):
#                 dp[j][j+i-1] = min([dp[k][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (sum_num[j+1-1] - sum_num[j-1])

#     print(dp[1][N])


# 1. 파일을 합치는 횟수는 K-1로 모든 조건에서 동일하다
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    table = [[0] * K for _ in range(K)]

#   table[i][j] = table[i][j-1] + files[j] + min(minimum)
    for i in range(K-1):
        # 합의 비용을 계산한다. 
        # 40 30 30 50일때,
        table[i][i+1] = files[i] + files[i+1] # 40+30 = 70, 30+30 = 60, 30+50 = 80
        # print(table)
        # K개의 행까지
        for j in range(i+2, K): # 2, 3, 3
            # table[0][2] [0][3], [1][3] = table[0][1]+file[2], table[0][2] =[0][2]+[3], [1][2]+[3]
            # 첫번째 합의 비용(70)에서 남은 비용(30, 50)을 더해서 기록 
            table[i][j] = table[i][j-1] + files[j] # 70+30 = 100, 100+50 = 150, 60+50 = 110 
            # print("files : "+str(files[j]))
            # print("table[i][j-1] : "+str(table[i][j-1]))
            # print(table)
    for d in range(2, K): # 2, 3
        for i in range(K-d): # 4-2 = 2, 4-3, 1
            j = i+d
            # print(table)
            # print(i, j) # i=0, j=3
            # ((i~k까지 더한 비용의 최솟값) + (k+1~j까지 더한 비용의 최솟값))
            # 0 0 1 3 = 170, 0 1 2 3 = 150, 0 2 3 3 = 300
            # min = 150
            minimum = [table[i][k] + table[k+1][j] for k in range(i, j)] # 0 1 2
            # 150 + 150
            table[i][j] += min(minimum)
            # print(table)

    print(table[0][K-1])
