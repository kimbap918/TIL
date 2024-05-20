# 숫자를 입력
# 15이상 20이하면 정상
# 15미만 20초과면 비정상


score = int(input("숫자를 입력하세요 : "))

if 15 <= score <= 20:
    print("정상입니다.") 
elif score < 15 or score > 20:
    print("비정상입니다.")
