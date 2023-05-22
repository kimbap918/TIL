from collections import Counter

N, M = map(int, input().split())
event_cnt = Counter()

for _ in range(M):
    events = list(map(int, input().split()))
    event_cnt.update(events[1:])

# 빈도가 가장 높은 카운트를 저장
most_frequent_cnt = max(event_cnt.values())

# event_cnt에서 빈도가 가장 높은 이벤트를 저장
most_frequent_events = [event for event, count in event_cnt.items() if count == most_frequent_cnt]
# 숫자가 높은 순으로 정렬
most_frequent_events.sort(reverse=True)

print(" ".join(map(str, most_frequent_events)))
