N = int(input())
n = 0
for i in range(1, N+1): # 입력값의 범위, ex : 123
    separate = list(map(int, str(i))) # 입력값을 분해 [1, 2, 3]
    hap = i + sum(separate) # 원본에 분해를 합한 값 123+6 = 129 
    if hap == N: # 분해합이 입력값과 같다면 
        n = i # n 변수에 i를 저장, 생성자가 없으면 0출력
        break

print(n) # i를 출력
