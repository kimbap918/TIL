

## 파이썬 알고리즘 수업 - 너비 우선 탐색 2(BOJ 24445)

<br>

## 문제

오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

*N*개의 정점과 *M*개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 *N*번이고 모든 간선의 가중치는 1이다. 정점 *R*에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 **내림차순**으로 방문한다.

```
bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    for each v ∈ V - {R}
        visited[v] <- NO;
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
    while (Q ≠ ∅) {
        u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
        for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
            if (visited[v] = NO) then {
                visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
                enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
            }
    }
}
```

<br>

## 입력

첫째 줄에 정점의 수 *N* (5 ≤ *N* ≤ 100,000), 간선의 수 *M* (1 ≤ *M* ≤ 200,000), 시작 정점 *R* (1 ≤ *R* ≤ *N*)이 주어진다.

다음 *M*개 줄에 간선 정보 `*u* *v*`가 주어지며 정점 *u*와 정점 *v*의 가중치 1인 양방향 간선을 나타낸다. (1 ≤ *u* < *v* ≤ *N*, *u* ≠ *v*) 모든 간선의 (*u*, *v*) 쌍의 값은 서로 다르다.

<br>

## 출력

첫째 줄부터 *N*개의 줄에 정수를 한 개씩 출력한다. *i*번째 줄에는 정점 *i*의 방문 순서를 출력한다. 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.

<br>

## 예제 입력 1 

```
5 5 1
1 4
1 2
2 3
2 4
3 4
```

## 예제 출력 1 

```
1
3
4
2
0
```

정점 1번에서 정점 4번, 정점 2번을 순서대로 방문한다. 정점 4번에서 정점 3번을 방문한다. 정점 5번은 정점 1번에서 방문할 수 없다.

<br>

## 📝 풀어보기 

알고리즘 수업 - 너비 우선 탐색(BOJ 24444)에서 인접 정점이 내림차순으로 바뀐 문제다.

#### 전체코드

``` python
import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
E = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

def bfs(E, R, visited):
    global cnt
    Q = deque([R])
    visited[R] = 1
    while Q:
        u = Q.popleft()
        E[u].sort(reverse=True)
        for i in E[u]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                Q.append(i)


bfs(E, R, visited)

for i in visited[1:]:
    print(i)
```

