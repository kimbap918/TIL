import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c] :
        return dp[a][b][c]

    if a<b<c :
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

    return dp[a][b][c]



dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]
while True:
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))

# 그냥, 문제에 있는 함수를 그대로 구현하여 dp값이 존재하면 return해주면 구현이 끝난다 !

# 해당 문제에서 재귀로 오래걸렸던 이유는 계속해서 동일한 값을 또 연산하고 또 연산하기 때문이다.

# 이를 if dp[a][b][c] : return dp[a][b][c] 즉 dp[a][b][c]의 값이 존재한다면, 해당 값을 리턴하라는 기능만 추가해주면 연산속도가 기하급수적으로 빨라진다.