from math import comb

total_options = 18
valid_options = 4

# 확률 계산
probability = comb(valid_options, valid_options) / sum(comb(total_options, i) for i in range(valid_options + 1))

# 퍼센트로 변환
probability_percentage = probability * 100

print(f"한 번의 시도에서 4개의 유효한 옵션이 전부 나올 확률은 약 {probability_percentage:.2f}%입니다.")