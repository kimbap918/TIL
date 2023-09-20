N = int(input())
Pi = list(map(int, input().split()))

if N == 1:
    print(0)
else:
    result = [0]
    height = 0
    for i in range(N-1):
        if Pi[i] < Pi[i+1]:
            height += Pi[i+1] - Pi[i]
            result.append(height)
        else:
            height = 0
print(max(result))
        