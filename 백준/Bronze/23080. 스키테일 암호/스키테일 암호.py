import sys
input = sys.stdin.readline

k = int(input())
s = input().rstrip()

answer = ''
for i in range(0, len(s), k):
    answer += s[i]

print(answer)