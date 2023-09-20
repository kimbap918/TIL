def factorial(x):
    if (x > 1):
        return x * factorial(x-1)
    else:
        return 1

N = int(input())
cnt = 0

for i in str(factorial(N))[::-1]: # 문자로 반환된 factorial(N)을 역순으로 세 가며 0이 나오지 않으면 멈춘다
    if i != '0':
        break
    cnt += 1
print(cnt)
