def calculate_reward(dice):
    from collections import Counter
    count = Counter(dice)
    sorted_count = sorted(count.items(), key=lambda x: (-x[1], -x[0]))
    
    if sorted_count[0][1] == 4:
        return 50000 + sorted_count[0][0] * 5000
    elif sorted_count[0][1] == 3:
        return 10000 + sorted_count[0][0] * 1000
    elif sorted_count[0][1] == 2:
        if sorted_count[1][1] == 2:
            return 2000 + sorted_count[0][0] * 500 + sorted_count[1][0] * 500
        else:
            return 1000 + sorted_count[0][0] * 100
    else:
        return max(dice) * 100

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    max_reward = 0
    
    for i in range(N):
        dice = list(map(int, data[1 + 4*i : 5 + 4*i]))
        reward = calculate_reward(dice)
        if reward > max_reward:
            max_reward = reward
    
    print(max_reward)

if __name__ == "__main__":
    main()