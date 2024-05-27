T = int(input())

for _ in range(T):
    N = int(input())
    if (N + 1) % int(str(N)[2:]) == 0:
        print("Good")
    else:
        print("Bye")
