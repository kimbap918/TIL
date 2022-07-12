d = 1
a, b, c = map(int, input().split())
while d%a != 0 or d%b != 0 or d%c != 0:
    d+=1
print(d)
