N = int(input())
switchs = list(map(int, input().split()))
S = int(input())
students = [list(map(int, input().split())) for _ in range(S)]

def man(num):
    for i in range(num - 1, N, num):
        switchs[i] = 1 - switchs[i]  # 상태 반전

def woman(num):
    idx = num - 1
    left = idx
    right = idx

    while left - 1 >= 0 and right + 1 < N and switchs[left - 1] == switchs[right + 1]:
        left -= 1
        right += 1

    for i in range(left, right + 1):
        switchs[i] = 1 - switchs[i]  # 상태 반전

for gender, number in students:
    if gender == 1:
        man(number)
    else:
        woman(number)

# 출력: 20개씩 한 줄에 출력
for i in range(N):
    print(switchs[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
