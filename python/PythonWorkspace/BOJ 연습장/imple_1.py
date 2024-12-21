# 시 24
# 분 60
# 초 60

N = int(input())
cnt = 0

for hour in range(0, N+1):
    for minute in range(1, 61):
        for second in range(1, 61):
            time = str(hour) + str(minute) + str(second)
            if "3" in time:
                cnt+=1


print(cnt)
