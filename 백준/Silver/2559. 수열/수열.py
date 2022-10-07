import sys
input = sys.stdin.readline

# 전체 날짜 수 N, 합을 구할 연속 날짜 수 K
N, K = map(int,input().split())
# 매일 측정한 온도
arr = list(map(int, input().split()))

result = []
# 합을 구할 연속 날짜 수 까지만 더한다 
result.append(sum(arr[:K]))

# 전체 날짜에서 연속 날짜 수를 뺀 범위만큼
# 범위 안의 값을 모두 사용하지 않아도 된다
for i in range(N - K):
    # 합산된 값에 - 이전값 제외  - 이후 값들 더하기
    result.append(result[i] - arr[i] + arr[K+i])
# 그 중 큰 값
print(max(result))