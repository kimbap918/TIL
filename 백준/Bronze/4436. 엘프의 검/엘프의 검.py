import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break

    appear = [False] * 10

    rest = 10
    S = k = 0

    while rest:
        k += 1
        S += n
        q = S
        while q:
            q, r = divmod(q, 10)
            if not appear[r]: 
                appear[r] = True
                rest -= 1
                if not rest: 
                    break
    print(k)