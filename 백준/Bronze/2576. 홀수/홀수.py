res = []
for _ in range(7) :
    n = int(input())
    if n % 2 != 0 :	# 홀수 판별
        res.append(n)

if res == [] :	# 빈 리스트이면
    print(-1)	# -1 출력
else :
    print(sum(res))	# 홀수들의 합
    print(min(res))	# 가장 작은 홀수