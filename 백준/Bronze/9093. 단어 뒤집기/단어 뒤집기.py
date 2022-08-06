T = int(input())

for i in range(T):
    string = list(input().split())
    for j in string:
        print(j[::-1], end = ' ')