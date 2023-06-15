while True:
    N = int(input().strip())
    if N == 0:
        break
    for i in range(1, N+1):
        print("*"*i)