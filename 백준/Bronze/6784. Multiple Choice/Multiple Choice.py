import sys

input = sys.stdin.readline
lst = [input() for _ in range(int(input()))]
ans = 0
for i in range(len(lst)) :
    if lst[i] == input() : ans += 1
print(ans)
