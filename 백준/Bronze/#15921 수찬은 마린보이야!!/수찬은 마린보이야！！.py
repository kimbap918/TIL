N = int(input())
if N == 0:
    print("divide by zero")
else:
    li = list(map(int, input().split()))
    ans = sum(li)/N / (sum(li)/N)
    print("%.2f" % ans)