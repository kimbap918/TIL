# 입력
s = int(input())
a = int(input())
b = int(input())

# 출력
res = 250
if s <= a:
    print(res)
else:
    res += ((s-a)//b)*100
    if (s-a) % b != 0:
        res += 100
    print(res)