# 20
number = input()
a = 0
b = list(number)
for i in range(len(b)):
    a += int(b[i])
print(a)