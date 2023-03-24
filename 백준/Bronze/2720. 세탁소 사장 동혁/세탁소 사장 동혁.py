T = int(input())

for i in range(T):
    C = int(input())
    Q, D, N, P = 0, 0, 0, 0
    Q = C // 25
    C = C % 25
    D = C // 10
    C = C % 10
    N = C // 5
    C = C % 5
    P = C // 1

    print(Q, D, N, P)
