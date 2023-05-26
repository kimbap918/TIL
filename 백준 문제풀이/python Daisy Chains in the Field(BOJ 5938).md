

## 파이썬 Daisy Chains in the Field(BOJ 5938)

<br>

## 문제

Farmer John let his N (1 <= N <= 250) cows conveniently numbered 1..N play in the field. The cows decided to connect with each other using cow-ropes, creating M (1 <= M <= N*(N-1)/2) pairwise connections. Of course, no two cows had more than one rope directly connecting them. The input shows pairs of cows c1 and c2 that are connected (1 <= c1 <= N; 1 <= c2 <= N; c1 != c2).

FJ instructed the cows to be part of a chain which contained cow #1. Help FJ find any misbehaving cows by determining, in ascending order, the numbers of the cows not connected by one or more ropes to cow 1 (cow 1 is always connected to herself, of course). If there are no misbehaving cows, output 0.

To show how this works, consider six cows with four connections:

```
    1---2  4---5
     \  |
      \ |      6
       \|
        3
```

Visually, we can see that cows 4, 5, and 6 are not connected to cow 1.

<br>

## 입력

- Line 1: Two space-separated integers: N and M
- Lines 2..M+1: Line i+1 shows two cows connected by rope i with two space-separated integers: c1 and c2

<br> 

## 출력

- Lines 1..???: Each line contains a single integer

<br> 

## 예제 입력 1 

```
6 4
1 3
2 3
1 2
4 5
```

## 예제 출력 1 

```
4
5
6
```

<br>

## 📝 풀어보기 

이 문제는 1번 소와 연결되는 소를 찾아내고, 연결되지 않은 소를 각각 출력하는 문제다.

문제는 BFS와 DFS로 모두 풀 수 있어 각각의 풀이를 적어봤다.

<br>

#### BFS로 풀어보기

소의 총 마리 수 N, 연결된 수 M을 입력받는다.

인접리스트 cows를 생성해 빈 리스트를 N+1만큼 저장해둔다.

visited에는 연결된 소들의 방문 여부를 파악한다. 각 줄마다 연결된 소들의 정보가 나오므로 중복되는 정보를 없애기 위해 set을 사용했다.

M만큼 반복하면서 연결된 소들의 정보 c1, c2를 입력받고 인접리스트에 저장한다. 그리고 BFS를 실행한다.

```python
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cows = [[] for _ in range(N+1)]
visited = set()

for _ in range(M):
    c1, c2 = map(int, input().split())
    cows[c1].append(c2)
    cows[c2].append(c1)

BFS(cows, 1)
```

<br>

함수 BFS를 정의한다.

visited에 시작지점을 삽입하고 Q에도 시작지점을 저장한다.

Q에서 꺼낸 시작지점의 값을 c에 저장하고, 인접리스트 arr[c]의 값을 순회하면서 방문하지 않은곳은 방문처리를 하고 해당 값을 Q에 삽입한다.

``` python
def BFS(arr, start):
    visited.add(start)
    Q = deque([start])  

    while Q:
        c = Q.popleft() 
        for i in arr[c]:
            if i not in visited:
                visited.add(i)  
                Q.append(i)  
```

<br>

cow_list를 생성한다. 이 리스트는 묶여있지 않은 소를 저장하는데에 사용된다.

첫번째 소를 제외하고, 2부터 N+1까지 순회하면서 방문하지 않은 소가 있으면 cow_list에 소를 저장하고 cow_list에 값이 있으면 하나씩 출력한다. 없는 경우엔 0을 출력한다.

``` python
cow_list = []
for i in range(2, N+1):
    if i not in visited:
        cow_list.append(i)

if cow_list:
    print(*cow_list, sep='\n')
else:
    print(0)
```

<br>

#### BFS 전체코드

``` python
from collections import deque
import sys
input = sys.stdin.readline

def BFS(arr, start):
    visited.add(start)
    Q = deque([start])  

    while Q:
        c = Q.popleft() 
        for i in arr[c]:
            if i not in visited:
                visited.add(i)  
                Q.append(i)  

N, M = map(int, input().split())
cows = [[] for _ in range(N+1)]
visited = set()

for _ in range(M):
    c1, c2 = map(int, input().split())
    cows[c1].append(c2)
    cows[c2].append(c1)

BFS(cows, 1)

cow_list = []
for i in range(2, N+1):
    if i not in visited:
        cow_list.append(i)

if cow_list:
    print(*cow_list, sep='\n')
else:
    print(0)
```

<br>

#### DFS로 풀어보기

소의 총 마리 수 N, 연결된 수 M을 입력받는다.

인접리스트 cows를 생성해 빈 리스트를 N+1만큼 저장해둔다.

visited에는 연결된 소들의 방문 여부를 파악한다. 각 줄마다 연결된 소들의 정보가 나오므로 중복되는 정보를 없애기 위해 set을 사용했다.

M만큼 반복하면서 연결된 소들의 정보 c1, c2를 입력받고 인접리스트에 저장한다. 그리고 DFS를 실행한다.

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 인접리스트
cows = [[] for _ in range(N+1)]
visited = set()

for _ in range(M):
    c1, c2 = map(int, input().split())
    cows[c1].append(c2)
    cows[c2].append(c1)

DFS(cows, visited, 1)
```

<br>

함수 DFS를 정의한다.

visited에 시작지점을 삽입하고 인접리스트 arr[시작지점]의 값을 꺼내어 해당 값이 방문을 하지 않았다면 시작지점을 해당 값으로 바꾸어 DFS를 수행한다. 

```python
def DFS(arr, visited, start):
    visited.add(start)

    for i in arr[start]:
        if i not in visited:
            DFS(arr, visited, i)
```

<br>

묶여있지 않은 소들을 저장할 리스트 cow_list를 생성한다.

1번 소를 제외한 2부터 N+1까지 순회하면서 방문하지 않은 소가 있을 경우 cow_list에 저장하고, cow_list에 값이 있으면 각각의 소들을 출력하고 없다면 0을 출력한다.

```python
# 묶여있지 않은 소들의 리스트
cow_list = []
for i in range(2, N+1):
    if i not in visited:
        cow_list.append(i)

if cow_list:
    print(*cow_list, sep='\n')
else:
    print(0)
```

<br>

#### DFS 전체코드

```python
import sys
input = sys.stdin.readline

def DFS(arr, visited, start):
    visited.add(start)

    for i in arr[start]:
        if i not in visited:
            DFS(arr, visited, i)

N, M = map(int, input().split())
# 인접리스트
cows = [[] for _ in range(N+1)]
visited = set()

for _ in range(M):
    c1, c2 = map(int, input().split())
    cows[c1].append(c2)
    cows[c2].append(c1)

DFS(cows, visited, 1)

# 묶여있지 않은 소들의 리스트
cow_list = []
for i in range(2, N+1):
    if i not in visited:
        cow_list.append(i)

if cow_list:
    print(*cow_list, sep='\n')
else:
    print(0)
```

