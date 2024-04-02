def f(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return -1*(abs(a)//abs(b)) if a*b < 0 else a//b

li = list(input().split())
li[0] = int(li[0]); li[2] = int(li[2]); li[4] = int(li[4])
a = f(f(li[0], li[2], li[1]), li[4], li[3])
b = f(li[0], f(li[2], li[4], li[3]), li[1])
print(min(a, b))
print(max(a, b))