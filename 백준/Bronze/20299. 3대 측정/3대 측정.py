import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())
cnt = 0 # 클럽 가입이 가능한 팀원 수
res = []

for _ in range(N) :
    team = list(map(int, input().split()))
    check = True	# 조건 판별 변수

    for i in team :
        if i < L :
            check = False
            break
    if check :
        if sum(team) >= K :
            res.extend(team)
            cnt += 1

print(cnt)
print(*res)
