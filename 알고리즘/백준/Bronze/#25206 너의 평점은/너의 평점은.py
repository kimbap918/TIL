# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합
grade_table = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0, 'P':0.0}
grade_total = 0
point_total = 0

for i in range(20):
    name, point, grade = map(str, input().split())
    if grade != 'P':
        point_total += float(point)
        grade_total += grade_table[grade] * float(point)
    # print(point, grade_table[grade], grade_total)
print('%.6f' % (grade_total/point_total))

