def h(a) :
    s = 0
    while a//1 != 0 :
        s += (a%10)**2
        a = int(a/10)
    return (s)

a = int(input())

while 1 :
    a = h(a)
    if a == 4 :
        print('UNHAPPY')
        break
    elif a == 1 :
        print('HAPPY')
        break