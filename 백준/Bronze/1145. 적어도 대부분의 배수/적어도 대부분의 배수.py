from math import gcd
from itertools import combinations

def lcm(a, b):
    return a * b // gcd(a, b)

def find_least_multiple(nums):
    # 모든 가능한 3개 조합에 대해 최소공배수를 계산
    min_multiple = float('inf')
    for comb in combinations(nums, 3):
        multiple = comb[0]
        for num in comb[1:]:
            multiple = lcm(multiple, num)
        min_multiple = min(min_multiple, multiple)
    return min_multiple

# 입력 받기
nums = list(map(int, input().split()))

# 결과 출력
print(find_least_multiple(nums))
