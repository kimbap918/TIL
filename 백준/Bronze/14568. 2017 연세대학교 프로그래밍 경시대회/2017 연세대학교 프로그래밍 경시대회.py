import sys

# 남는 사탕이 없어야함
# 남규는 영훈이보다 2개 이상 많은 사탕을 가져야함
# 셋 중 사탕이 0개 받는 사람은 없어야함
# 택희가 받는 사탕은 홀수면 안됨

input = sys.stdin.readline

N = int(input())
cnt = 0

def candy(A, B, C):
    if A + B + C > N:
        return 0
    elif A + B + C < N:
        return 0
    elif C < B+2:
        return 0
    elif A%2 == 1:
        return 0
    else:
        return 1

tak, young, nam = 0, 0, 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if candy(i,j,k) == 1:
                cnt += 1

if cnt > 0:
    print(cnt)
else:
    print(0)