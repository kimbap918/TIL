def setEggplant(x):
    for e in x:
        check = set(e)
        if len(check) == 1:
            return True


eggplant1 = [input().split() for _ in range(10)]
eggplant2 = list(zip(*eggplant1))

result1, result2 = setEggplant(eggplant1), setEggplant(eggplant2)

if result1 or result2:
    print(1)
else:
    print(0)