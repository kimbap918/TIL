# T = int(input())

# for i in range(1, T+1):
#     N = int(input())
#     num = [0] * 10
#     k = 1
#     while 0 in num:
#         n = str(N * k)
#         for j in range(len(n)):
#             num[int(n[j])] += 1
#         k += 1
#     print('#{0} {1}'.format(i, n))

T = int(input())
for test_case in range(1, T+1):
    # input 가져오기(첫번째값 -> 1)
    N = int(input())
    N1 = N
    numbers = set()
    # while 반복 -> set 길이가 10이 될 때까지
    while True:
        # for 반복 : 숫자를 문자로
        for n in str(N):
        # numbers set에 추가
            numbers.add(n)
        if len(numbers) == 10:
            break
        # print(n, numbers)
        N += N1
    print(f'#{test_case} {N}')

