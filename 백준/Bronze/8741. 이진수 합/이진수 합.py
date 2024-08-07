k = int(input())
t = 2**k - 1
res = t*(t+1)//2
print(bin(res)[2:])