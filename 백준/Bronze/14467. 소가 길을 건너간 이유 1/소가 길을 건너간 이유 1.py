N = int(input())
state, cnt = {}, 0

for _ in range(N):
    num, pos = map(int, input().split())
    if num in state and state[num] != pos:
        cnt += 1
    state[num] = pos
print(cnt)