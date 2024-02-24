while 1:
    n = int(input())
    if n == 0:
        break
    if n <= 1000000:
        print(n)
    elif 1000000 < n <= 5000000:
        print(int(n*0.9))
    else:
        print(int(n*0.8))