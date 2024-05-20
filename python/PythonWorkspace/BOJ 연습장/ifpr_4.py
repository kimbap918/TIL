# 점수만을 입력 받아야한다.
# 90점 이상 A, 
# 90점 미만 80점 이하 B
# 80점 미만  70점 이상 C
# 70점 미만 60점 이상 D


# while True:

#     try:
#         score = int(input("점수를 입력하세요(정수만 입력) :"))
        

#         if isinstance(score, int):
#             if score > 100 or score < 0:
#                 print("잘못된 점수입니다. 다시 입력해주세요")
#                 continue
#             else:
#                 if score >= 90:
#                     print("당신의 학점은 A입니다.")
#                     break
#                 elif 90 > score >= 80:
#                     print("당신의 학점은 B입니다.")
#                     break
#                 elif 80 > score >= 70:
#                     print("당신의 학점은 C입니다.")
#                     break
#                 elif 70 > score >= 60:
#                     print("당신의 학점은 D입니다.")
#                     break
#                 else:
#                     print("당신은 낙제입니다.")
#                     break
#     except ValueError:
#         print("정수만 입력하세요")
        



while True:
    try:
        score = int(input("점수를 입력하세요(정수만 입력) :"))

        if score > 100 or score < 0:
            print("잘못된 점수입니다. 다시 입력해주세요")
            continue
        
        if score >= 90:
            print("당신의 학점은 A입니다.")
        elif score >= 80:
            print("당신의 학점은 B입니다.")
        elif score >= 70:
            print("당신의 학점은 C입니다.")
        elif score >= 60:
            print("당신의 학점은 D입니다.")
        else:
            print("당신은 낙제입니다.")
        break
    except ValueError:
        print("정수만 입력하세요")
