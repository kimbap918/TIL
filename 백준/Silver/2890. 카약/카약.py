R, C = map(int, input().split())
kayaks = {'111':1, '222':2, '333':3, '444':4, '555':5, '666':6, '777':7, '888':8, '999':9}
maps = list(input() for _ in range(R))
distances = {key: 0 for key in kayaks.keys()}

for i in range(len(maps)):
    for k, v in kayaks.items():
        if k in maps[i]:
            distances[k] = maps[i].index('F') - maps[i].index(k[0]) 
            # F에서 얼마나 떨어져있는지 확인, 숫자가 작을수록 순위가 높음

rank = distances.copy()
score = 0  # 순위
prev = -1  # 이전 거리

# v 거리
for k, v in sorted(distances.items(), key=lambda item: item[1]):
    if v == prev:  # 이전 거리와 동일하면 동일 순위 부여
        rank[k] = score
    else:  # 이전 거리와 다르면 현재 점수로 갱신
        score += 1  # 순위는 건너뛰지 않고 증가
        rank[k] = score
    prev = v

for v in rank.values():
    print(v)
