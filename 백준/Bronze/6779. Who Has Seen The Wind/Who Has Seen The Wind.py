h = int(input())
M = int(input())
t = 1
while t <= M :
    A = ((-6) * (t ** 4)) + (h * (t ** 3)) + (2 * (t ** 2)) + t
    if A <= 0 :
        print("The balloon first touches ground at hour:", t)
        exit(0)
    t += 1
print("The balloon does not touch ground in the given time.")