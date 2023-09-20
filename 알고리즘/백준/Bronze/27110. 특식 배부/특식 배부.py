N = int(input())
chicken = list(map(int, input().split()))
result = 0

for i in range(3) :
    if chicken[i] <= N :
        result += chicken[i]
    else :
        result += N

print(result)