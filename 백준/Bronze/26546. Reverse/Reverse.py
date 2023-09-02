for _ in range(int(input())) :
    s, i, j = input().split()
    for x in range(int(i)) :
        print(s[x], end = "")
    for x in range(int(j), len(s)) :
        print(s[x], end = "")
    print()