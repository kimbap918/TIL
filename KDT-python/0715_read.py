# 파일명, 어떤 모드로 열지,
# 인코딩을 설정
with open('students.txt', 'r', encoding='utf-8') as f:
    # 텍스트는 String 타입
    text = f.read()
    print(text, type(text))
    # string.split() => st 타입
    names = text.split()
    cnt = 0
    for name in names:
        if name.startwith('김'):
        # name : 첫번째 시행 - 김세환
        #if name[0] == '김':
            cnt += 1
    print(cnt)


