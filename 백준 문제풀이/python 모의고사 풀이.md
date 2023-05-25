

## 파이썬 모의고사 풀이(goorm level)

<br>

### 1번 문제

<img width="1680" alt="스크린샷 2023-05-25 오후 2 53 12" src="https://github.com/kimbap918/TIL/assets/75712723/324ce4c7-4991-494c-9481-8d0c134c304f">
<img width="1680" alt="스크린샷 2023-05-25 오후 2 53 21" src="https://github.com/kimbap918/TIL/assets/75712723/5147f6f2-e2ac-4831-872d-dbc0d0b89d53">

<br>

## 📝 풀어보기

1번 문제는 M개의 테스트 마다 주어지는 k개의 숫자 중에서 최다 등장한 정수를 찾는 문제다.

최다 등장한 정수가 같다면 큰 정수에서 작은 정수 순으로 출력해야 한다.

<br>

이벤트의 개수 N과 사용자의 수 M을 입력받는다.

cnt는 이벤트와 실행 횟수를 담을 딕셔너리다.

``` python
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# defaultdict 는 자료형을 미리 선언 가능하다
cnt = defaultdict(int)
```

<br>

M만큼 반복하면서 이벤트의 실행 내역을 입력받는다.

여기서 입력받은 events[0]은 실행한 이벤트의 개수이므로 제외하고 events[1]부터 들어오는 i값의 개수만큼 1씩 증가시켜 cnt에 저장한다.

cnt의 출력은 예시1을 입력했을때 다음과 같을것이다.

defaultdict(<class 'int'>, {1: 4, 2: 4, 3: 4, 4: 4})

``` python
for _ in range(M):
    events = list(map(int, input().split()))
    for i in events[1:]:
        cnt[i] += 1
```

<br>

lambda식을 사용한다. 의미는 다음과 같다.

lambda x가 cnt.items()(cnt 딕셔너리의 키와 값)에 대해 정렬 조건을 가지는데, x[1]을 오름차순으로 가지고, 값이 같다면 x[0]을 비교해서 정렬. 정렬된 값을 내림차순으로 뒤집는다.

정렬된 `res[0][1]`은 내림차순 정렬되었기 때문에 입력된 값들의 카운트 중 가장 높은 값을 가지고 있을것이다. lamda x[1]이 가장 높은 카운트 값과 같다면 그 값을 필터링하여 res에 저장한다.

res를 순회하면서 가장 높은 카운트에 해당하는 값을 끝에 공백과 함께 출력한다. 

``` python
res = sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)
res = list(filter(lambda x : x[1] == res[0][1], res))

for i in res:
    print(i[0], end=' ')
```

<br>

#### 전체코드

``` python
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# defaultdict 는 자료형을 미리 선언 가능하다
cnt = defaultdict(int)

for _ in range(M):
    events = list(map(int, input().split()))
    for i in events[1:]:
        cnt[i] += 1

res = sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)
res = list(filter(lambda x : x[1] == res[0][1], res))

for i in res:
    print(i[0], end=' ')
```

<br>

### 2번 문제

### <img width="1677" alt="스크린샷 2023-05-25 오후 3 11 02" src="https://github.com/kimbap918/TIL/assets/75712723/f0498967-e446-49c2-887f-f2169f51a936"><img width="1676" alt="스크린샷 2023-05-25 오후 3 11 23" src="https://github.com/kimbap918/TIL/assets/75712723/b22409ea-8d65-45b2-9c3a-c0ee7b911dcc">

<br>

## 📝 풀어보기

2번 문제는 2차원 배열에서 조건에 따른 #의 영역을 탐색하는 문제다.

분산된 #의 영역 개수를 찾고, #의 영역 중 가장 크기가 큰 값 찾기이다.

이런 문제는 BFS와 DFS 두가지 방법으로 모두 풀 수 있지만 파이썬은 재귀에 취약하므로 BFS를 사용해서 푸는게 좋다.

<br>

사진의 가로 크기 N, 세로 크기 M을 입력받아 저장한다.

matrix에는 사진의 상태가 입력되고, visited에는 사진의 크기만큼 방문을 확인하기 위한 값을 저장한다.

each에는 사진이 특정 색깔에 해당하는 영역이 몇 군데 있는지 저장할 변수다. ans는 그 중에 가장 면적이 큰 색깔의 크기를 표시한다. 

dx, dy는 상하좌우를 탐색하기위해 저장된 좌표 리스트다.

``` python
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(str, input().rstrip())) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
each = 0
ans = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
```

<br>

M(세로)과 N(가로)만큼 순회하면서 탐색영역이 #이고, 방문하지 않은 곳이라면 방문처리를 하고 사진의 색깔이 있는 영역이기때문에 each를 1증가시킨다. cnt는 0으로 초기화하고 해당 영역에 대해 BFS를 수행한다.

``` python
for i in range(M):
    for j in range(N):
        if matrix[i][j] == '#' and not visited[i][j]:
            visited[i][j] = True
            each += 1
            cnt = 0
            BFS(i, j)
```

<br>

BFS함수를 선언한다.

Q에 탐색할 i, j를 삽입하고, while문을 돌려 Q에 들어간 값을 빼내 y, x에 저장한다.

