N, K = map(int, input().split())
li = list(map(int, input().split()))
cnt = sum([(n+1)//2 for n in li])
print("YES" if cnt >= N else "NO")