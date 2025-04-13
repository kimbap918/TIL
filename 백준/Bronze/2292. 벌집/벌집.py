# 등차수열 
# N번째 항의 값 = 시작숫자 + (시작숫자-1) * 공차
start = 1 # 시작지점(시작숫자)
res = 0 # 도착까지 횟수 
goal = int(input()) # N번째 항의 값, 목표지점
a = []

for i in range(0, goal):
    start += res * 6
    a.append(start)
    if start < goal:
        res += 1
    else:
        res += 1
        break
print(res)
