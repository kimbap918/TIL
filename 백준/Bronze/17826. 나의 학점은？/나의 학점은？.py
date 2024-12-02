GPA = []
GPA += ['A+'] * 5
GPA += ['A0'] * 10
GPA += ['B+'] * 15
GPA += ['B0'] * 5
GPA += ['C+'] * 10
GPA += ['C0'] * 3
GPA += ['F'] * 2

score_list = list(map(int, input().split()))
hong = int(input())
print(GPA[score_list.index(hong)])