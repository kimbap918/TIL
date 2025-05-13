# 1. 플레이어가 입장을 신청하였을 때 매칭이 가능한 방이 없다면 새로운 방을 생성하고 입장시킨다.
#    이떄 해당 방에는 처음 입장한 플레이어의 레벨을 기준으로 -10부터 +10까지 입장 가능하다.
# 2. 입장 가능한 방이 있다면 입장시킨 후 방의 정원이 모두 찰 때까지 대기시킨다.
# 2-1. 이때 입장이 가능한 방이 여러 개라면 먼저 생성된 방에 입장한다.
# 3. 방의 정원이 모두 차면 게임을 시작시킨다.

p, m = map(int, input().split())
players = []

for _ in range(p):
    l, n = input().split()
    players.append((int(l), n))

rooms = []

for level, nickname in players:
    placed = False
    for room in rooms:
        # 방에 여유가 있고, 레벨 조건도 맞을 경우
        if len(room['players']) < m and room['min_level'] <= level <= room['max_level']:
            room['players'].append((level, nickname))
            placed = True
            break

    # 입장 가능한 방이 없으면 새 방 생성
    if not placed:
        new_room = {
            'min_level': level - 10,
            'max_level': level + 10,
            'players': [(level, nickname)]
        }
        rooms.append(new_room)

# 출력
for room in rooms:
    if len(room['players']) == m:
        print("Started!")
    else:
        print("Waiting!")
    
    for player in sorted(room['players'], key=lambda x: x[1]):  # 닉네임 사전순 정렬
        print(player[0], player[1])
