T = int(input())
for i in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W # 리터당 요금 * 사용량
    B = Q if W <= R else Q + (W-R)*S
    print("#{0} {1}".format(i, B if A>B else A))