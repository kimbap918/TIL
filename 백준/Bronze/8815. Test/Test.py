for _ in range(int(input())):
    n = int(input())
    s = "BCBCDCDADABA"
    print('A' if n == 1 else s[(n-2)%12])