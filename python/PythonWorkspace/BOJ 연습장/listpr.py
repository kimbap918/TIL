# - 힌트 과목과 점수를 리스트에 저장 받으세요
# - 딕셔너리 보다는 리스트 추천

# 국어:점수
# 영어:점수
# 수학:점수
# .
# .
# .
# 등을 입력했을 경우 평균을 내어주는 함수를 작성해보시오.
# (과목의 제한은 없다.)

# 과목: 수학
# 점수: 20
# 추가 하실 건가요?
#     예 or 아니오 : 예
# 과목: 국어
# 점수: 50
# 추가 하실 건가요?
#     예 or 아니오 : 아니오
# 수학 : 20
# 국어 : 50
# 평균 : 35


def get_average_score():

    dict = {}

    while True:
            try:
                subject = input("과목: ")
                score = int(input("점수: "))
                question = input("추가 하실 건가요? \n\t 예 or 아니오 : ")
            except ValueError:
                print("올바른 값을 입력하세요")
                continue
            
            if question == "예":
                dict[subject] = score
                # print(dict)

            elif question == "아니오":
                summ = 0
                dict[subject] = score
                for k, v in dict.items():
                    print(k + " : " + str(v))
                    summ += v
                print("평균 : " + str(int(summ/len(dict))))
                break
    
get_average_score()
