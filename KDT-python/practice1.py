# 9번 문제
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
cnt = 0
for i in range(len(students)):
    if students[i] == '이영희':
        cnt += 1
print(cnt)

# 10번 문제
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
cnt = 0
for i in range(len(numbers)):
    if numbers[i] == 5:
        cnt += 1
print(cnt)

# 11번 문제
for i in range(1, 10):
    print("{0}단".format(i))
    for j in range(2, 10):
        print("{0} X {1} = {2}".format(i, j, i*j))

# 12번 문제
a = input()
result = a
for i in a:
    if i in "a":
       result = result.replace("a", '')
print(result)

# 13번 문제
a = input()
b = list(a)
c = []
for i in reversed(b):
    c.append(i)
for i in range(len(a)):
    print(c[i], end='')

# 1번 기초함수 문제
def cube(n): 
    return n*n*n

print(cube(12))

# 2번 기초함수 문제
def rectangle(a, b):
    return a * b, (a + b) * 2

print(rectangle(20, 30))