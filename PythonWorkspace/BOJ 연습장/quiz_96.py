import sys
input = sys.stdin.readline

N = int(input())
candidate = {}

for i in range(N):
    s = input()
    if s not in candidate:
        candidate[s] = 1
    else:
        candidate[s] += 1
            
for j in range(N-1):
    x = input()
    if x in candidate:
        candidate[x] -= 1

for k, v in candidate.items():
    if v == 1:
        print(k, end='')

