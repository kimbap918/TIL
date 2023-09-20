N = int(input())
A = []
cnt = 0
sum = 0

for i in range(N): # 입력 테스트 케이스동안
    A = input()    # OX 입력
    for j in A:    # 순차적으로 돌면서 테스트 케이스 확인
        if j == "O": # O인경우
            cnt += 1 # +1
            sum += cnt # cnt를 누적
        elif j == "X": # X인경우
            cnt = 0 # 0점
    print(sum) # 누적된 점수 출력
    sum = 0 # 초기화
    cnt = 0 # 초기화
