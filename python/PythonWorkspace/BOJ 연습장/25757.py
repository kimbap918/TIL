# 임스와 여러 번 미니게임을 플레이하고자 하는 사람이 있으나, 
# 임스는 한 번 같이 플레이한 사람과는 다시 플레이하지 않습니다.

# 임스와 함께 플레이하고자 하는 사람 중 동명이인은 존재하지 않습니다.
#  임스와 lms0806은 서로 다른 인물입니다.
N, game = map(str, input().split())
N = int(N)
players = set()

for i in range(N):
    player = input()
    players.add(player)


# print(players)
if game == "Y":
    print(len(players))
elif game == "F":
    print(len(players) // 2)
else:
    print(len(players) // 3)

