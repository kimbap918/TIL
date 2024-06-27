t_machine = list(map(int, input().split(':')))
hour = [h for h in range(1, 13)]
min_sec = [ms for ms in range(60)]

result = 0

for i in range(3) :
    for j in range(3) :
        for k in range(3) :
            if i != j and j != k and k != i :	# 3개의 숫자가 다른 위치에 해당하기 위한 조건
                if t_machine[i] in hour and t_machine[j] in min_sec and t_machine[k] in min_sec :
                    result += 1

print(result)
