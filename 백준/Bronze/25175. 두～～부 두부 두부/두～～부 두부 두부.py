n, m, k = map(int, input().split())
 
while k < 0:
    k += n
 
result = (((k - 3) % n) + m)
if result > n:
    result %= n
print(result)
 