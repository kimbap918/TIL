A, B, C = map(int, input().split())
cnt = 0
D = C - B  

if B > C or D == 0:
    print(-1)
else:
    result = A//D+1
    print(result)


