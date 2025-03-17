def potato_sum(C, potato):
    potato.sort(reverse=True)

    def backtrack(index, current_sum):
        if current_sum == C:
            return True
        if current_sum > C or index >= len(potato):
            return False

        if backtrack(index+1, current_sum+potato[index]):
            return True
        if backtrack(index+1, current_sum):
            return True

        return False

    return backtrack(0, 0)

P = int(input())


for i in range(P):
    arr = list(map(int, input().split()))
    K, C, potato = arr[0], arr[1], arr[2:]

    res = "YES" if potato_sum(C, potato) else "NO"
    print(K, res)
    


def subset_sum_dp(capacity, potatoes):
    dp = [False] * (capacity + 1)
    dp[0] = True  # 0 무게는 항상 만들 수 있음

    for potato in potatoes:
        for j in range(capacity, potato - 1, -1):  # 뒤에서부터 업데이트
            if dp[j - potato]:
                dp[j] = True

    return dp[capacity]

# 테스트
data = [
    (20, [3, 2, 1, 3, 3, 2, 3, 2, 1, 1]),  # YES
    (25, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3])   # NO
]

for i, (c, potatoes) in enumerate(data, start=1):
    result = "YES" if subset_sum_dp(c, potatoes) else "NO"
    print(i, result)
