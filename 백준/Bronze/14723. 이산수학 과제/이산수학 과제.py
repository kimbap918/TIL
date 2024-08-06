n = int(input())
i = 1
while i*(i+1)//2 < n:
    i += 1
b = n - (i-1)*i//2
a = i+1 - b
print(a, b)