# 공포도가 X인 모험가는 반드시 X명 이상 구성한 모험가 그룹에 참가해야함
# N명의 모험가에 대한 정보가 주어졌을때 여행을 떠날 수 있는 글부 수의 최댓값

N = int(input())
group = sorted(list(map(int, input().split())))
res = 0
cnt = 0

# 1, 2, 2, 2, 3
for i in group:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0


print(res)
