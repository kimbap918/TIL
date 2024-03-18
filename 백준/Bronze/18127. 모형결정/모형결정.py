A,B = map(int,input().split())
a=1
b=1
for i in range(B):
    a += A-2
    b += a
print(b)
