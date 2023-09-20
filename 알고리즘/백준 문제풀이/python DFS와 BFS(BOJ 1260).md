

## 파이썬 DFS와 BFS(BOJ 1260)

<br>

## 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

<br>

## 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

<br>

## 출력

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

<br>

## 예제 입력 1 

```
4 5 1
1 2
1 3
1 4
2 4
3 4
```

## 예제 출력 1 

```
1 2 4 3
1 2 3 4
```

## 예제 입력 2 

```
5 5 3
5 4
5 2
1 2
3 4
3 1
```

## 예제 출력 2 

```
3 1 2 5 4
3 1 4 2 5
```

## 예제 입력 3 

```
1000 1 1000
999 1000
```

## 예제 출력 3 

```
1000 999
1000 999
```

<br>

## 📝 풀어보기 

이전의 너비 우선 탐색(BFS), 깊이 우선 탐색(DFS)를 모두 활용하여 푸는 문제다.

두 가지를 모두 구현하여 출력하면 된다.

#### 전체코드

``` python
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for num in graph:
    num.sort()

def dfs(visited, graph, V):
    visited[V] = 1
    print(V, end=" ")
    for i in graph[V]:
        if visited[i] == 0:
            dfs(visited, graph, i)

def bfs(visited, graph, V):
    visited[V] = 1
    Q = deque([V])
    while Q:
        V = Q.popleft()
        print(V, end=" ")
        for i in graph[V]:
            if visited[i] == 0:
                visited[i] = 1
                Q.append(i)
        


dfs(visited_dfs, graph, V)
print()
bfs(visited_bfs, graph, V)
```

