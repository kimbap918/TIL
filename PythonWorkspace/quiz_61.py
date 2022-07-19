M = int(input()) # 최소값 
N = int(input()) # 최대값
A = [] # 범위 내의 소수를 담을 리스트
B = 0 # 합계를 담을 변수 

# 아리스토텔레스의 체
for i in range(2, N+1): # 2부터 최대값+1의 범위까지
    check = True
    for j in range(2, int((i**0.5)+1)): # 최대값의 제곱근까지만 탐색
        if i%j == 0:
            check = False
    if check:
        if i >= M: # 도출된 소수가 최소값인 M보다 클 경우에만 삽입
            A.append(i)

for k in range(len(A)): # 리스트 A의 합계
    B += A[k]  

if A != []: # 리스트가 비어있지 않을 경우
    print(B)
    print(A[0])
else: # 비어있는 경우
    print(-1)