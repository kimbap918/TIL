

## 파이썬 알고리즘 수업 - 깊이 우선 탐색 3(BOJ 24481)

<br>

## 문제

오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

*N*개의 정점과 *M*개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 *N*번이고 모든 간선의 가중치는 1이다. 정점 *R*에서 시작하여 깊이 우선 탐색으로 만들어 지는 트리를 깊이 우선 탐색 트리라고 하자. 깊이 우선 탐색 트리에 있는 모든 노드의 깊이(depth)를 출력하자. 시작 정점 *R*의 깊이는 0이고 방문 되지 않는 노드의 깊이는 -1로 출력하자.

깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 **오름차순**으로 방문한다.

```
dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
```

<br>

## 입력

첫째 줄에 정점의 수 *N* (5 ≤ *N* ≤ 100,000), 간선의 수 *M* (1 ≤ *M* ≤ 200,000), 시작 정점 *R* (1 ≤ *R* ≤ *N*)이 주어진다.

다음 *M*개 줄에 간선 정보 `*u* *v*`가 주어지며 정점 *u*와 정점 *v*의 가중치 1인 양방향 간선을 나타낸다. (1 ≤ *u* < *v* ≤ *N*, *u* ≠ *v*) 모든 간선의 (*u*, *v*) 쌍의 값은 서로 다르다.

<br>

## 출력

첫째 줄부터 *N*개의 줄에 정수를 한 개씩 출력한다. *i*번째 줄에는 정점 *i*의 깊이를 출력한다. 시작 정점 *R*의 깊이는 0이고 방문 되지 않는 노드의 깊이는 -1로 출력하자.

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
0
1
2
3
-1
```

깊이 우선 탐색 트리는 1, 2, 3, 4번 노드로 구성된다. 1번 노드가 루트이다. 1번 노드의 자식은 2번 노드이다. 2번 노드의 자식은 3번 노드이다. 3번 노드의 자식은 4번 노드이다. 5번 노드는 1번 노드에서 방문 될 수 없다.

<br>

## 📝 풀어보기 

정점의 수 N, 간선의 수 M, 시작 정점 R을 입력받는다.

무방향 그래프를 저장하기 위해 graph에 N+1만큼의 빈 리스트를 미리 생성해둔다.

visited로 방문여부를 확인하면서, 모든 노드의 깊이를 방문할 때마다 저장하고 방문하지 않은 노드는 -1로 저장한다.

``` python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1) # 미방문 노드를 -1로 초기화
```

<br>

M개의 줄에 걸쳐서 간선정보 u, v를 입력받아 graph에 저장한다.

저장된 그래프를 오름차순으로 정렬한다.

``` python
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for num in graph:
    num.sort()
```

<br>

DFS를 정의한다. 시작정점 r이 들어가면, graph의 시작정점을 순회하면서 방문하지 않은곳을 방문하면 1씩 증가시킨다.

시작정점은 0이기 때문에, visited[R]을 0으로 초기화시키고 DFS를 실행한다.

visited의 1번째 인덱스부터 마지막까지 출력한다.

```python
def DFS(r):
    for i in graph[r]:
        if visited[i] == -1:
            # 노드를 방문하면서 깊이를 저장
            visited[i] = visited[r]+1
            DFS(i)

visited[R] = 0
DFS(R)

for i in visited[1:]:
    print(i)
```

<br>

#### 전체코드

```python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1) # 미방문 노드를 -1로 초기화

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for num in graph:
    num.sort()

def DFS(r):
    for i in graph[r]:
        if visited[i] == -1:
            # 노드를 방문하면서 깊이를 저장
            visited[i] = visited[r]+1
            DFS(i)

visited[R] = 0
DFS(R)

for i in visited[1:]:
    print(i)
```

