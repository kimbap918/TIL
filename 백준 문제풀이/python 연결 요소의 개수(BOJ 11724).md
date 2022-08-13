## 파이썬 연결요소의 개수(백준 BOJ 11724)

<br>

DFS를 사용해보는 문제

## 문제

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

<br>

## 출력

첫째 줄에 연결 요소의 개수를 출력한다.

<br>

## 예제 입력 1

```
6 5
1 2
2 5
5 1
3 4
4 6
```

## 예제 출력 1

```
2
```

## 예제 입력 2 

```
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
```

## 예제 출력 2

```
1
```

<br>

## 📝 풀어보기

📌 sys를 import해서 재귀 제한을 걸어놓는다. 재귀 제한을 걸지 않으면 RecursionError가 발생한다.

정점의 개수 `N`, 간선의 개수 `M`을 입력받고 1부터 시작하기때문에 N + 1만큼 값이 없는 빈 인접리스트를 생성한다.

방문 확인을 위해 visited를 생성하고 연결요소 개수를 카운트하기 위해 answer변수를 생성해둔다.

``` python
# visited[start] = False
# start를 한 횟수 2번이 연결요소의 개수
# 시작을 한 횟수 == 연결요소의 개수
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split()) # 6 5
adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0
```

<br>

📌 dfs 함수 생성을 하는것이 먼저가 맞으나, 이해를 위해 코드를 먼저 설명한다. 

간선의 개수 범위만큼 간선의 양 끝점을 입력받아 adj_list에 입력한다.

예를 들어 u, v에 1, 2가 입력됐다면 adj_list[1].append(2), adj_list[2].append(1)이 된 셈이다.

1부터 N + 1 범위를 반복하며 방문을 확인한다. visited[1]이 False라면, True로 변경해주고 answer를 1 증가시켜준다. 그리고 dfs 함수를 호출한다.

``` python
for _ in range(M):
    u, v = map(int, input().split()) # 1 2 / 2 5 / 5 1 / 3 4 / 4 6
    adj_list[u].append(v)
    adj_list[v].append(u)

for number in range(1, N + 1): # 1, 2, 3, 4, 5, 6
    if not visited[number]: # visited[1]
        visited[number] = True # visited[1] = True
        answer += 1 # answer = 1
        dfs(number) # dfs(1)
print(answer)
```

<br>

📌 dfs 함수로 들어간 값은 아래와 같이 실행된다.

만약 1이 들어갔다면 visited[1] = True로 변경되고 인접리스트 내 요소들을 반복하면서 인접 리스트 내의 요소가 False라면 True로 변경해주고 dfs에 다음 값을 넣어 재귀시킨다.

이렇게 방문하지 않은 요소들을 True로 바꾸며 answer를 증가시키고, 그 값을 출력한다.

``` python
def dfs(n): # dfs(1)
    visited[n] = True # visited[1]
    for i in adj_list[n]: #2,1,5,2,1,5,4,3,6,4
        if visited[i] == False: # if visited[2] == False:
            visited[i] = True # visited[2] = True
            dfs(i) # dfs(2) 1, 5, 2, 1, 5, 4 ... 순으로 쭉 순회
```

<br>

#### 전체 코드

``` python
# visited[start] = False
# start를 한 횟수 2번이 연결요소의 개수
# 시작을 한 횟수 == 연결요소의 개수
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split()) # 6 5
adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

def dfs(n): # dfs(1)
    visited[n] = True # visited[1]
    for i in adj_list[n]: #2,1,5,2,1,5,4,3,6,4
        if visited[i] == False: # if visited[2] == False:
            visited[i] = True # visited[2] = True
            dfs(i) # dfs(2) 1, 5, 2, 1, 5, 4 ... 순으로 쭉 순회


for _ in range(M):
    u, v = map(int, input().split()) # 1 2 / 2 5 / 5 1 / 3 4 / 4 6
    adj_list[u].append(v)
    adj_list[v].append(u)

for number in range(1, N + 1): # 1, 2, 3, 4, 5, 6
    if not visited[number]: # visited[1]
        visited[number] = True # visited[1] = True
        answer += 1 # answer = 1
        dfs(number) # dfs(1)

print(answer)
```

