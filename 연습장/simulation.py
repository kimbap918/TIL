import time

# 플레이어 초기 체력 8,000,000
player_health = 8000000

# 각 물약의 효과와 쿨타임
potion1_heal = 5600000  # 70% 회복
potion1_cooldown = 15
potion2_heal = 5600000  # 70% 회복
potion2_cooldown = 7
potion3_heal = 8000000  # 100% 회복
potion3_cooldown = 1

# 자동 사용 체력 비율 설정
auto_use_percentage = 50

# 물약 사용 여부를 저장하는 변수
potion1_used = False
potion2_used = False
potion3_used = False


# 데미지 적용 함수
def apply_damage():
    global player_health
    player_health -= 8000000 * 0.02  # 200% 데미지 / 10분 = 0.02 * 체력

# 물약 사용 함수
def use_potion(potion_heal, potion_cooldown):
    global player_health
    global potion1_used
    global potion2_used
    global potion3_used
    
    player_health += potion_heal
    if potion_heal == potion3_heal:
        potion3_used = True
    elif potion_heal == potion2_heal:
        potion2_used = True
    else:
        potion1_used = True
    
    time.sleep(potion_cooldown)

# 시뮬레이션 실행
while player_health > 0:
    if player_health < auto_use_percentage / 100 * 8000000:
        if not potion3_used:
            use_potion(potion3_heal, potion3_cooldown)
        elif not potion2_used:
            use_potion(potion2_heal, potion2_cooldown)
        elif not potion1_used:
            use_potion(potion1_heal, potion1_cooldown)
    
    apply_damage()

player_hp = 8000000
potion1_cd = 0
potion2_cd = 0
potion3_cd = 0
potion1_ratio = 20
potion2_ratio = 10
potion3_ratio = 100
potion1_heal = player_hp * 0.7
potion2_heal = player_hp * 0.7
potion3_heal = player_hp
total_dmg = player_hp * 2
dmg_per_sec = total_dmg / 600

start_time = time.time()

while True:
    elapsed_time = time.time() - start_time
    if elapsed_time > 600:
        break
    
    player_hp -= dmg_per_sec * 5
    
    if player_hp <= potion3_heal * (100 - potion3_ratio) / 100 and potion3_cd == 0:
        player_hp += potion3_heal
        potion3_cd = 1
    elif player_hp <= potion2_heal * (100 - potion2_ratio) / 100 and potion2_cd == 0:
        player_hp += potion2_heal
        potion2_cd = 7
    elif player_hp <= potion1_heal * (100 - potion1_ratio) / 100 and potion1_cd == 0:
        player_hp += potion1_heal
        potion1_cd = 15
        
    if potion1_cd > 0:
        potion1_cd -= 1
    if potion2_cd > 0:
        potion2_cd -= 1
    if potion3_cd > 0:
        potion3_cd -= 1


# 각 물약의 사용 여부와 체력 비율 출력
print(f"Potion 1 used: {potion1_used}, Health percentage at use: {potion1_heal / 8000000 * 100}%")
print(f"Potion 2 used: {potion2_used}, Health percentage at use: {potion2_heal / 8000000 * 100}%")
print(f"Potion 3 used: {potion3_used}, Health percentage at use: {potion3_heal / 8000000 * 100}%")
