

## 파이썬 트리의 부모 찾기(BOJ 11725)

<br>

## 문제

루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

<br>

## 출력

첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

<br>

## 예제 입력 1

```
7
1 6
6 3
3 5
4 1
2 4
4 7
```

## 예제 출력 1 

```
4
6
1
3
1
4
```

## 예제 입력 2 

```
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
```

## 예제 출력 2 

```
1
1
2
3
3
4
4
5
5
6
6
```

<br>

## 📝 풀어보기 

이 문제도 DFS, BFS로 각각 풀이해보았다.

<br>

#### BFS

노드의 개수 N을 입력받는다.

tree에는 트리 상에 연결된 두 정점정보를 담기위해 빈 리스트를 저장한다.

visited는 결과값 출력을 위해 [0]을 N+1만큼 저장해둔다. 

```python
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
visited_2 = [0] * (N+1)

```

<br>

N-1개의 줄만큼 반복하며 두 정점정보를 받아 tree에 저장한다. 그리고 BFS(1)을 수행한다.

``` python
for i in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
   
BFS(1)
```

<br>

BFS를 정의한다.

Q에 트리의 루트(1)을 담고 Q에서 꺼낸 값을 cur에 저장한다.

tree의 cur인덱스 내의 값을 탐색하면서, 방문하지 않은곳이 있으면 해당 방문위치에 cur을 저장하고 Q에 순회중인 값을 저장한다.

```python
def BFS(r):
    Q = deque([r])

    while Q:
        cur = Q.popleft()
        for i in tree[cur]:
            if visited_2[i] == 0:
                visited_2[i] = cur
                Q.append(i)
```

<br>

visited의 2번째 인덱스부터 값을 출력한다.

```python
for i in visited_2[2:]:
    print(i)
```

<br>

#### DFS

노드의 개수 N을 입력받는다.

tree에는 트리 상에 연결된 두 정점정보를 담기위해 빈 리스트를 저장한다.

visited는 결과값 출력을 위해 [0]을 N+1만큼 저장해둔다. 

```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
visited_1 = [0] * (N+1)
```

<br>

N-1개의 줄만큼 반복하며 두 정점정보를 받아 tree에 저장한다. 그리고 DFS(1)을 수행한다.

``` python
for i in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
 
DFS(1)
```

<br>

tree의 루트 인덱스 내의 값을 탐색하면서, 방문하지 않은곳이 있다면 해당 값을 r로 변경하고 DFS(i)를 수행한다.

``` python
def DFS(r):
    for i in tree[r]:
        if visited_1[i] == 0:
            visited_1[i] = r
            DFS(i)
```

<br>

visited의 2번째 인덱스부터 값을 차례대로 출력한다.

``` python
for i in visited_1[2:]:
    print(i)
```

<br>

#### 전체코드

```python
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
visited_1 = [0] * (N+1)
visited_2 = [0] * (N+1)


def DFS(r):
    for i in tree[r]:
        if visited_1[i] == 0:
            visited_1[i] = r
            DFS(i)

def BFS(r):
    Q = deque([r])

    while Q:
        cur = Q.popleft()
        for i in tree[cur]:
            if visited_2[i] == 0:
                visited_2[i] = cur
                Q.append(i)


for i in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)


DFS(1)
BFS(1)

for i in visited_1[2:]:
    print(i)

for i in visited_2[2:]:
    print(i)
```

