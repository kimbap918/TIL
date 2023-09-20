A, B = map(int, input().split())# A = 시 B = 분
C = int(input())
D = B + C

if (D / 60) > 1: # D를 60으로 나누었을때 1시간 초과인 경우
    A += (D // 60) # 시간 + 몫
    B = round(((D / 60) - (D // 60)) * 60) # (나눈값 - 몫) * 60
    if A > 23:
        A = A - 24
elif (D / 60) < 1: # D를 60으로 나누었을때 1시간 미만인 경우
    B = D
else: # 1시간 초과이면서 정각일때
    A += int((D / 60))
    B = 0
    if A > 23: # 자정을 넘을때
        A = A - 24

print(A, B)