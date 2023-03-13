n = int(input())
num = 1

for i in range(n):
    print(" "*(n-i-1)+"*"*num)
    num+=2
num-=4

for j in range(n):
    print(" "*(j+1)+"*"*num)
    num-=2



# 1, 3, 5, 7, 9
