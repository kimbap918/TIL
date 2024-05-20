# score라는 변수에 점수를 입력받기
# 90점 이상일때만 합격이라고 출력

# 점수를 입력하세요 : 90


import sys
# input = sys.stdin.readline


while True:
    score = int(input("점수를 입력하세요 : "))

    if score > 100 or score < 0:
        print("잘못 입력된 점수입니다. 다시 입력해주세요")
    else:    
        if score >= 90:
            print(str(score)+"의 점수로 합격입니다.")
            break
        elif score < 90:
            print(str(score)+"의 점수로 불합격입니다.")
            break