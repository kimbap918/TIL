import random
import time

# 플레이어 초기 상태 설정
player_max_hp = 8000000
player_hp = player_max_hp
revive_threshold = 0.5
revive_time = 5

# 물약 초기 상태 설정
potion_A = {
    'heal_percentage': 0.7,
    'cooldown': 15,
    'last_used_time': -float('inf')
}

potion_B = {
    'heal_percentage': 0.7,
    'cooldown': 15,
    'last_used_time': -float('inf')
}

potion_C = {
    'heal_percentage': 0.9,
    'cooldown': 1,
    'last_used_time': -float('inf')
}

# 사용자 입력으로 체력 회복 비율 설정
potion_A_ratio = float(input("물약 A의 체력 회복 비율을 입력하세요 (1% ~ 100%): ")) / 100
potion_B_ratio = float(input("물약 B의 체력 회복 비율을 입력하세요 (1% ~ 100%): ")) / 100
potion_C_ratio = float(input("물약 C의 체력 회복 비율을 입력하세요 (1% ~ 100%): ")) / 100

# 시뮬레이션 실행
start_time = time.time()
elapsed_time = 0
potion_A_count = 0
potion_B_count = 0
potion_C_count = 0
is_reviving = False
revive_start_time = 0

while elapsed_time <= 20:
    # 체력 감소 및 부활 처리
    if not is_reviving:
        if player_hp > 0:
            damage_per_tick = (random.uniform(0.1, 0.7) * player_max_hp) / 10
            for _ in range(10):
                player_hp -= damage_per_tick
                if player_hp < 0:
                    player_hp = 0
                    is_reviving = True
                    revive_start_time = time.time()
                    print(f"체력 부활! {revive_time}초 동안 무적 상태입니다.")
                    break
                else:
                    print(f"플레이어가 입고 있는 데미지: {damage_per_tick:.2f}")
                time.sleep(0.3)  # 0.3초 딜레이

    else:
        if time.time() - revive_start_time >= revive_time:
            is_reviving = False

    # 물약 사용 가능한지 체크 및 사용
    if player_hp <= player_max_hp * (1 - potion_A_ratio) and not is_reviving:
        if time.time() - potion_A['last_used_time'] >= potion_A['cooldown']:
            heal_amount = min(player_max_hp - player_hp, potion_A['heal_percentage'] * player_max_hp - player_hp)
            player_hp += heal_amount
            potion_A['last_used_time'] = time.time()
            potion_A_count += 1
            print(f"물약 A를 사용했습니다. 회복량: {heal_amount:.2f}, 현재 체력: {player_hp:.2f}/{player_max_hp:.2f}")

    if player_hp <= player_max_hp * (1 - potion_B_ratio) and not is_reviving:
        if time.time() - potion_B['last_used_time'] >= potion_B['cooldown']:
            heal_amount = min(player_max_hp - player_hp, potion_B['heal_percentage'] * player_max_hp - player_hp)
            player_hp += heal_amount
            potion_B['last_used_time'] = time.time()
            potion_B_count += 1
            print(f"물약 B를 사용했습니다. 회복량: {heal_amount:.2f}, 현재 체력: {player_hp:.2f}/{player_max_hp:.2f}")

    if player_hp <= player_max_hp * (1 - potion_C_ratio) and not is_reviving:
        if time.time() - potion_C['last_used_time'] >= potion_C['cooldown']:
            heal_amount = min(player_max_hp - player_hp, potion_C['heal_percentage'] * player_max_hp - player_hp)
            player_hp += heal_amount
            potion_C['last_used_time'] = time.time()
            potion_C_count += 1
            print(f"물약 C를 사용했습니다. 회복량: {heal_amount:.2f}, 현재 체력: {player_hp:.2f}/{player_max_hp:.2f}")

    elapsed_time = time.time() - start_time

# 결과 출력
print(f"물약 A 사용 횟수: {potion_A_count}")
print(f"물약 B 사용 횟수: {potion_B_count}")
print(f"물약 C 사용 횟수: {potion_C_count}")
