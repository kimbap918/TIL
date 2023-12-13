a = int(input())
b = int(input())
cnt = 2
while a-b >= 0:
    a, b = b, a-b
    cnt += 1
print(cnt)