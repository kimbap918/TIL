T = int(input())

for i in range(T):
    a = list(input())
    j = 0
    try:
        while len(a) != 0:
            if a[j] + a[j+1] == "()":
                a.pop(j+1)
                a.pop(j)
                j = 0
            elif a[j] + a[j+1] != "()":
                j += 1
            if len(a) == 0:
                print("YES")
                break    
    except IndexError:
                print("NO")