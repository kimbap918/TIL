h, b, c, s = map(int, input().split())
print('{:.1f} MB'.format(h*b*c*s/8/1024/1024))
