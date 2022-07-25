N = int(input())

for i in range(N):
    if i % 2 == 0:
        print("* "*N, end='')
    else:
        print("\n "+"* "*N)