k = int(input())
n = int(input())
time = 0
for _ in range(n):
    t, z = input().split()
    t = int(t)
    time += t
    if time >= 210:
        print(k)
        break
    if z == 'T':
        k = (k+1)%9
        if k == 0:
            k += 1