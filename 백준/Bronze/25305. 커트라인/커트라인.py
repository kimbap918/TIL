N, k = map(int, input().split()) # 응시자의 수 N, 점수가 가장 높은 k명
a = []

score = list(map(int, input().split()))
score.sort(reverse=True)
print(score[k-1])