여기서 y, x의 4방위를 탐색하는데 y, x를 기준으로 한 4방위 ny, nx가 범위를 벗어나고 방문을 했으며, `matrix[n][y]`가 특정 색깔에 해당하는 영역이 아니라면 건너뛰고 그 외엔 nx, ny를 방문처리하고, Q에 좌표값을 추가한다.

ans는 cnt를 통해 탐색하는 영역의 크기를 저장하고, ans와 cnt중에 더 큰것을 비교해 저장한다. 

탐색이 끝나고 저장된 each와 cnt를 출력한다.

``` python
def BFS(i, j):
    global cnt
    global ans
    Q = deque()
    Q.append([i, j])

    while Q:
        y, x = Q.popleft()
        cnt += 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or nx < 0 or ny >= M or nx >= N or visited[ny][nx] or matrix[ny][nx] == '.':
                continue    
            visited[ny][nx] = True
            Q.append([ny, nx])
    ans = max(ans, cnt)
```

<br>

#### 전체코드

```python
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(str, input().rstrip())) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
each = 0
ans = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(i, j):
    global cnt
    global ans
    Q = deque()
    Q.append([i, j])

    while Q:
        y, x = Q.popleft()
        cnt += 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or nx < 0 or ny >= M or nx >= N or visited[ny][nx] or matrix[ny][nx] == '.':
                continue    
            visited[ny][nx] = True
            Q.append([ny, nx])
    ans = max(ans, cnt)


for i in range(M):
    for j in range(N):
        if matrix[i][j] == '#' and not visited[i][j]:
            visited[i][j] = True
            each += 1
            cnt = 0
            BFS(i, j)


print(each)
print(ans)
```

<br>

### 3번 문제

<img width="1680" alt="스크린샷 2023-05-25 오후 3 19 31" src="https://github.com/kimbap918/TIL/assets/75712723/c2b3f9fa-be21-4f81-9134-4541a7287d89">
<img width="1680" alt="스크린샷 2023-05-25 오후 3 19 46" src="https://github.com/kimbap918/TIL/assets/75712723/5b4fb7ee-0d3f-43c5-878f-4c428217ff29">

<br>

## 📝 풀어보기

A공간에서 B공간으로 이동할 때 비용이 최소인 방법을 구하는 문제다.

여기서 이동은 한번에 최대 3칸으로 제한되어있다.

<br>

그리디 알고리즘은 현재 사건이 다음 사건에 영향을 끼치면 사용할 수 없다.

다음의 예를 보자.

`A 3 1 3 1 3 1 B `가 있을때, A에서 B로 이동한다면?

1. 무조건 3칸을 이동해보기

   -> arr[2] 에서  arr[5] 로 이동 후 B에 도달한다.(3+1 = 비용 4)

   -> 하지만, arr[2] 에서 arr[4]로 이동 후에 B에 도달하는게 더 유리할것이다.(1+1 = 비용 2)

`A 3 4 5 2 B`가 있을때, A에서 B로 이동한다면?

1. 이동 가능한 경로 앞의 최소값으로 이동할때

   -> arr[0] 에서 arr[3]이동 후 B에 도달하면 이동 가능 경로에서는 최소값을 이용한다.(3+2 = 비용 5)

   -> 하지만 arr[1]을 선택 후 바로 B지점에 도달하는 방법이 있다.(비용 4)

<br>

이럴때에는 동적 프로그래밍을 생각해본다.

동적 프로그래밍(Dynamic Programming, DP)은 문제 내에서 규칙을 찾고, 식으로 정리하는 방법이다.

<br>

징검다리를 구성하는 돌의 개수 N을 입력받는다.

돌에 묻어있는 독의 양을 입력받아 리스트 형태로 저장한다.

 ``` python
 from collections import deque
 
 N = int(input())
 P = list(map(int, input().split())) + [0]
 ```

<br>

한 번에 징검다리를 건너는 횟수는 3칸까지다. 그렇기때문에 N이 3 이하라면 구름이는 독을 하나도 묻히지 않고 건널 수 있다.

그외엔 deque를 생성해서 초기값으로 독이 담긴 리스트의 0, 1, 2번째 값을 dp에 삽입한다.

초기 3개의 값을 넣었기 때문에 3부터 N+1까지 반복하면서 dp에 삽입된 0, 1, 2번째 값 중 가장 최소값과 현재 독의 값을 더해 dp에 추가한다. 그리고 앞으로 이동하기 때문에 dp의 맨 왼쪽값은 빼낸다.

반복을 마치고, dp의 마지막 값은 돌다리를 건너면서 독이 가장 덜 묻는 최소의 값이 저장되어있다.

``` python
if N < 3:
    print(0)
else:
    dp = deque()
    dp.append(P[0])
    dp.append(P[1])
    dp.append(P[2])

    for i in range(3, N+1):
        dp.append(min(dp[0], dp[1], dp[2]) + P[i])
        # print(dp)
        dp.popleft()

    print(dp[-1])
```

<br>

#### 전체코드

``` python
from collections import deque

N = int(input())
P = list(map(int, input().split())) + [0]

if N < 3:
    print(0)
else:
    dp = deque()
    dp.append(P[0])
    dp.append(P[1])
    dp.append(P[2])

    for i in range(3, N+1):
        dp.append(min(dp[0], dp[1], dp[2]) + P[i])
        # print(dp)
        dp.popleft()

    print(dp[-1])
```

