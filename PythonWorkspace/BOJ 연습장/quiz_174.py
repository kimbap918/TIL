n = int(input())
dp = []

for i in range(n) :                            ## 입력값 이차원리스트 형태로 dp테이블에 저장하기
    dp.append(list(map(int,input().split())))

for i in range(1,n) :                           ## 행을 기준으로 for문 구성
    for j in range(0,i+1) :                     ## 열을 기준으로 for문 구성
        if j == 0 :
            dp[i][0] += dp[i-1][0]              # 0열끼리 더하기
        elif j == i :
            dp[i][j] += dp[i-1][j-1]            # 마지막 열끼리 더하기
        else :
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])    # 두 화살표중 더 큰 경우 받아들이기

print(max(dp[n-1]))                 # n-1행에서의 최댓값 출력