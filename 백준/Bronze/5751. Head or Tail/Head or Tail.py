while 1:
    N = int(input())
    if N == 0:
        break
    li = list(map(int, input().split()))
    j = m = 0
    for n in li:
        if n == 1:
            j += 1
        else:
            m += 1
    print(f"Mary won {m} times and John won {j} times")