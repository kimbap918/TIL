for _ in range(int(input())):
    n = int(input())
    p1 = p2 = 0
    for i in range(n):
        a, b = input().split()
        if a == b:
            continue
        elif (a == 'R' and b == 'S') or (a == 'P' and b == 'R') or (a == 'S' and b == 'P'):
            p1 += 1
        else:
            p2 += 1
    if p1 > p2:
        print("Player 1")
    elif p1 < p2:
        print("Player 2")
    else:
        print("TIE")