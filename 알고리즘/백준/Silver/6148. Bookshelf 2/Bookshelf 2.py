import sys
input = sys.stdin.readline
def dfs(cows, height, target, current_height, idx):
    # 모든 소를 확인했을 때
    if idx == len(cows):
        # 현재 높이가 B보다 크거나 같을 경우
        if current_height >= target:
            # 현재 높이 - B
            return current_height - target 
        else:
            # 현재 소들의 높이의 합이 책장의 높이보다 작은 경우 float('inf')를 반환함으로써, 
            # 이 경우를 유효하지 않은 경우로 표시하고 최소 높이 차이 계산 시 고려되지 않도록 처리
            return float('inf')
    # 현재 소를 포함하는 경우
    include_height = dfs(cows, height, target, current_height + cows[idx], idx + 1)

    # 현재 소를 포함하지 않는 경우
    exclude_height = dfs(cows, height, target, current_height, idx + 1)

    # 최소 높이 차이 반환
    return min(include_height, exclude_height)

# 입력 처리
N, B = map(int, input().split())
cows = [int(input()) for _ in range(N)]

# DFS 호출
result = dfs(cows, N, B, 0, 0)

# 결과 출력
print(result)
