

## 파이썬 알고리즘 수업 - 깊이 우선 탐색 5(BOJ 24483)

<br>

## 문제

오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

*N*개의 정점과 *M*개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 *N*번이고 모든 간선의 가중치는 1이다. 정점 *R*에서 시작하여 깊이 우선 탐색으로 만들어 지는 트리를 깊이 우선 탐색 트리라고 하자. 깊이 우선 탐색 트리에 있는 *i*번 노드의 깊이(depth)를 *di*라고 하자. 시작 정점 *R*의 깊이는 0이고 방문 되지 않는 노드의 깊이는 -1이다. 정점 *R*에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 *i*번 노드의 방문 순서를 *ti*라고 하자. 시작 정점의 방문 순서는 1이고 시작 정점에서 방문할 수 없는 노드는 0이다. 모든 노드에 대한 *di* × *ti* 값의 합을 구해보자.

깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 **오름차순**으로 방문한다.

<br>

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

첫째 줄에 모든 노드에 대한 *di* × *ti* 값의 합을 출력한다.

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
20
```

정점 1번에서 정점 2번을 방문한다. 정점 2번에서 정점 3번을 방문한다. 정점 3번에서 정점 4번을 방문한다. 정점 5번은 정점 1번에서 방문할 수 없다. 따라서, *ti* 값은 1번 정점부터 1, 2, 3, 4, 0이다.

깊이 우선 탐색 트리는 1, 2, 3, 4번 노드로 구성된다. 1번 노드가 루트이다. 1번 노드의 자식은 2번 노드이다. 2번 노드의 자식은 3번 노드이다. 3번 노드의 자식은 4번 노드이다. 5번 노드는 1번 노드에서 방문 될 수 없다. 따라서, *di*값은 1번 정점부터 0, 1, 2, 3, -1이다.

*ti* × *di* 값의 합은 1×0 + 2×1 + 3×2 + 4×3 + 0×(-1) = 20이다.

<br>

## 📝 풀어보기 

정점의 수 N, 간선의 수 M, 시작 정점 R을 입력받는다.

N+1만큼 빈 리스트를 graph에 저장한다. 

방문되지 않은 노드의 깊이 -1을 N+1만큼 visited에 저장한다.

t에는 방문 정점을 담는 리스트다. cnt는 방문 정점을 증가시키며 저장하고, ans는 노드와 방문정점의 카운트를 곱해서 누적합을 할 변수다.

``` python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
t = [0] * (N+1) 
cnt = 1
ans = 0
```

<br>

M만큼 반복하면서 간선 정보 u, v를 입력받는다.

입력받은 간선의 정보를 graph에 저장하고 그래프 내의 값을 오름차순 정렬한다.

그리고 DFS를 수행한다. 

``` python
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for num in graph:
    num.sort()
    
DFS(R, 0)
```

 <br>

DFS를 정의한다.

t의 시작정점 인덱스에 cnt값을 저장한다.

visited의 시작정점 인덱스에 깊이를 저장한다.

graph의 시작정점 인덱스부터 graph내의 요소를 탐색하면서 visited[i]가 -1이라면 cnt를 1 증가시키고 깊이를 1증가시켜준다.

그리고 i값과 증가시킨 깊이값을 인자로 넣어 DFS함수를 재귀호출한다.

``` python
def DFS(r, depth):
    global cnt
    t[r] = cnt
    visited[r] = depth

    for i in graph[r]:
        if visited[i] == -1:
            cnt += 1
            DFS(i, depth+1)
```

<br>

인덱스의 0번째 요소는 사용하지 않기 때문에 1부터 N+1까지 t[i]와 visited[i]를 곱한 값을 ans에 누적시키고 ans를 출력한다.

``` python
for i in range(1, N+1): 
    ans += t[i] * visited[i]

print(ans)
```

<br>

#### 전체코드

```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
t = [0] * (N+1) 
cnt = 1
ans = 0

def DFS(r, depth):
    global cnt
    t[r] = cnt
    visited[r] = depth

    for i in graph[r]:
        if visited[i] == -1:
            cnt += 1
            DFS(i, depth+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for num in graph:
    num.sort()
    
DFS(R, 0)

for i in range(1, N+1): 
    ans += t[i] * visited[i]

print(ans)
```

