

## 파이썬 이분 그래프(BOJ 1707)

<br>

## 문제

그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

<br>

## 입력

입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 

<br>

## 출력

K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

<br>

## 제한

- 2 ≤ K ≤ 5
- 1 ≤ V ≤ 20,000
- 1 ≤ E ≤ 200,000

<br>

## 예제 입력 1 

```
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
```

## 예제 출력 1

```
YES
NO
```

<br>

## 📝 풀어보기 

이분 그래프(Bipartiete Graph)는 인접해있는 정점끼리 서로 다른색으로 칠해서 모든 정점을 두 가지 색으로만 나눌 수 있는 그래프를 말한다. 

이분 그래프를 BFS로 확인할 땐 같은 레벨의 정점을 같은 색으로 칠해서 두 가지로만 나눠지는지 확인하면 된다.

#### 이분 그래프의 확인법

너비 우선 탐색(BFS), 깊이 우선 탐색(DFS)를 이용한다.

* 인접한 정점이 같은 색이면 이분 그래프가 아니다.
* BFS, DFS로 탐색하면서 정점을 방문할 때 마다 두 가지 색 중 하나로 칠한다.
* 다음 정점을 방문하면서 자신과 인접한 정점은 **다른 색**으로 칠한다.
* 탐색 시 자신과 인접한 정점의 색이 자신의 색과 동일하다면 이분 그래프가 아니다.
* 연결 그래프와 비연결 그래프를 둘 다 고려해야한다.
  * 그래프가 비연결 그래프인 경우 모든 정점에 대하여 확인하는 작업이 필요하다.

<br> 

테스트 케이스 K를 입력받고 정점의 개수(V), 간선의 개수(E)를 입력받는다.

graph에는 정점의 개수 +1 만큼 빈 리스트를 생성하고 방문 확인을 위해 똑같이 정점의 개수 +1만큼 False를 저장해둔다.

``` python
import sys
from collections import deque
input = sys.stdin.readline

for K in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
```

<br>

E 줄에 걸쳐 정점의 개수와 간선의 개수를 입력받고 graph에 저장한다.

문제의 조건에서 정점에는 1부터 V까지 차례로 번호가 붙어있으므로, 1부터 V까지 순회하면서 방문하지 않은 경우에 BFS를 수행한 값을 ans에 저장하고, ans가 False를 반환받아 저장할경우 반복을 탈출할수 있도록 한다.

``` python
    # E줄에 걸쳐 정점의 개수, 간선의 개수를 입력받음
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
	  # 각 정점에는 1부터 V까지 차례로 번호가 붙어있다.
    for j in range(1, V+1):
        if not visited[j]:
            ans = BFS(j, 1)
            if not ans:
                break
```

<br>

BFS를 정의한다.

Q에 시작 정점의 값을 넣어 저장하고, 시작 정점의 방문처리를 한다.

반복이 종료될때까지 Q에서 정점의 값을 꺼내어, x에 저장하고 graph[x]에서 방문하지 않은곳은 Q에 삽입하고, 다른 색으로 칠한다.

순회하는 값이 visited[x]와 같다면 이분그래프가 아니므로 False를 반환한다. 그 외엔 True를 반환한다.

```python
def BFS(start, num):
    Q = deque([start])
    visited[start] = num
    
    while Q:
        x = Q.popleft()

        for i in graph[x]:
            if not visited[i]:
                Q.append(i)
                visited[i] = -1 * visited[x]
            elif visited[i] == visited[x]:
                return False
    return True
```

<br>

ans가 True를 반환받았을 경우 이분 그래프이므로 YES를 출력하고 그외엔 NO를 출력한다.

``` python
    if ans:
        print("YES")
    else:
        print("NO")
```



#### 전체코드

``` python
import sys
from collections import deque
input = sys.stdin.readline

def BFS(start, num):
    Q = deque([start])
    visited[start] = num
    
    while Q:
        x = Q.popleft()

        for i in graph[x]:
            if not visited[i]:
                Q.append(i)
                visited[i] = -1 * visited[x]
            elif visited[i] == visited[x]:
                return False
    return True

for K in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)

    # E줄에 걸쳐 정점의 개수, 간선의 개수를 입력받음
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 각 정점에는 1부터 V까지 차례로 번호가 붙어있다.
    for j in range(1, V+1):
        if not visited[j]:
            ans = BFS(j, 1)
            if not ans:
                break

    if ans:
        print("YES")
    else:
        print("NO")
```

<br>



