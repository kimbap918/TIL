N = int(input())  # 학생 수
board = [list(map(int, input().split())) for _ in range(N)]  # 학생의 학년별 반 정보

# 같은 반이었던 횟수를 세기 위한 리스트 초기화
students = [0] * N

# 모든 학생을 비교
for i in range(N):  # 학생 i
    for j in range(N):  # 학생 j
        if i != j:  # 자기 자신은 비교하지 않음
            # 학년별로 같은 반이었던 적이 있는지 확인
            for k in range(5):  # 1학년부터 5학년까지
                if board[i][k] == board[j][k]:
                    students[i] += 1
                    break  # 한 학년에서 같은 반이면 추가 계산 불필요

# 가장 많은 학생들과 같은 반이었던 학생 찾기
max_value = max(students)  # 가장 많은 횟수
leader = students.index(max_value) + 1  # 1번부터 시작하므로 +1

print(leader)
