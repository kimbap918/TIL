from collections import defaultdict

T = int(input())
total = []

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    teams = defaultdict(int)

    # 팀 개수 세기
    for num in arr:
        teams[num] += 1


    # 골인한 팀 필터
    team = {teams for teams, count in teams.items() if count >= 6}
    arr = [x for x in arr if x in team]


    # 순위, 점수부여
    scores = defaultdict(list)
    rank = 1

    for i in arr:
        scores[i].append(rank)
        rank += 1

    res = []
    for team, score in scores.items():
        # print(team, score)
        total_score = sum(score[:4])
        fifth = score[4]

        res.append([total_score, fifth, team])
        res.sort()
    
    total.append(res[0][2])

for i in total:
    print(i)
