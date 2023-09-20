def gcd(x, y): # 8, 4
    while(y != 0):
        x, y = y, x%y # x = 4 y = 8%4 = 0
    return x # 4, 2

T = int(input())

ring = list(map(int, input().split()))


for i in range(1, len(ring)):
    g = gcd(ring[0], ring[i])
    print("{}/{}".format(ring[0]//g, ring[i]//g)) # 8//4 = 2, 4//4 = 1 
