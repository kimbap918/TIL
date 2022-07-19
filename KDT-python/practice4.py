# 20
number = input()
a = 0
b = list(number)
for i in range(len(b)):
    a += int(b[i])
print(a)

# 20
# 방법 1
number = int(input())
result = 0

while number:
    result += number%10
    number //= 10
print(result)

# 20 방법 2
# divmod(x, y)는 x를 y로 나누고
# 결과를 tuple로 반환한다.
number, remainder = divmod(number, 10)
result += remainder

# 21
number = 123
while number:
    result *= 10
    result += number%10
    number //= 10

n = int(input())

def rev(n):
    if n <= 0 : return
    print(n%10, end = '')
    rev(n//10)

rev(n)