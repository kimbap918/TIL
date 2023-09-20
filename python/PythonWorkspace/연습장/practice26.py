N = int(input())
stones = list(map(int, input().split()))

dp = [0] * N  # 돌을 밟을 때마다 묻게 되는 독의 양의 최소값을 저장하는 dp 배열

# 초기값 설정
dp[0] = stones[0]  # 첫 번째 돌은 그대로 묻힘

for i in range(1, N):
    # 현재 돌을 밟을 때의 독의 양은 이전 돌을 밟았을 때와 현재 돌에 묻은 독의 양의 합 중 최소값을 선택
    dp[i] = min(dp[i-1], stones[i])

    # 최대 세 칸까지 건너뛸 수 있으므로 이전 돌들 중 최소값을 찾아서 더해줌
    if i >= 3:
        dp[i] += min(dp[i-3:i])

print(dp[-1])  # 마지막 돌까지 건너뛰었을 때의 묻게 되는 독의 양 출력
print(dp)