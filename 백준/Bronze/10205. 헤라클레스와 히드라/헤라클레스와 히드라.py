for n in range(1, int(input()) + 1) :
    h = int(input())
    for i in input() :
        if i == "c" : h += 1
        else : h -= 1
    print(f"Data Set {n}:\n{h}\n")
