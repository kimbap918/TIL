# n을 입력받고 입력받은 값이 짝수이면 1~n 까지 곱하는 팩토리얼을 구현하고
# n이 홀수이면 1부터 n까지 더하는 시그마를 구현



n = int(input())
res_1 = 1
res_2 = 0

if n % 2 == 0:
    # 4
    # 0 1 2 3 4
    for i in range(n, 1, -1):
        # 4 * 3 * 2 * 1
        res_1 *= i
    print(res_1)
else:
    for i in range(1, n+1):
        res_2 += i
    print(res_2)



