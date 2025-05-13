import heapq 

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1  # 남은 시간보다 모든 음식의 총 시간이 적다면 종료
    
    # 우선순위 큐(최소 힙)
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  # (남은 음식량, 음식 번호)
    
    sum_value = 0  # 총 소요된 시간
    previous = 0  # 이전 단계에서 소비한 음식량
    length = len(food_times)  # 남은 음식 개수
    
    # 가장 적은 음식부터 순차적으로 제거 (음식이 한 바퀴 도는 횟수 단위로 계산)
    while q and sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]  # 가장 적게 남은 음식량
        sum_value += (now - previous) * length  # 해당 음식만큼 전체 음식이 소비됨
        length -= 1  # 해당 음식을 다 먹었으므로 개수 감소
        previous = now  # 이전 단계 음식량 갱신
    
    # 2. sum_value + ((q[0][0] - previous) * length) <= k
    # 이 조건이 True일 때만 루프가 실행됩니다.

    # (1) q[0][0] - previous (현재 음식에서 이전 음식량을 빼는 부분)
    # q[0][0] : 우선순위 큐의 최소값(가장 적게 남은 음식량) 을 의미합니다.
    # previous : 이전까지 제거한 음식의 양을 저장해둔 값입니다.
    # q[0][0] - previous : 현재 최소 음식량에서 이전에 제거된 음식량을 뺀 값으로,
    # 예를 들어, q[0][0] = 3, previous = 2라면 → 3 - 2 = 1
    # 즉, 현재 단계에서 "새롭게" 먹어야 하는 양을 의미합니다.
    # (2) (q[0][0] - previous) * length
    # 현재 음식에서 이전 음식량을 제외한 부분을 남아 있는 음식 개수만큼 곱함.
    # 즉, 한 바퀴 돌면서 모든 음식을 한 번씩 먹는 데 걸리는 총 시간을 계산하는 과정입니다.
    # 예제:
    # 음식이 3개 남아 있고, q[0][0] - previous = 2라면,
    # → 한 바퀴 돌며 각 음식에서 2씩 줄이는 데 걸리는 시간은 2 × 3 = 6초.
    # (3) sum_value + ((q[0][0] - previous) * length) <= k
    # sum_value : 지금까지 걸린 총 시간.
    # (q[0][0] - previous) * length : 이번 단계에서 모든 음식을 한 바퀴 돌며 먹는 데 필요한 시간.
    # sum_value + ((q[0][0] - previous) * length) <= k :
    # → 현재까지 걸린 시간 + 새롭게 걸릴 시간이 k 이내라면 루프 계속 진행!
    # → k를 초과하면 루프 종료!


    # 남은 음식들을 원래 음식 번호 기준으로 정렬
    res = sorted(q, key=lambda x: x[1])  # 음식 번호 기준 정렬
    
    # (k - sum_value)번째 음식을 찾음 (나머지 연산을 활용)
    return res[(k - sum_value) % length][1]