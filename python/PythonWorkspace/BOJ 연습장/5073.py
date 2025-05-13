

while True:

    one, two, three = map(int, input().split())

    if one == 0 and two == 0 and three == 0:
        break

    total = sum((one, two, three))
    tri_max = max(one, two, three)

    if total - tri_max <= tri_max:
        print("Invalid")
    elif one == two and two == three:
        print("Equilateral")
    elif one == two or two == three or one == three:
        print("Isosceles")
    else:
        print("Scalene")


