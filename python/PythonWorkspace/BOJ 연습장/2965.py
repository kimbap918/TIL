import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
cnt = 0

while True:
    if B-A == C-B and B-A == 1:
        break

    if B-A <= C-B:
        A = B
        B = C-1
        cnt += 1
    elif B-A >= C-B:
        C = B
        B = C-1
        cnt += 1


print(cnt)


# 1 5 9

# 5 8 9

# 5 7 8

# 5 6 7