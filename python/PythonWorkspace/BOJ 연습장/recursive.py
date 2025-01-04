def iter(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def recur(n):
    if n <= 1:
        return 1
    return n * recur(n-1)


print(recur(5))
print(iter(5))