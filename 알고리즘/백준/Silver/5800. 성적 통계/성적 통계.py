cls = int(input())

for _ in range(1, cls+1):
    math = list(map(int, input().split()))
    students = math[1:]
    a = sorted(students)
    gap = 0

    for i in range(len(a)-1):
        if a[i+1] - a[i] > gap:
            gap = a[i+1] - a[i]
    print("Class {}".format(_))
    print("Max {}, Min {}, Largest gap {}".format(max(a), min(a), gap))
