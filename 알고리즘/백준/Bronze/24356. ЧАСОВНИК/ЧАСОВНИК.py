# 입력
t1, m1, t2, m2 = map(int, input().split())

# 시간 계산
time = (t2-t1)*60 + (m2-m1)
if time < 0:
    time += 1440

# 출력
print(time, time//30)