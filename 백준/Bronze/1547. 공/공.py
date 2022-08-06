M = int(input())
a = [0, 'ball', 'not', 'not']
for i in range(M):
    X, Y = map(int, input().split())
    temp = 0
    temp = a[X] # 2
    a[X] = a[Y] # x = 3
    a[Y] = temp # y = 2

if 'ball' not in a:
    print(-1)
else: 
    print(a.index('ball'))

    
