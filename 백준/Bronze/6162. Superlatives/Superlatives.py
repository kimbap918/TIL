for i in range(1, int(input()) + 1) :
    print(f"Data Set {i}:")
    A, E = map(int, input().split())
    if E >= A : print("no drought")
    else :
        mega = A / E
        n = 0
        while mega > 1 :
            mega /= 5
            n += 1
        print("mega " * (n - 1) + "drought")
    print()