n = int(input())
result = 0
for i in range(n):
    t = input()
    for j in range(len(t)):
        if t[j] == "U":
            result += 1
        else:
            break
    print(result)
    result = 0