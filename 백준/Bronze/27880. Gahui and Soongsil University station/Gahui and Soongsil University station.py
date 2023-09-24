res = 0
for _ in range(4) :
    path, height = input().split()
    res += int(height) * [21, 17][path =='Stair']
print(res)