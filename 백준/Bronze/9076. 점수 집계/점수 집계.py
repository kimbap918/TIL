x = int(input())
for i in range(x):
    points = list(map(int, input().split()))
    points.remove(max(points))
    points.remove(min(points))
    if max(points) - min(points) >= 4:
        print('KIN')
    else:
        print(sum(points))