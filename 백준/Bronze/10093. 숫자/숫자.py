a, b = map(int, input().split())
n1 = min(a, b)
n2 = max(a, b)
n = n2-n1-1
if n1 == n2 or n1+1 == n2:
    n = 0    
print(n)
for i in range(n1+1, n2):
    print(i, end = ' ')