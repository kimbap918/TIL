import sys
input = sys.stdin.readline
N, M = map(int, input().split())

poke_dic = {}
for i in range(1, N+1):
    pokemon = input().rstrip()
    poke_dic[i] = pokemon
    poke_dic[pokemon] = i

for j in range(M):
    S = input().rstrip()
    if S.isalpha() == False: # S가 숫자면
        print(poke_dic[int(S)])
    else:
        print(poke_dic[S])
