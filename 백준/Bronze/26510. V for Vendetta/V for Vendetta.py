N = list(map(int, input().split()))

for i in range(len(N)): # N번 반복
    num = N[i]
    
    for j in range(num, 0, -1):
        if j == 1:
            print(" " * (num-1) + "*")
        else:
            print(" " * (num-j) + "*" + " " * (2*j-3)+ "*")
