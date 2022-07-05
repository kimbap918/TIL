# 가변인자, 서로 다른 개수의 값을 넣기위해 사용

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ") # 줄바꿈을 하지 않기위에 끝에 end= " "
    print()

profile("유재석", 20, "python", "java", "C", "C++", "C#")
profile("김태호", 25, "koflin", "swift")