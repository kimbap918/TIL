import time

player_max_health = 8000000  # 플레이어의 최대 체력
player_health = player_max_health  # 플레이어의 초기 체력
potion_1_health_ratio = int(input("첫번째 물약 체력 설정 비율(1~100): "))
potion_1_cooldown = 15  # 첫번째 물약의 재사용 대기시간 (초)
potion_2_health_ratio = int(input("두번째 물약 체력 설정 비율(1~100): "))
potion_2_cooldown = 15  # 두번째 물약의 재사용 대기시간 (초)
potion_3_health_ratio = int(input("세번째 물약 체력 설정 비율(1~100): "))
potion_3_cooldown = 1  # 세번째 물약의 재사용 대기시간 (초)
resurrection_threshold = 0.5  # 체력 부활 임계치
resurrection_duration = 5  # 체력 부활 시간 (초)
simulation_duration = 10 * 60  # 시뮬레이션 진행 시간 (10분)

potion_1_count = 0  # 첫번째 물약 사용 횟수
potion_2_count = 0  # 두번째 물약 사용 횟수
potion_3_count = 0  # 세번째 물약 사용 횟수

damage_interval = 2  # 데미지 입는 간격 (초)
damage_amount_ratio = 0.6  # 데미지 비율

def use_potion(potion_index, cooldown):
    global player_health
    global potion_1_count, potion_2_count, potion_3_count

    if potion_index == 1:
        potion_health_ratio = potion_1_health_ratio
        potion_1_count += 1
    elif potion_index == 2:
        potion_health_ratio = potion_2_health_ratio
        potion_2_count += 1
    elif potion_index == 3:
        potion_health_ratio = potion_3_health_ratio
        potion_3_count += 1

    heal_amount = player_max_health * (potion_health_ratio / 100)
    player_health = min(player_health + heal_amount, player_max_health)  # 체력 회복 후 최대 체력 체크
    print(f"물약 사용: 플레이어 체력 {player_health}, 물약 종류: {potion_index}")
    time.sleep(cooldown)  # 물약 재사용 대기시간만큼 대기

def simulate_game():
    global player_health
    start_time = time.time()  # 시뮬레이션 시작 시간
    damage_timer = 0  # 데미지 입는 타이머
    count = 0  # 체력 부활 횟수
    while time.time() - start_time < simulation_duration:
        if player_health <= 0:  # 플레이어 체력이 0 이하인 경우
            print(f"체력 부활: 플레이어 체력 {player_health}")
            count += 1
            player_health = player_max_health * resurrection_threshold  # 체력 부활 후 임계치 설정
            time.sleep(resurrection_duration)  # 체력 부활 시간만큼 대기
        else:
            # 물약 사용
            if player_health <= player_max_health * (potion_1_health_ratio / 100):
                use_potion(1, potion_1_cooldown)
            if player_health <= player_max_health * (potion_2_health_ratio / 100):
                use_potion(2, potion_2_cooldown)
            if player_health <= player_max_health * (potion_3_health_ratio / 100):
                use_potion(3, potion_3_cooldown)

        # 데미지 입기
        if time.time() - damage_timer >= damage_interval:
            damage_timer = time.time()
            damage_amount = player_health * damage_amount_ratio
            player_health = max(player_health - damage_amount, 0)
            print(f"데미지 입음: 플레이어 체력 {player_health}")

        # 체력바 표시
        health_percentage = (player_health / player_max_health) * 100
        health_bar = "#" * int(health_percentage // 5)
        print(f"체력바: [{health_bar}] {health_percentage:.2f}%")

    print(f"시뮬레이션 종료: 총 부활 횟수 {count}")
    print(f"첫번째 물약 사용 횟수: {potion_1_count}")
    print(f"두번째 물약 사용 횟수: {potion_2_count}")
    print(f"세번째 물약 사용 횟수: {potion_3_count}")

simulate_game()
