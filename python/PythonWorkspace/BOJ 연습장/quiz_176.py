# 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
# 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
n = int(input()) # 10
dp = [0] * (n+1) # [0] * 11

# 0, 1 은 연산 횟수가 없다.
for i in range(2, n+1): # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    dp[i] = dp[i-1]+1 # 2와 3으로 나누어 떨어지지 않으면 1을 무조건 빼야한다.
                    # 그러므로 연산횟수 1회가 증가한다.

    # dp[2] = min(dp[2]=1, dp[1]=1)
    # dp[4] = min(dp[4]=2, dp[2]+1=2)
    if i % 2 == 0: # 2, 4, 6, 8, 10 숫자의 연산 
        dp[i] = min(dp[i], dp[i//2]+1) # dp[4] = dp[4](0), dp[2] = 0 + 1
                                        # dp[6] = dp[6](0), dp[3] = 0
    if i % 3 == 0: # 3, 6, 9, 
        dp[i] = min(dp[i], dp[i//3]+1) # dp[3] = dp[3](0), dp[1]+1(1)
    
# 2, 3, 4, 6, 8, 9, 10 
# 5, 7 = 1
print(dp)

print(dp[n])