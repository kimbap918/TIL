

## 파이썬 알고리즘 수업 - 너비 우선 탐색 1(BOJ 24444)

<br>

## 문제

오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

*N*개의 정점과 *M*개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 *N*번이고 모든 간선의 가중치는 1이다. 정점 *R*에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 **오름차순**으로 방문한다.

```
bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    for each v ∈ V - {R}
        visited[v] <- NO;
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
    while (Q ≠ ∅) {
        u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
        for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
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

## 📝 풀어보기 

이번 문제도 최대한 의사코드와 비슷하게 풀어봤다.

<br>

정점의 수 N, 간선의 수 M, 시작 정점 R을 입력받는다.

정점의 집합 E 에 N+1만큼 빈 공간을 만들어 저장해둔다. 여기에는 간선의 정보 u, v가 저장된다.

방문 여부를 확인하기 위해 visited에 [0]을 N+1만큼 생성해서 저장하고 cnt에 1을 저장해둔다. 

``` python
import sys
from collections import deque
input = sys.stdin.readline
N, M, R = map(int, input().split())
E = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1
```

<br>

M만큼 반복하면서 간선정보 u,v를 입력받고 E에 저장해둔다.

```python
for i in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)
```

<br>

dfs를 구현한다.

여기서 R은 시작 정점이다. deque를 만들어 시작정점 R을 저장해둔다.

visited[R] 은 시작점이므로 여기에 1을 저장해둔다.

Q의 가장 왼쪽의 값을 빼내고, u에 저장해둔다.

간선정보가 담긴 E를 오름차순으로 정렬하고 E[u]를 순회하면서 방문이 되지 않은곳을 탐색하면 cnt를 올리면서 해당 값을 visited에 저장하고, Q에도 순회중인 E[u]의 값 i를 저장한다.

```python
def bfs(E, R, visited):
    global cnt
    # 시작지점이 들어감 
    Q = deque([R])
    # 시작 정점 방문 표시
    visited[R] = 1
    while Q:
        u = Q.popleft()
        E[u].sort()
        for i in E[u]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                Q.append(i)

bfs(E, R, visited)
```

<br>

visited의 1번째 인덱스부터 출력한다.

```python
for i in visited[1:]:
    print(i)
```

<br>

#### 전체코드

``` python
import sys
from collections import deque
input = sys.stdin.readline
N, M, R = map(int, input().split())
E = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for i in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)


def bfs(E, R, visited):
    global cnt
    # 시작지점이 들어감 
    Q = deque([R])
    # 시작 정점 방문 표시
    visited[R] = 1
    while Q:
        u = Q.popleft()
        E[u].sort()
        for i in E[u]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                Q.append(i)

bfs(E, R, visited)

for i in visited[1:]:
    print(i)
```

