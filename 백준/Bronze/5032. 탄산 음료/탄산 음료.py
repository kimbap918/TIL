e, f, c = map(int, input().split())
n = (e+f)//c + (e+f)%c
res = (e+f)//c
while n//c:
    res += n//c
    n = n//c + n%c
print(res)