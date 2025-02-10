import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

count = 0
for start in range(N):
    for end in range(start + 3, N + 1):
        substring = S[start:end]
        if substring[0] == 'A' and substring[-1] == 'A' and substring.count('A') == 2 and substring.count('N') == 1: count += 1
print(count)