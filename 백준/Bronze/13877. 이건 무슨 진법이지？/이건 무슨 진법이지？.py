for _ in range(int(input())):
    i, n = input().split()
    o = int(n, 8) if max(list(n)) < '8' else 0
    print(int(i), o, int(n), int(n, 16))