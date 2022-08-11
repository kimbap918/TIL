n = int(input()) # 사람의 수
start, end = list(map(int, input().split())) # 촌수를 계산할 두 사람
m = int(input()) # 관계(간선)의 수
# 빈 리스트를 (n+1)개를 가진 이차원 리스트
# _ : 값을 사용하지 않겠다는 의미
# n+1을 하는 이유, 촌수가 1부터 시작하기 때문에
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # 부모 자식 관계
    x, y = list(map(int, input().split()))
    # 무방향 인접 그래프 생성
    graph[x].append(y)
    graph[y].append(x)

# 방문 표시를 할 리스트
visited = [False] * (n + 1)

# DFS를 시작하기위해서 기본값 설정
# 스택에 값을 추가할 때 촌수도 같이 추가한다.
# stack = [start]
stack = []
stack.append([start, 0])
visited[start] = True

# 정답을 출력할 변수
answer = -1 

while len(stack) != 0 : # 스택이 비어있지 않으면 반복
    # LIFO, 스택의 가장 위에 있는 값을 저장
    # 번호와 촌수를 같이 pop
    number, count = stack.pop()
    # pop을 한 값이 우리가 원하는 값(end)
    # 촌수가 연결이 안되어있으면 line 35~37 실행 x
    if number == end:
        answer = count
        break
    # 해당하는 값의 인접 그래프를 저장
    adj_graph = graph[number]
    # 인접하는 값들을 탐색 
    for adj_number in adj_graph:
        if not visited[adj_number]:
            # 인접 번호와 촌수+1를 같이 push
            stack.append([adj_number, count + 1])
            visited[adj_number] = True

# 촌수 출력
print(answer)