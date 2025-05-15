N, D, K = map(int, input().split())
s = list(map(int, input().split()))

max_star_per_day = max(s)
star_cnt = 0
answer = 0

for _ in range(D):
    star_cnt += max_star_per_day
    if star_cnt > K:
        star_cnt = max_star_per_day
        answer += 1

print(answer)