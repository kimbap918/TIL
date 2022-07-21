N = int(input())

# for i in range(N):
#     print('{:>}'.format('*'*(i+1))) # 왼쪽 정렬을 하고 *의 개수 *(i+1)값 만큼 곱한다.

# for i in range(N+1, 0, -1): # -1 인덱스의 마지막 끝, N+1에서 0까지 역순으로
#     print('{:<}'.format('*'*(i-1)))

for i in range(N):
    print('{:<}'.format("*"*(i+1)))

for i in range(N+1, 0, -1):
    print('{:<}'.format("*"*(i-1)))

for i in range(N):
    for j in range(i):
        print(" ", end='')
    for j in range(N-i):
        print("*", end='')
    print('')


for i in range(1, N+1): # 1부터 N+1까지
    for j in range(N-i):# N에서 i값이 빼지며 공백 출력 5..4..3..2
        print(" ", end='')
    for j in range(i): # i값만큼 늘어나며 * 출력 1..2..3..4..5
        print("*", end='')
    print('')
