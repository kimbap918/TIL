def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)




# print(fibo(10))