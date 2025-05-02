T = int(input())

# a_n​=a_{n−3}​+⌊n/2​⌋+1(n: 자연수,a₁=1,a₂=2,a₃​=3)

def cnt_combination(N):
    res = 0
    for i in range(N//3 + 1):
        tmp = N - (3*i)
        res += (tmp // 2) + 1
    return res

for _ in range(T):
    N = int(input())
    print(cnt_combination(N))
