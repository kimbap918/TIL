max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]
score = list(map(int, input().split()))
total_score, hacker = 0, 0
for i in range(9):
    if score[i] > max_score[i]:
        hacker = 1
    total_score += score[i]
if hacker:
    print("hacker")
else:
    print("draw" if total_score >= 100 else "none")