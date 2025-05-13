N, mood = map(int, input().split())

# 기분이 좋은날(0)의 다음날도 좋은날일 확률, 다음날은 기분이 싫은날일 확률,
# 기분이 싫은날(1)의 다음날은 좋은날일 확률, 다음날도 기분이 싫은날일 확률 
good_to_good, good_to_bad, bad_to_good, bad_to_bad = map(float, input().split())
# 0.70 0.30 0.50 0.50


# N일 뒤에
# 기분이 좋은 날일 확률과 싫은 날일 확률에 1,000을 곱해 
# 소수점 첫째자리에서 반올림한 수를 차례대로 출력
# "N일 뒤의 재현이의 기분이 좋은 날일 확률과 싫은 날일 확률에 1,000을 곱해 소수점 첫째자리에서 반올림한 수를 차례대로 출력한다
# 2 1 
# day 1
# 0.50 0.50

# day 2
# (0.7 / 2)+(0.5 / 2), (0.3 / 2)+(0.5 / 2)

# good : 0.7, 0.3 good_to_good, good_to_bad
# bad : 0.5 0.5  bad_to_good, bad_to_bad

# 마코프 체인 (Markov Chain)
if mood == 0:
    good_prob, bad_prob = 1.0, 0.0
else:
    good_prob, bad_prob = 0.0, 1.0

for _ in range(N): # N일동안 반복
    new_good_prob = good_prob * good_to_good + bad_prob * bad_to_good
    new_bad_prob = good_prob * good_to_bad + bad_prob * bad_to_bad

    good_prob, bad_prob = new_good_prob, new_bad_prob

print(int(round(good_prob*1000, 1)), int(round(bad_prob*1000, 1)))
