dust = int(input())
if dust >= 150:
    print("매우 나쁨")
elif dust <= 150 and dust >= 81:
    print("나쁨")
elif dust <= 80 and dust >= 31:
    print("보통")
elif dust <= 30 and dust >= 0:
    print("좋음")
else:
    if dust < 0:
        print('음수값 입니다.')
    else:
        print('좋음')