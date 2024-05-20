
while True:
# 구구단 계산기
    try: 
        N = int(input("몇 단을 계산하시겠습니까? (0입력시 종료) : "))
        if N == 0:
            print("프로그램을 종료합니다.")
            break
        for i in range(1, 10):
            res = N * i
            print(str(N) + "x" + str(i) + "=" + str(res))
    except ValueError:
        print("숫자를 입력해주세요")