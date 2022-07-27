T = int(input())

for i in range(1, T+1):
    S = input()

    for j in range(1, 10):
        if S[:j] == S[j:j*2]: # i의 2배 길이를 곱해주면 찾는 마디의 수를 알수있다.
            print('#{} {}'.format(i, j))
            break
