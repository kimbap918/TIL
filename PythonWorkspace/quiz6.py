def std_weight(height, gender):
    if gender == 1:
        man = round((height * height * 22)/10000, 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, man))
    elif gender == 2:
        girl = round((height * height * 21)/10000, 2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, girl))

height_input = input("키는 몇 cm인가요?")
gender_input = input("성별을 입력해주세요. 남자 : 1, 여자 : 2")

std_weight(int(height_input), int(gender_input))