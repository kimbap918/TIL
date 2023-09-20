import sys
import math
input = sys.stdin.readline

# 테스트 케이스 수
T = int(input())
# 정수(짝수)를 테스트 케이스 수만큼 입력
N = [int(input()) for i in range(T)]
# 입력 값 중 가장 큰 값
max_N = max(N)
# 소수 판별을 위한 배열
arr = [True for i in range(max_N+1)]
bucket = [] 

# 2부터 최대값의 제곱근까지 판별
for i in range(2, int(math.sqrt(max_N))+1):
    # 해당 인덱스가 True면
    if arr[i] == True:
        j = 2
        # i*j가 최대값보다 작거나 같을때까지
        while i * j <= max_N:
            arr[i*j] = False
            j += 1

# for i in range(2, max_N+1):
#     bucket.append(i)


# 입력한 N값들을 꺼내온다
for i in N:
    cnt = 0
    # 2부터 i의 절반 범위에서 소수찾기
    for j in range(2, i//2+1):
        if arr[j] and arr[i-j]:
            cnt += 1
    print(cnt)

    # print(cnt)
    # for i in bucket:
    #     if i >= N:
    #         break
    #     if bucket[i]
    #     print(i)

    #print(cnt)


# def goldbach(n):
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i 
#     return 



