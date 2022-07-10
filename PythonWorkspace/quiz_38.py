C = int(input()) # 테스트 케이스
A = 0
B = 0
D = []
E = 0

for i in range(C):
    students_list = list(map(int,input().split())) # 학생 리스트 생성 
    for j in range(1, len(students_list)): 
        A += students_list[j] # A 에 학생 성적 누적
    B = A / (len(students_list)-1) # 성적 / 학생 수 = 평균

    for j in range(1, len(students_list)):
        if students_list[j] > B: # 평균보다 높은 학생 뽑기
            D.append(students_list[j]) # 평균보다 높은 학생 넣기
            E = (len(D) / (len(students_list)-1)) * 100 # 반에서 평균보다 높은 학생 비율
    print("{0:.3f}%".format(E)) # 출력
    A = 0 # 초기화
    B = 0
    D = []
    E = 0

