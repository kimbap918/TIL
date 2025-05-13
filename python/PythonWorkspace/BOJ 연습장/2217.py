# 2
# 10
# 15

# w/k

# 2/20 = 10

N = int(input())
arr = []

for i in range(N):
    weight = int(input())
    arr.append(weight)

arr.sort(reverse=True)


# [25, 20, 15, 10]
max_weight = 0
for i in range(N):
    weight = arr[i] * (i+1)
    max_weight = max(max_weight, weight)


print(max_weight)

