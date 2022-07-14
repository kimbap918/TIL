s = input()
cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cro_list:
    s = s.replace(i, '*') # 문자열 s의 크로아티아 단어를 전부 *로 바꿈
    print(s)
print(len(s))

