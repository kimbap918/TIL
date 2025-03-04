## python 촌수계산(백준 BOJ 2644)

<br>

## 문제

우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

<br>

## 입력

사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

<br>

## 출력

입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.

<br>

## 예제 입력 1 

```
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
```

## 예제 출력 1 

```
3
```

## 예제 입력 2

```
9
8 6
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
```

## 예제 출력 2 

```
-1
```

<br>

## 📝 풀어보기

📌 전체 사람의 수 `n`, 촌수를 계산할 두 사람 `start, end`, 관계의 수 `m`, 사람의 시작점이 1이므로 n+1 만큼의 빈 인접 리스트를 생성한다.

``` python
n = int(input()) # 사람의 수
start, end = list(map(int, input().split())) # 촌수를 계산할 두 사람
m = int(input()) # 관계(간선)의 수
# 빈 리스트를 (n+1)개를 가진 이차원 리스트
# _ : 값을 사용하지 않겠다는 의미
# n+1을 하는 이유, 촌수가 1부터 시작하기 때문에
graph = [[] for _ in range(n + 1)]
```

<br>

📌 m의 범위만큼 반복하며, 간선의 양 끝점을 입력받아 인접 리스트에 추가한다.

``` python
for _ in range(m):
    # 부모 자식 관계
    x, y = list(map(int, input().split()))
    # 무방향 인접 그래프 생성
    graph[x].append(y)
    graph[y].append(x)
```

<br>

📌 방문표시를 할 리스트를 n+1 범위만큼 생성하고 

stack을 생성해서 start값과 촌수값을 같이 추가해준다.

시작값은 True로 변경하고 정답을 출력할 변수 answer를 하나 생성해서 -1을 저장해둔다.

``` python
# 방문 표시를 할 리스트
visited = [False] * (n + 1)

# DFS를 시작하기위해서 기본값 설정
# 스택에 값을 추가할 때 촌수도 같이 추가한다.
# stack = [start]
stack = []
stack.append([start, 0])
visited[start] = True

# 정답을 출력할 변수
answer = -1 
```

<br>

📌 스택이 비어있지 않으면 반복하면서 번호와 촌수를 `number`, `count`에 저장한다. number가 끝 값에 도달하면 answer를 count 값으로 변경해주고 break한다.

adj_graph 를 생성해 해당하는 값의 인접 그래프를 저장하고 adj_graph 범위 만큼을 반복하면서 방문하지 않은 요소가 있다면 stack에 인접 번호와 촌수+1 값을 저장하고 방문을 True로 변경한다.

마지막에 증가된 촌수 값을 출력한다.

``` python
while len(stack) != 0 : # 스택이 비어있지 않으면 반복
    # LIFO, 스택의 가장 위에 있는 값을 저장
    # 번호와 촌수를 같이 pop
    number, count = stack.pop()
    # pop을 한 값이 우리가 원하는 값(end)
    # 촌수가 연결이 안되어있으면 line 35~37 실행 x
    if number == end:
        answer = count
        break
    # 해당하는 값의 인접 그래프를 저장
    adj_graph = graph[number]
    # 인접하는 값들을 탐색 
    for adj_number in adj_graph:
        if not visited[adj_number]:
            # 인접 번호와 촌수+1를 같이 push
            stack.append([adj_number, count + 1])
            visited[adj_number] = True

# 촌수 출력
print(answer)
```

<br>

#### 전체 코드

``` python
n = int(input()) # 사람의 수
start, end = list(map(int, input().split())) # 촌수를 계산할 두 사람
m = int(input()) # 관계(간선)의 수
# 빈 리스트를 (n+1)개를 가진 이차원 리스트
# _ : 값을 사용하지 않겠다는 의미
# n+1을 하는 이유, 촌수가 1부터 시작하기 때문에
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # 부모 자식 관계
    x, y = list(map(int, input().split()))
    # 무방향 인접 그래프 생성
    graph[x].append(y)
    graph[y].append(x)

# 방문 표시를 할 리스트
visited = [False] * (n + 1)

# DFS를 시작하기위해서 기본값 설정
# 스택에 값을 추가할 때 촌수도 같이 추가한다.
# stack = [start]
stack = []
stack.append([start, 0])
visited[start] = True

# 정답을 출력할 변수
answer = -1 

while len(stack) != 0 : # 스택이 비어있지 않으면 반복
    # LIFO, 스택의 가장 위에 있는 값을 저장
    # 번호와 촌수를 같이 pop
    number, count = stack.pop()
    # pop을 한 값이 우리가 원하는 값(end)
    # 촌수가 연결이 안되어있으면 line 35~37 실행 x
    if number == end:
        answer = count
        break
    # 해당하는 값의 인접 그래프를 저장
    adj_graph = graph[number]
    # 인접하는 값들을 탐색 
    for adj_number in adj_graph:
        if not visited[adj_number]:
            # 인접 번호와 촌수+1를 같이 push
            stack.append([adj_number, count + 1])
            visited[adj_number] = True

# 촌수 출력
print(answer)
```

