import sys

M, N = map(int, sys.stdin.readline().split())

# 에라토스테네스의 체 방식 사용
for i in range(2, N+1): # 2부터 N+1의 범위까지 탐색
    check = True
    for j in range(2, int(i**0.5)+1): # 2부터 i의 제곱근까지만 수행
        if i % j == 0: # 소수가 아닐 경우
            check = False
            break
    if check:   # 소수일경우
        if i >= M: # M 이상의 소수만 추가
            print(i)
