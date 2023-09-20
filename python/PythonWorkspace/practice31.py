# 표준입출력

# print("python", "java", sep = ", ", end="?") # sep 는 각 구분자 사이에 넣을 값 출력, end는 문장의 끝에 넣을 값 출력
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr) # 표준 에러로 처리

# scores = {"수학":0, "영어":50, "코딩":100} # dictionary
# for subject, scores in scores.items():
#     print(subject, scores)
#     print(subject.ljust(8), str(scores).rjust(4), sep=": ") # ljust -> left justify  rjust -> right justify

# # 은행 대기순번
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) # zero fill 3칸을 확보해 값이 없는 빈 공간에 대해 0을 채움

answer = input("아무값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")