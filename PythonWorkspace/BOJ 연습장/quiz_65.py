# N = 10000
# array1 = []
# array2 = []
# [array1.append(i) for i in range(N+1) if True]
# array1[0], array1[1] = False, False #0,1은 소수가 아니기에 False로 설정

# for i in range(2, int(N**0.5)+1): # 2부터 N의 제곱근 범위
#     if array1[i]:
#         j = 2
#         while i*j <= N:
#             array1[i * j] = False
#             j += 1
# # 소수만 리스트에 담는다
# [array2.append(i) for i in range(len(array1)) if array1[i] != False] 

# # 골드바흐 수를 출력
# T = int(input())
# for _ in range(T):
#     even = int(input())
#     half = even//2  # 입력받은 짝수를 2로 나눈 몫을 구함. / 기호를 쓰면 실수가 됨.
#     for x in range(half, 1, -1):  # 차이가 적은 두 수를 구하기 위해서 큰수부터 꺼냄
#         if (even-x in array2) and (x in array2):  # even-x 와 x가 소수 집합에 포함 되었는지 확인
#             print(x, even-x)  # 작은수부터 출력
#             break

N = 10000
array1 = []
array2 = []
[array1.append(i) for i in range(N+1) if True]
array1[0], array1[1] = False, False

for i in range(2, int(N**0.5)+1):
    if array1[i]:
        j = 2
        while i*j <= N:
            array1[i*j] = False
            j += 1
[array2.append(i) for i in range(len(array1)) if array1[i] != False]

T = int(input())
for i in range(T):
    n = int(input())
    half = n // 2
    for j in range(half, 1, -1):
        if (n - j in array2) and (j in array2):
            print(j, n-j)
            break