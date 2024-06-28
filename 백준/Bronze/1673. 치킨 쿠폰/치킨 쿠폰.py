while 1:
    try:
        n, k = map(int, input().split())
        res = 0 
        res += n
        while n//k:
            res += n//k
            n = n//k + n%k
        print(res)
    except:
        break