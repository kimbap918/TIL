# 입력
a, b, c = map(int, input().split())

# 출력
avg = (a+b+c)//3
res = 0  # 이동거리

# c => b
res += (c-avg)
b += (c-avg)

# b => a
res += (b-avg)

# 출력
print(res)