## 파이썬 바이러스(백준 BOJ 2606)

<br>

DFS 사용 문제

## 문제

신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

![img](https://www.acmicpc.net/upload/images/zmMEZZ8ioN6rhCdHmcIT4a7.png)

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

## 출력

1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

## 예제 입력 1 복사

```
7
6
1 2
2 3
1 5
5 2
5 6
4 7
```

## 예제 출력 1

```
4
```

<br>

## 📝 풀어보기 

📌 연결된 컴퓨터의 수 `n`, 네크워크 상에 연결된 컴퓨터 쌍의 수 `m`을 입력받는다.

문제의 인덱스가 1부터 시작하므로 n + 1만큼 컴퓨터의 번호 쌍을 입력받는다.

DFS는 왔던 곳을 확인해야하므로 방문하지 않은곳을 False, 방문한곳을 True로 표시하기 위한 변수와 중복을 제거할 set을 생성한다.

``` python
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)] # 문제의 인덱스가 1부터 시작해서 n + 1
visited = [False] * (n + 1) # 왔던곳을 확인할 변수
total = set()
```

<br>

📌 m에 대한 인접리스트를 생성한다.

아래의 코드를 실행하면 주석과 같이 생성된다.

``` python
# 인접리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
"""
graph = [
    [],
    [2, 5],
    [1, 3, 5],
    [2],
    [7],
    [1, 2, 6],
    [5],
    [4]
]
"""
```

<br>

📌 DFS를 수행한다.

stack에 시작 컴퓨터 1을 넣어주고 visited의 시작점을 True로 바꿔준다.

stack이 빌때까지 반복하며 cur에 스택의 빠져나온 값을 저장한다.

그래프 리스트 내의 요소값을 반복하면서 visited[adj]가 False면, True로 바꾸고 스택과 total에 adj의 값을 추가한다.

마지막에 total을 반환받고 total의 총 길이를 출력한다.

``` python
def dfs(start):
    stack = [start] # stack = [1]
    # print(stack)
    visited[start] = True # visited[1] = True

    while stack:
        # pop이 맨 마지막에 추가된 요소를 가져오므로 2가 아닌 5가 빠져나간다.
        cur = stack.pop() # 1 stack.append 끝나고 -> 5
        # print("cur :"+str(cur))

        for adj in graph[cur]: # graph[1] = [2, 5]
            # print("adj :"+str(adj))
            if not visited[adj]: # visited[2] = False / visited[5] = False
                visited[adj] = True # visited[2] = True / visited[5] = False
                stack.append(adj) # stack.append(2) / stack.append(5)
                total.add(adj)
    return total
print(len(dfs(1)))
```

<br>

#### 전체 코드

``` python
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)] # 문제의 인덱스가 1부터 시작해서 n + 1
visited = [False] * (n + 1) # 왔던곳을 확인할 변수
total = set()

# 인접리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

"""
graph = [
    [],
    [2, 5],
    [1, 3, 5],
    [2],
    [7],
    [1, 2, 6],
    [5],
    [4]
]
"""
def dfs(start):
    stack = [start] # stack = [1]
    # print(stack)
    visited[start] = True # visited[1] = True

    while stack:
        # pop이 맨 마지막에 추가된 요소를 가져오므로 2가 아닌 5가 빠져나간다.
        cur = stack.pop() # 1 stack.append 끝나고 -> 5
        # print("cur :"+str(cur))

        for adj in graph[cur]: # graph[1] = [2, 5]
            # print("adj :"+str(adj))
            if not visited[adj]: # visited[2] = False / visited[5] = False
                visited[adj] = True # visited[2] = True / visited[5] = False
                stack.append(adj) # stack.append(2) / stack.append(5)
                total.add(adj)
    return total
print(len(dfs(1)))
# 최종적으로 1번 컴퓨터에 의해 감염되는 컴퓨터는 2, 3, 5, 6
```

