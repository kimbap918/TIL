num = int(input())
numbox = []

for i in reversed(range(1, 6)):
    div_num = num//i
    num = num%i
    numbox.append(div_num)

print(sum(numbox))
