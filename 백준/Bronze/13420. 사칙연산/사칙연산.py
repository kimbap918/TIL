for _ in range(int(input())):
    li = input().split()
    a, b, c = int(li[0]), int(li[2]), int(li[4])
    op = li[1]
    if op == '+':
        t = a+b
    elif op == '-':
        t = a-b
    elif op == '*':
        t = a*b
    elif op == '/':
        t = a//b
    print("correct" if t == c else "wrong answer")