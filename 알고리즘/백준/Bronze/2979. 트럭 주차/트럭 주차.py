A, B, C = map(int, input().split())
time_table = [0] * 101
for _ in range(3):
    arrive, depart = map(int, input().split())
    for i in range(arrive-1, depart-1): # 1 6 / 01234, / 3 5  23, / 2 8 123456
        time_table[i] += 1
answer = 0
for j in time_table:
    if j == 1:
        answer += A*j
    elif j == 2:
        answer += B*j
    elif j == 3:
        answer += C*j

print(answer)
