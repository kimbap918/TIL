while 1:
    a, b = input().split()
    if a == b == '0':
        break
    if len(a) > len(b):
        b = (len(a)-len(b))*'0' + b
    else:
        a = (len(b)-len(a))*'0' + a
    cnt = carry = 0
    for i in range(len(a)-1, -1, -1):
        if int(a[i]) + int(b[i]) + carry >= 10:
            cnt += 1
            carry = 1
        else:
            carry = 0
    print(cnt)