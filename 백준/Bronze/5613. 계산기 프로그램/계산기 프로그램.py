res = int(input())
while 1:
    op = input()
    if op == '=':
        break
    n = int(input())
    if op == '+': res += n;
    elif op == '-': res -= n;
    elif op == '*': res *= n;
    elif op == '/': res //= n;
print(res)