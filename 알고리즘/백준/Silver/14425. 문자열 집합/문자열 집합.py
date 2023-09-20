import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic_N = {input():0 for _ in range(N)}
for _ in range(M): 
    S = input()
    if S in dic_N:
        dic_N[S] += 1
sum = 0
for v in dic_N.values():
    sum += v
    

print(sum)