while True:
    N = input()
    if N == '0':
        break
    res = len(N)+1
    for n in N:
        if n == '0':
            res += 4 
        elif n == '1':
            res += 2
        else:
            res += 3
    print(res)