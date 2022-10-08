## 파이썬 스타트와 링크(백준 BOJ 14889)

<br>

## 문제

오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

<br>

| i\j  | 1    | 2    | 3    | 4    |
| :--- | :--- | :--- | :--- | :--- |
| 1    |      | 1    | 2    | 3    |
| 2    | 4    |      | 5    | 6    |
| 3    | 7    | 1    |      | 2    |
| 4    | 3    | 4    | 5    |      |

예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

- 스타트 팀: S12 + S21 = 1 + 4 = 5
- 링크 팀: S34 + S43 = 2 + 5 = 7

1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

- 스타트 팀: S13 + S31 = 2 + 7 = 9
- 링크 팀: S24 + S42 = 6 + 4 = 10

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

<br>

## 입력

첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

<br>

## 출력

첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

<br>

## 예제 입력 1 

```
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
```

## 예제 출력 1 

```
0
```

## 예제 입력 2 

```
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
```

## 예제 출력 2 

```
2
```

## 예제 입력 3 

```
8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
```

## 예제 출력 3 

```
1
```

## 힌트

예제 2의 경우에 (1, 3, 6), (2, 4, 5)로 팀을 나누면 되고, 예제 3의 경우에는 (1, 2, 4, 5), (3, 6, 7, 8)로 팀을 나누면 된다.

<br>

## 📝 풀어보기

📌 전체 인원의 수 n을 입력받는다. 방문 확인을 위해 visited에 n만큼 0을 생성해서 리스트로 저장한다.

능력치를 이중리스트 형태로 입력받아 저장해둔다. 최소 차이값을 저장하기 위해 min_diff를 생성한다.

``` python
n = int(input())

visited = [0 for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)
```

<br>

📌  min_diff를 전역변수로 설정하고 idx부터 n의 범위까지 반복하면서 방문이 없으면 visited[i]를 True로 변경하고 depth, i 에 각각 1을 더하고 dfs를 실행시킨다. 실행을 하고 방문을 False로 변경한다.

depth가 증가하다가 팀의 인원수인 n//2명과 같아지면 team1, team2를 생성해서 0으로 초기화 하고 n의 범위에서 2중반복하면서 방문처리된 팀에 `graph[i][j]` 값을 누적하고 나머지 방문처리 되지 않은 팀에  `graph[i][j]` 값을 저장하고 min_diff, team1-team2의 절대값 중 최소값을 min_diff에 저장한다.

``` python
def dfs(depth, idx):
    global min_diff
    # 팀의 인원수가 n//2명으로 다 채워졌을때
    if depth == n//2:
      	# 스타트팀, 링크팀 능력치를 구하기 위한 변수
        team1, team2 = 0, 0
        for i in range(n):
            for j in range(n):
              	# 방문처리된 팀이 스타트팀이면
                if visited[i] and visited[j]:
                    team1 += graph[i][j]
                # 방문처리 되지않은 팀이 링크팀
                elif not visited[i] and not visited[j]:
                    team2 += graph[i][j]
        min_diff = min(min_diff, abs(team1-team2))
        return
		# idx(시작 : 0) 부터 n까지 
    for i in range(idx, n):
      	# 방문이 없으면 
        if not visited[i]:
            visited[i] = True # 1
            dfs(depth+1, i+1) # 1을 추가하고 dfs실행
            visited[i] = False # 0
```

<br>

#### 전체 코드

``` python
def dfs(depth, idx):
    global min_diff
    # 팀의 인원수가 n//2명으로 다 채워졌을때
    if depth == n//2:
      	# 스타트팀, 링크팀 능력치를 구하기 위한 변수
        team1, team2 = 0, 0
        for i in range(n):
            for j in range(n):
              	# 방문처리된 팀이 스타트팀이면
                if visited[i] and visited[j]:
                    team1 += graph[i][j]
                # 방문처리 되지않은 팀이 링크팀
                elif not visited[i] and not visited[j]:
                    team2 += graph[i][j]
        min_diff = min(min_diff, abs(team1-team2))
        return
		# idx(시작 : 0) 부터 n까지 
    for i in range(idx, n):
      	# 방문이 없으면 
        if not visited[i]:
            visited[i] = True # 1
            dfs(depth+1, i+1) # 1을 추가하고 dfs실행
            visited[i] = False # 0


n = int(input())

visited = [0 for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)
```

