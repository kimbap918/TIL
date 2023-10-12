N = int(input())
sum = 0  #점의 개수

for i in range(N+1):
    for j in range(i, N+1):
        sum += (i + j)

print(sum)