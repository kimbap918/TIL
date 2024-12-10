def count_magical_numbers(N):
    # 자릿수 합을 미리 계산
    digit_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        digit_sum[i] = digit_sum[i // 10] + (i % 10)

    # 신기한 수를 셈
    count = 0
    for i in range(1, N + 1):
        if i % digit_sum[i] == 0:
            count += 1

    return count

# 입력 및 실행
N = int(input())
print(count_magical_numbers(N))
