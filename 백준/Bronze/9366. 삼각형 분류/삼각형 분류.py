for case in range(int(input())):
    li = sorted(map(int, input().split()))
    print(f"Case #{case+1}: ", end='')
    if li[0]+li[1] <= li[2]:
        print("invalid!")
    elif li[0] == li[1] == li[2]:
        print("equilateral")
    elif li[0]==li[1] or li[1]==li[2] or li[2]==li[0]:
        print("isosceles")
    else:
        print("scalene")