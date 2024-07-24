R, C = map(int, input().split())
A, B = map(int, input().split())

li = []
t1, t2 = '', ''
for i in range(C):
    if i % 2:
        t1 += '.'*B
    else:
        t1 += 'X'*B
    if i % 2:
        t2 += 'X'*B
    else:
        t2 += '.'*B
for i in range(R):
    if i % 2:
        for _ in range(A):
            print(t2)
    else:
        for _ in range(A):
            print(t1)