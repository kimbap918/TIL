N = int(input())
ary = []
for i in range(N):
    [A, B] = input().split()
    ary.append([int(A), i, B])

ary = sorted(ary)
# print(ary) [[20, 2, 'Sunyoung'], [21, 0, 'Junkyu'], [21, 1, 'Dohyun']]
for i in range(N):
    print(ary[i][0], end= ' ')
    print(ary[i][2])
