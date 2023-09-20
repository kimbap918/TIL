from collections import deque
queue = deque()
rm = []

N, K = map(int, input().split())

for i in range(1, N+1):
    queue.append(i)

while queue:
    # K번째의 숫자를 가장 앞으로 이동
    queue.rotate(-(K-1))
    # print(queue)
    # 가장 앞의 숫자를 빼냄
    rm.append(queue.popleft())
    # print(rm)
print('<'+', '.join(map(str, rm))+'>')
