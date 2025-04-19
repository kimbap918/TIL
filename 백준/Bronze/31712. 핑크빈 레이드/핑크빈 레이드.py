skillDamage = [list(map(int, input().split())) for _ in range(3)]
H = int(input())
second = 0

while True:
    for s in skillDamage:
        C, D = s[0], s[1]	# 스킬 주기, 대미지
        if second % C == 0:
            H -= D

    if H <= 0:
        print(second)
        break
    else:
        second += 1
