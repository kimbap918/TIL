# i가 3의 배수이면서 5의 배수이면 “FizzBuzz”를 출력합니다.
# i가 3의 배수이지만 5의 배수가 아니면 “Fizz”를 출력합니다.
# i가 3의 배수가 아니지만 5의 배수이면 “Buzz”를 출력합니다.
# i가 3의 배수도 아니고 5의 배수도 아닌 경우 i를 그대로 출력합니다.

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def find_number(a, b, c):
    # 두 번째 또는 세 번째 값이 숫자인 경우를 활용
    if b.isdigit():
        num = int(b)
        if fizzbuzz(num-1) == a and fizzbuzz(num+1) == c:
            return num - 1
    
    if c.isdigit():
        num = int(c)
        if fizzbuzz(num-2) == a and fizzbuzz(num-1) == b:
            return num - 2
    
    # 첫 번째 값이 숫자인 경우
    if a.isdigit():
        num = int(a)
        if fizzbuzz(num) == a and fizzbuzz(num+1) == b and fizzbuzz(num+2) == c:
            return num
    
    # 모든 값이 숫자가 아닌 경우, 가능한 모든 시작점 확인
    # FizzBuzz 패턴은 15개 단위로 반복되므로 1부터 15까지만 확인
    for i in range(1, 16):
        if (fizzbuzz(i) == a and 
            fizzbuzz(i+1) == b and 
            fizzbuzz(i+2) == c):
            return i
    
    # 더 큰 범위에서 확인
    for i in range(16, 1000001):
        if (fizzbuzz(i) == a and 
            fizzbuzz(i+1) == b and 
            fizzbuzz(i+2) == c):
            return i
    
    return -1  # 일치하는 패턴을 찾지 못함

# 입력 받기
a = input().strip()
b = input().strip()
c = input().strip()

# 시작 숫자 찾기
start = find_number(a, b, c)

if start != -1:
    # 다음 문자열 출력
    print(fizzbuzz(start+3))