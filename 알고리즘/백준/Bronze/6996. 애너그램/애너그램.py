T = int(input())

for _ in range(T):
    A, B = input().split()
    
    a = sorted(list(A))
    b = sorted(list(B))

    if a == b:
        print("{} & {} are anagrams.".format(A, B))
    else:
        print("{} & {} are NOT anagrams.".format(A, B))


