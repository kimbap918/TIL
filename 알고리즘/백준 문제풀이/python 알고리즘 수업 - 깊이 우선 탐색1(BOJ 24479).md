

## 파이썬 알고리즘 수업 - 깊이 우선 탐색 1(BOJ 24479)

<br>

## 문제

오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

*N*개의 정점과 *M*개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 *N*번이고 모든 간선의 가중치는 1이다. 정점 *R*에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

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
2
3
4
0
```

정점 1번에서 정점 2번을 방문한다. 정점 2번에서 정점 3번을 방문한다. 정점 3번에서 정점 4번을 방문한다. 정점 5번은 정점 1번에서 방문할 수 없다.

<br>

## 📝 풀어보기

최대한 위의 의사코드와 유사하게 풀어봤다.

dfs는 재귀가 여러번 있기때문에 재귀 횟수 제한을 걸어둔다.

정점의 수 N, 간선의 수 M, 시작 정점 R을 입력받고 간선 정보가 담길 리스트 E를 생성해둔다.

방문 유무를 확인하기 위해 visited를 생성하고 방문 정점을 기록하기 위한 cnt에 1을 저장해둔다.

``` python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 5 5 1
N, M, R = map(int, input().split())
# 간선 정보가 담긴 리스트
E = [[] for _ in range(N+1)]
# 방문 기록
visited = [0] * (N+1)
cnt = 1
```

<br>

간선의 수 M만큼 순회하면서 간선정보 u v를 입력받고 간선정보 리스트 E에 저장한다.

저장된 값은 오름차순으로 정렬해준다.

``` python
for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)    

for num in E:
    num.sort()
```

<br>

dfs를 구현한다.

R이 시작정점(start)이므로 

visited[R]에 cnt를 저장해두고 

E[R]을 순회하면서 방문하지 않은 곳에 카운트를 1 증가시키고 다시 dfs(E, i, visited)를 호출한다.

visited의 1번째 인덱스부터 i를 출력해준다. 

```python
def dfs(E, R, visited):
    global cnt
    visited[R] = cnt
    for i in E[R]:
        if visited[i] == False:
            cnt += 1
            dfs(E, i, visited)
    return visited

dfs(E, R, visited)

for i in visited[1:]:
    print(i)
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 5 5 1
N, M, R = map(int, input().split())
# 간선 정보가 담긴 리스트
E = [[] for _ in range(N+1)]
# 방문 기록
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)    

for num in E:
    num.sort()

def dfs(E, R, visited):
    global cnt
    visited[R] = cnt
    for i in E[R]:
        if visited[i] == False:
            cnt += 1
            dfs(E, i, visited)
    return visited

dfs(E, R, visited)

for i in visited[1:]:
    print(i)

```

