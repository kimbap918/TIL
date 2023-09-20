N = int(input())
wine = [0]
for i in range(N):
    wine.append(int(input())) # [0, 6, 10, 13, 9, 8, 1]
dp = [0]
dp.append(wine[1]) # [0, 6]
if N > 1: # 와인잔이 2개 이상일 경우
    dp.append(wine[1] + wine[2]) # dp에 와인의 양 1, 2번 인덱스 값을 추가
for i in range(3, N+1): # 3부터 N+1까지
    dp.append(max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i]))
print(dp[N])