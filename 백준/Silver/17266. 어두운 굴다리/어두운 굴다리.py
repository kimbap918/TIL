def check(lights, N, height):
    last_covered = 0  # 커버 시작점

    for light in lights:
        start = max(0, light - height)
        end = light + height

        # 커버 안 이어지면 실패
        if start > last_covered:
            return False
        
        last_covered = max(last_covered, end)

    # 끝까지 커버했는지 확인
    return last_covered >= N


def find_min(lights, N):
    left = 0
    right = N
    result = N

    while left <= right:
        mid = (left + right) // 2
        if check(lights, N, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# 입력 처리
N = int(input())
M = int(input())
lights = list(map(int, input().split()))
lights.sort()

# 최소 높이 찾기
min_height = find_min(lights, N)
print(min_height)
