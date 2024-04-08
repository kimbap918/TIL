level = list(map(int, input().split()))
n = int(input())
grades = []
for i in range(n):
    grade = 0
    for j in range(3):
        a = list(map(int, input().split()))
        for k in range(3):
            grade += a[k] * level[k]
    grades.append(grade)
print(max(grades))