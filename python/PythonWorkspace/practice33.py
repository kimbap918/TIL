# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8") # 생성, w = write
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() # 끝에 파일을 반드시 닫아줄것.

# score_file = open("score.txt", "a", encoding="utf8") # 기존 파일에 추가, a = append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # 파일 불러오기, r = read
# print(score_file.read())
# score_file.close() 

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄 별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # 줄의 수를 알 수 없는 파일을 불러올때
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
