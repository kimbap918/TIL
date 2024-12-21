# 20 30 50 48 33 66 0 64
scores = [int(input()) for i in range(8)]

# 66, 64, 50, 48, 33, 30, 20, 0
sorted_scores = sorted(scores, reverse=True)
res = sum(sorted_scores[:5])
res_arr = []

for i in range(len(sorted_scores[:5])):
    if sorted_scores[i] in scores:
        res_arr.append(scores.index(sorted_scores[i])+1)


print(res)
for i in sorted(res_arr):
    print(i, end=' ')