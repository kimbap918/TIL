a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# 모든 n0보다 크거나 같은 n에 대해(예: n0이 10이면 n= 10부터 100까지) 
# f = (a1*n) + a0 보다 크거나 같은 cg = c*n 인 양의 상수 c와 n0가 존재하는가?
def fn(a1, a0, c, n0):
    ans = 1
    for n in range(n0, 101):
        f = (a1*n) + a0
        cg = c*n

        if f > cg:
            ans = 0
            break

    return ans

print(fn(a1, a0, c, n0))