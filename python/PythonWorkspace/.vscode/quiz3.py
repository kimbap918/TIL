
# 방법 1
site = "http://www.naver.com"
pwd1 = site[11:16]
pwd2 = str(len(pwd1))

print(pwd1[0:3] + pwd2 + str(pwd1.count("e")) + "!")

# 방법 2
site = "http://www.naver.com"
pwd1 = site.replace("http://www.", "")
print(pwd1)
pwd1 = pwd1[:pwd1.index(".")]
print(pwd1)
pwd2 = pwd1[:3] + str(len(pwd1)) + str(pwd1.count("e")) + "!"
print(pwd2)
print("{0}의 비밀번호는 {1} 입니다.".format(site, pwd2))

