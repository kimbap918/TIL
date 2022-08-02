S = [
    "baekjoononlinejudge", "startlink", 
    "codeplus", "sundaycoding"
]

words = [
    "baekjoon", "codeplus", "codeminus", "startlink", "starlink",
    "sundaycoding", "codinghs", "sondaycoding"
]

# 풀이 1
cnt = 0

for word in words:
    if word in S:
        cnt += 1

print(cnt)

# 풀이 2
print(len(set(words) & set(S)))
