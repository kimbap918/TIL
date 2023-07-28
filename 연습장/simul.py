import random

def enhance_item():
    cost = 0
    level = 1
    enhance_count = 0
    
    while level <= 30:
        if level <= 10:
            success = True
        elif level <= 20:
            success = random.random() <= 0.7
        else:
            success = random.random() <= 0.6
        
        if success:
            level += 1
        else:
            if level <= 20:
                level = 10
            else:
                level = 20
            cost += 200000000
        
        enhance_count += 1
        
        if level == 30:
            break
    
    return enhance_count, cost

def simulate_enhancement(num_simulations):
    total_enhance_count = 0
    total_cost = 0
    success_count = 0
    
    for _ in range(num_simulations):
        enhance_count, cost = enhance_item()
        total_enhance_count += enhance_count
        total_cost += cost
        success_count += 1 if cost == 0 else 0
    
    success_rate = success_count / num_simulations * 100
    average_enhance_count = total_enhance_count / num_simulations
    average_cost = total_cost / num_simulations
    
    return success_rate, average_enhance_count, average_cost

if __name__ == "__main__":
    num_simulations = 10000  # 시뮬레이션 횟수 설정
    success_rate, average_enhance_count, average_cost = simulate_enhancement(num_simulations)
    
    print(f"시뮬레이션 횟수: {num_simulations}")
    print(f"강화 성공 확률: {success_rate:.2f}%")
    print(f"평균 강화 횟수: {average_enhance_count:.2f} 회")
    print(f"평균 비용: {average_cost:,} 원")
