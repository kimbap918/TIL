K, N, M = map(int, input().split())
answer = (K*N)-M 

if answer > 0:
    print(answer)
else:
    print(0)