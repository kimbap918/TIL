N = int(input())
x1, y1 = map(int, input().split())  # Mary의 최소, 최대
x2, y2 = map(int, input().split())  # Marty의 최소, 최대

sushi = []
total = 0
for _ in range(N):
    m = int(input())
    sushi.append(m)
    total += m

# 전체 스시 개수가 두 사람이 먹을 수 있는 범위를 벗어나는지 확인
if total < x1 + x2 or total > y1 + y2:
    print("No")
else:
    # 각 타입의 스시에 대해 최소로 나눠야 하는 개수 계산
    mary_min = sum(m // 2 for m in sushi)  # 각 종류별 절반의 합
    marty_min = mary_min

    # 남은 홀수 개의 스시들의 합
    extra = sum(m % 2 for m in sushi)
    
    # Mary가 받을 수 있는 최소값과 최대값 범위 체크
    mary_possible_min = mary_min
    mary_possible_max = mary_min + extra
    
    # Mary와 Marty 모두가 조건을 만족하는지 확인
    if (x1 <= mary_possible_max and mary_possible_min <= y1 and 
        x2 <= total - mary_possible_min and total - mary_possible_max <= y2):
        print("Yes")
    else:
        print("No")