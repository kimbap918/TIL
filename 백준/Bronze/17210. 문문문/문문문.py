N = int(input())
a = int(input())
if N <= 5:
    for i in range(N-1):
        a = int(not a)
        print(a)
else:
    print("Love is open door")