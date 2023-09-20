from collections import deque

def bfs(adjacency_list, cow):
    visited = set()  # 방문한 소들을 저장할 집합
    visited.add(cow)  # 소 방문 표시

    queue = deque([cow])  # 소를 큐에 추가

    while queue:
        current_cow = queue.popleft()  # 큐에서 소 하나를 꺼냄

        # 현재 소와 연결된 소들을 탐색
        for neighbor in adjacency_list[current_cow]:
            if neighbor not in visited:
                visited.add(neighbor)  # 소 방문 표시
                queue.append(neighbor)  # 연결된 소를 큐에 추가

    return visited

def find_misbehaving_cows(N, M, connections):
    adjacency_list = [[] for _ in range(N+1)]  # 인접 리스트 생성

    # 인접 리스트 구성
    for c1, c2 in connections:
        adjacency_list[c1].append(c2)
        adjacency_list[c2].append(c1)

    visited = bfs(adjacency_list, 1)  # BFS 탐색 시작

    misbehaving_cows = []
    for cow in range(2, N+1):
        if cow not in visited:
            misbehaving_cows.append(cow)

    return misbehaving_cows

# 입력 받기
N, M = map(int, input().split())
connections = []
for _ in range(M):
    c1, c2 = map(int, input().split())
    connections.append((c1, c2))

# 결과 출력
result = find_misbehaving_cows(N, M, connections)
if result:
    for cow in result:
        print(cow)
else:
    print(0)
