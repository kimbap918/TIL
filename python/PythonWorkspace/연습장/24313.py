a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())


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


# 모든 n0보다 크거나 같은 n에 대해 fn 보다 크거나 같은 c*g(n)인 양의 상수 c와 n0가 존재한다.
# 14 
# O(g(n)) = {f(n) 모든 n >= n0에 대하여 fn <= c*g(n)인 양의 상수 c와 n0가 존재한다}

# 7 7
# 8
# 1
# fn = 7n + 7, g(n) = n, c = 8, n0 = 1
# f(1) = 14, c*g(1) = 8  