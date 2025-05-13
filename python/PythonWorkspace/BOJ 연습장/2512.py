# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
#  상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

def check(arr):
    start, end = 0, max(arr)

    while start <= end:
        mid = (start+end) // 2
        total = sum(min(mid, x) for x in arr)

        if total > M:
            end = mid - 1
        else:
            start = mid + 1

    return end

if sum(arr) <= M:
    print(max(arr))
else:
    print(check(arr))


# 1. 평균(최소값 + 최대값) % 2 이상인 값들을 남긴다
# 2. 평균 이하의 값들은 M에서 차감하고 계산에서 제외한다.
# 3. 평균 이상의 값에서 이분탐색을 이용, 최소값(start)에서 부터 최대값(end)사이에 분배할 금액을 비교
