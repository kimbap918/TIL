N = int(input())
H = list(map(int, input().split()))
result = 1

for i in range(N-1):
    if H[i] <= H[i+1]:
        result += 1

print(result)
