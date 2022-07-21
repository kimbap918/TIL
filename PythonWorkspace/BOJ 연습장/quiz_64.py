m = 123456 # 문제에서 제시한 최대값
array1 = [] #소수 판별을 위한 리스트설정(True면 소수)
for _ in range((2*m)+1):
    if True:
        array1.append(_)
array1[0], array1[1] = False, False #0,1은 소수가 아니기에 False로 설정

# 에라토스테네스의 체 공식
for i in range(2, int((2*m)**0.5)+1): # 2부터 2*m의 제곱근 까지
    if array1[i]: #만약 array1[i]가 True(소수)라면
        j = 2 # i에 곱해줄 j값을 2부터 설정
        while i*j <= (2*m): #i * j 가 (2*m) 보다 작거나 같을때 까지 구한다.
            array1[i * j] = False # 2 4 6 8...m, 6 9 12...m.. 5 10 15..m 
            j += 1                # 해당 i*j의 값은 소수가 아니므로 False로 설정

while True:
    n = int(input())
    if n == 0: #0이면 반복문 탈출
        break
    count = 0
    # 개수 출력
    for i in range(n+1, (2*n)+1): #n+1(n보다 커야하기 때문) 부터 2 * n + 1 까지 설정
        if array1[i]:  #만약 해당 i가 True(소수) 라면
            count += 1 #count값에다 +1
    print(count)  #count 값 출력