cnt = 0

while True:
    N = int(input())
    for i in range(2, (N*2)+1):
        check = True
        cnt += 1
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                check = False
                break
        if check:
            if i > N:
                print(i)
    if N == 0:
        break
        

