import sys
input = sys.stdin.readline
T = int(input())
ary = []
for _ in range(T):
    [X, Y] = map(int, input().split())
    ary.append([X, Y])

re_ary = sorted(ary)

for i in range(T):
    print(re_ary[i][0], re_ary[i][1])

