# 입력
M, S, G = map(float, input().split())  # M개의 계단, S 에스컬레이터 속도, G 올라가는 계단 속도
A, B = map(float, input().split())
L, R = map(float, input().split())

# 시간 계산
lwait = L/A
rwait = R/B

lv = M/G + 1 if M % G else M/G
rv = M/S + 1 if M % S else M/S

if lv + lwait < rv + rwait:
    print("friskus")
else:
    print("latmask")