
# 입력 받기
N, S, R = map(int, input().split())
damaged = set(map(int, input().split()))
reserves = set(map(int, input().split()))

# 1. 여분이 있는 팀이 자기 카약이 부서졌다면 먼저 사용
real_reserves = reserves - damaged  # 빌려줄 수 있는 팀
real_damaged = damaged - reserves   # 여전히 카약이 부서진 팀

# 2. 카약 빌려주기 (앞뒤 팀에게만 가능)
for r in sorted(real_reserves):  # 작은 번호부터 빌려주기
    if r - 1 in real_damaged:
        real_damaged.remove(r - 1)
    elif r + 1 in real_damaged:
        real_damaged.remove(r + 1)

# 3. 남은 부서진 팀 개수 출력
print(len(real_damaged))