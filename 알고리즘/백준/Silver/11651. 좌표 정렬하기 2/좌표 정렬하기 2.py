import sys
input = sys.stdin.readline
T = int(input())
ary = []
for _ in range(T):
    [X, Y] = map(int, input().split())
    ary.append([Y, X])

new_ary = sorted(ary)

for i in range(T):
    print(new_ary[i][1], new_ary[i][0])
