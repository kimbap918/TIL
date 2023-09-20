N = int(input())
a = 2

while a <= N: # a가 N보다 작거나 같을때까지
    if N % a == 0: # 입력값을 2로 나누어서 떨어지면 2를 출력
        print(a)
        N = N / a # N을 a로 나누고 저장
    else:
        a = a+1 # 아니라면 a를 1씩 증가시킨다.

