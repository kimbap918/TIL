N = int(input())
MOD = 1000000000 # 정답에서 10억을 나눈 값 출력

# 0부터 9까지, N+1(숫자의 자리 수) 만큼 생성
dp = [[0] * 10 for i in range(N+1)]

# 1자리 수 일때 N = 1
# 1자리 수는 0을 제외한 1~9까지 모두 1의 차이를 가짐
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0: # 앞에 오는 숫자가 0이라면
            # 0은 계단수가 될수 없다 
            dp[i][j] = dp[i-1][1] # j 가 0이므로 
        elif j == 9: # j가 마지막 수라면
            # 마지막 수의 뒤에는 8밖에 존재하지 않는다.
            dp[i][j] = dp[i-1][8]
        else: # 1~8까지의 수 
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] # j의 앞 뒤수가 계단수가 될수있다.

print(sum(dp[N]) % MOD)