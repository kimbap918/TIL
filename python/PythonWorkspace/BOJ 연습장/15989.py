# 1+1+1+1
# 2+1+1 (1+1+2, 1+2+1)
# 2+2
# 1+3 (3+1)

# 1 = 100%
# %2 == 0: = 100%
# 2+1 = dp[n][k] = k이하 수를 사용해 n을 만드는 조합 수
# 
# 6 -> 2+2+1+1, 2+1+1+1+1

T = int(input())

# a_n​=a_{n−3}​+⌊n/2​⌋+1(n: 자연수,a₁=1,a₂=2,a₃​=3)

def cnt_combination(N):
    res = 0
    for i in range(N//3 + 1):
        tmp = N - (3*i)
        res += (tmp // 2) + 1
    return res

for _ in range(T):
    N = int(input())
    print(cnt_combination(N))


# T = int(input())

# dp = [1 for _ in range(10001)] #dp[i]는 i를 만들 수 있는 경우의 수

# for i in range(2,10001):
#     dp[i] += dp[i-2]
# for i in range(3,10001):
#     dp[i] += dp[i-3]
# for _ in range(T):
#     N = int(input())
#     print(dp[N])