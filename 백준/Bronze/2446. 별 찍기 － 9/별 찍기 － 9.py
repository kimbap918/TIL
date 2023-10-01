n = int(input())
for i in range(n, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))
for j in range(2,n+1):
    print(" " * (n-j) + "*" * (2*j-1))