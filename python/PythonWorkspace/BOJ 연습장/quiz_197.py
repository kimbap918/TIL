from collections import deque
import sys
# 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 
# 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 
# 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
input = sys.stdin.readline
TC = int(input())

for i in range(TC):
    # N: 문서의 개수, M: queue에서 몇번째로 놓여있는지
    # M이 남은 큐 중에서 가장 큰수가 될때까지 검사
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while queue:
        best = max(queue) # 큐의 최고 우선순위값 저장
        front = queue.popleft() # 맨 왼쪽의 값을 뺌
        # print(best, front, M)
        # print(queue)
        M -= 1 # M을 -1 이동

        if best == front: # 뽑은 숫자가 제일 큰 숫자면
            count += 1 # 하나가 배출되었기 때문에 카운트 증가
            if M < 0: 
                print(count) 
                break
        else:
            queue.append(front) # 빼낸 숫자를 맨 뒤에 붙인다
            # print(queue) 
            if M < 0: # 음수로 떨어지면
                M = len(queue)-1 # 큐 길이 -1 