a, d, k = map(int, input().split())
print((k-a)//d +1 if (k-a)%d == 0 and (k-a)//d >= 0 else 'X')