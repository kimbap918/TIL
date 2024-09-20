n = int(input())
x = h = 0
while x <= n:
    h += 1
    x += (h*2-1)**2 - 4*(h*(h-1)//2)
if x > n:
    h -= 1
print(h)