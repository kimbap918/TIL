def calculate_delivery_time(start_time, end_time, N, T):
    # 출근 시간과 퇴근 시간 파싱
    start_h, start_m = map(int, start_time.split(':'))
    end_h, end_m = map(int, end_time.split(':'))
    
    # 출근 및 퇴근 시간을 분 단위로 변환
    start_minutes = start_h * 60 + start_m
    end_minutes = end_h * 60 + end_m
    work_minutes = end_minutes - start_minutes  # 하루 근무 시간

    # 총 배달 소요 시간 (N개의 이전 배송 시간 + 브실이의 택배 시간)
    total_time = N * T + T

    # 며칠이 소요되는지 계산
    days = 0
    remaining_time = total_time

    # 근무 시간 초과 처리
    while remaining_time > work_minutes:
        remaining_time -= work_minutes
        days += 1

    # 브실이 택배 도착 시각 계산
    final_minutes = start_minutes + remaining_time  # 출근 시각 기준으로 누적 시간 계산
    if final_minutes >= end_minutes:  # 퇴근 시간을 초과하면 초과 시간 처리
        days += 1
        excess_time = final_minutes - end_minutes  # 초과된 시간
        final_minutes = start_minutes + excess_time  # 초과 시간을 다음 날 출근 시간부터 계산

    # 최종 도착 시각 계산
    final_h = final_minutes // 60
    final_m = final_minutes % 60

    return days, f"{final_h:02}:{final_m:02}"

# 입력
start_time, end_time = "07:30", "12:30"
N, T = 100, 42

# 결과 계산
days, delivery_time = calculate_delivery_time(start_time, end_time, N, T)

# 출력
print(days)
print(delivery_time)
