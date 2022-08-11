## 파이썬 연결요소의 개수(백준 BOJ 11724)

<br>

DFS

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

