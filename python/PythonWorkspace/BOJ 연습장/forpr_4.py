# scores를 확인하고 60점 미만인 학생들은 불합격으로 출력되게 작성해 보세요

scores = [15, 50, 60, 70, 52, 75, 101]

for i, score in enumerate(scores):
    i += 1
    if score < 0 or score > 100:
        print("잘못된 점수")
        continue

    if score >= 60:
        print(str(i)+ "번 학생은 합격")
    else:
        print(str(i)+ "번 학생은 불합격")