import math

# 입력 받기
N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠 계산
t_bundles = 0
for size in sizes:
    # 각 사이즈별로 필요한 최소 묶음 수 계산
    # 올림 연산 사용 (나누어 떨어지지 않으면 하나 더 필요)
    bundles = math.ceil(size / T)
    t_bundles += bundles

# 펜 계산
# 펜은 정확히 N개 필요
# P자루씩 묶음으로 최대한 주문하고 나머지는 낱개로
p_bundles = N // P  # 몫 (최대 묶음 수)
p_singles = N % P   # 나머지 (낱개 주문 수)

# 결과 출력
print(t_bundles)
print(p_bundles, p_singles)