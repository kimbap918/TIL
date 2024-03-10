s = 0
for _ in range(int(input())):
    s += sum(list(map(int, input().split())))
print(s)