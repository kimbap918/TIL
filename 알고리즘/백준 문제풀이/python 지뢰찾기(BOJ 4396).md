## 파이썬 지뢰찾기(백준 BOJ 4396)

<br>

## 문제

지뢰찾기는 n × n 격자 위에서 이루어진다. m개의 지뢰가 각각 서로 다른 격자 위에 숨겨져 있다. 플레이어는 격자판의 어느 지점을 건드리기를 계속한다. 지뢰가 있는 지점을 건드리면 플레이어가 진다. 지뢰가 없는 지점을 건드리면, 그곳의 상하좌우 혹은 대각선으로 인접한 8개의 칸에 지뢰가 몇 개 있는지 알려주는 0과 8 사이의 숫자가 나타난다. 완전히 플레이되지 않은 게임에서 일련의 동작이 아래에 나타나 있다.

![img](https://www.acmicpc.net/upload/images3/Image1.gif)![img](https://www.acmicpc.net/upload/images3/Image2.gif)![img](https://www.acmicpc.net/upload/images3/Image3.gif) 

여기서, n은 8이고, m은 10이며, 빈 칸은 숫자 0을 의미하고, 올라가 있는 칸은 아직 플레이되지 않은 위치이며, 별표 모양(*)과 닮은 그림은 지뢰를 의미한다. 맨 왼쪽의 그림은 일부만이 플레이된 게임을 나타낸다. 첫 번째 그림에서 두 번째 그림으로 오면서, 플레이어는 두 번의 이동을 시행해서, 두 번 다 안전한 곳을 골랐다. 세 번째 그림을 볼 때 플레이어는 운이 썩 좋지는 않았다. 지뢰가 있는 곳을 골라서 게임에서 졌다. 플레이어는 m개의 열리지 않은 칸을 남길 때까지 계속해서 안전한 곳을 고르면 이긴다. 그 m개의 칸은 반드시 지뢰이다.

당신이 할 일은 일부가 플레이된 게임의 정보를 읽어 해당하는 격자를 출력하는 것이다.

<br>

## 입력

첫 번째 줄에는 10보다 작거나 같은 양의 정수 n이 입력된다. 다음 n개의 줄은 지뢰의 위치를 나타낸다. 각각의 줄은 n개의 문자를 사용하여 한 행을 나타낸다. 온점(.)은 지뢰가 없는 지점이며 별표(*)는 지뢰가 있는 지점이다. 다음 n개의 줄에는 길이가 n인 문자열이 입력된다. 이미 열린 칸은 영소문자 x로, 열리지 않은 칸은 온점(.)으로 표시된다. 예제 입력은 문제 설명에서의 가운데 그림과 상응한다.

<br>

## 출력

출력은 각각의 위치가 정확하게 채워진 판을 표현해야 한다. 지뢰가 없으면서 열린 칸에는 0과 8 사이의 숫자가 있어야 한다. 지뢰가 있는 칸이 열렸다면 지뢰가 있는 모든 칸이 별표(*)로 표시되어야 한다. 다른 모든 지점은 온점(.)이어야 한다.

<br>

## 예제 입력 1

```
8
...**..*
......*.
....*...
........
........
.....*..
...**.*.
.....*..
xxx.....
xxxx....
xxxx....
xxxxx...
xxxxx...
xxxxx...
xxx.....
xxxxx...
```

## 예제 출력 1

```
001.....
0013....
0001....
00011...
00001...
00123...
001.....
00123...
```

<br>

## 📝 풀어보기

📌 일단 맨 처음 주어지는 사항들을 잘 봐야 문제를 이해하기 편하다.

이 게임은 지뢰찾기 게임이고, `n`은 지뢰찾기 맵의 크기이면서 입력해야할 값의 개수다.

`.` 은 사용자가 클릭하기 전의 필드, `*` 는 지뢰이며, `x` 는 사용자가 클릭한 필드다.

조건은 2가지가 있다.

1. **지뢰가 있는곳을 클릭하면** 출력 시 모든 지뢰가 보여야한다.
2. **지뢰가 없는곳을 클릭하면** 열린 칸에는 0~8사이의 숫자가 출력되어야 한다.

<br>

📌 먼저 입력받을 `n` 을 생성하고 지뢰를 입력할 리스트, 사용자 클릭을 입력할 리스트, 결과를 출력할 리스트를 각각 만든다.

``` python
n = int(input()) # 8

mine_map = list(input() for _ in range(n)) # 지뢰를 입력할 리스트 # 64
mine_click = list(input() for _ in range(n)) # 사용자 클릭을 입력할 리스트 64
mine_result = [['.'] * n for _ in range(n)] # 결과를 출력할 리스트 64
```

<br>

📌 그다음 지뢰가 없는곳을 클릭시 0~8사이의 숫자가 출력되어야 하기 때문에 델타탐색 방법을 사용한다.

`dc(행)`, `dr(열)`  을 각각 -1, -1 -> -1, 0 .. 순으로 돌면서 사용자가 선택한 x를 기준으로 8방위를 체크하게끔 만든다.

``` python
dc = [-1, -1, -1, 0, 1, 1, 1, 0] # ex) -1,-1 = x보다 위,왼쪽 / -1,0 = x보다 위,중앙 
dr = [-1, 0, 1, 1, 1, 0, -1, -1] # -1,1 = x보다 위,오른쪽 / 0,1 = x보다 중앙,오른쪽
```

<br>

📌 n의 범위만큼 세로와 가로를 돌면서 지뢰를 밟지 않았을 경우, 카운트를 생성하고 8방위를 돌면서 좌표를 확인한다. 좌표가 음수이거나, n보다 클 때에는 건너뛴다.

좌표 안에 폭단이 있을 경우에는 카운트를 1씩 늘려가며 클릭한 결과에 카운트를 저장한다.

``` python
for c in range(n): # 세로
    for r in range(n): # 가로 
        # 지뢰를 밟지 않았을 경우
        if mine_map[c][r] == "." and mine_click[c][r] == "x": 
            # 클릭시 숫자를 뜨게하는 카운트
            cnt = 0
            # 클릭한 값(x)를 기준으로 8방위의 좌표를 확인 
            for k in range(8):
                nc = c + dc[k]
                nr = r + dr[k]
                # 좌표가 음수이거나(맵 밖을 벗어났거나), n보다 큰 경우 건너뜀
                if nc < 0 or nc >= n or nr < 0 or nr >= n:
                    continue
                # 좌표 안에 폭탄이 있을 경우
                if mine_map[nc][nr] == "*":
                    cnt += 1 # 숫자 카운트 증가(최대 8)
            # 클릭한 결과에 카운트를 저장한다 
            mine_result[c][r] = cnt
```

<br>

📌 지뢰를 밟았을 경우에는 다시한번 n범위만큼 세로와 가로를 돌면서 `mine_map` 의 지뢰 표시를 ` mine_result` 에 띄운다.

그리고 n범위만큼 세로와 가로를 돌면서 결과를 출력한다.

``` python
        # 지뢰를 밟았을 경우
        if mine_map[c][r] == "*" and mine_click[c][r] == "x":  
            for a in range(n):
                for b in range(n):
                    if mine_map[a][b] == "*":
                        mine_result[a][b] = "*"

#결과값 출력
for i in range(n):
    for j in range(n):
        print(mine_result[i][j], end='')
    print()
```

<br>

#### 전체 코드

``` python
n = int(input()) # 8

mine_map = list(input() for _ in range(n)) # 지뢰를 입력할 리스트 # 64
mine_click = list(input() for _ in range(n)) # 사용자 클릭을 입력할 리스트 64
mine_result = [['.'] * n for _ in range(n)] # 결과를 출력할 리스트 64

# 열린 칸 주변에 지뢰가 몇개 있는지(열린칸에서 8방향을 탐색)
# 델타 탐색
# ...
# .x.
# ...
dc = [-1, -1, -1, 0, 1, 1, 1, 0] # ex) -1,-1 = x보다 위,왼쪽 / -1,0 = x보다 위,중앙 
dr = [-1, 0, 1, 1, 1, 0, -1, -1] # -1,1 = x보다 위,오른쪽 / 0,1 = x보다 중앙,오른쪽


for c in range(n): # 세로
    for r in range(n): # 가로 
        # 지뢰를 밟지 않았을 경우
        if mine_map[c][r] == "." and mine_click[c][r] == "x": 
            # 클릭시 숫자를 뜨게하는 카운트
            cnt = 0
            # 클릭한 값(x)를 기준으로 8방위의 좌표를 확인 
            for k in range(8):
                nc = c + dc[k]
                nr = r + dr[k]
                # 좌표가 음수이거나(맵 밖을 벗어났거나), n보다 큰 경우 건너뜀
                if nc < 0 or nc >= n or nr < 0 or nr >= n:
                    continue
                # 좌표 안에 폭탄이 있을 경우
                if mine_map[nc][nr] == "*":
                    cnt += 1 # 숫자 카운트 증가(최대 8)
            # 클릭한 결과에 카운트를 저장한다 
            mine_result[c][r] = cnt

        # 지뢰를 밟았을 경우
        if mine_map[c][r] == "*" and mine_click[c][r] == "x":  
            for a in range(n):
                for b in range(n):
                    if mine_map[a][b] == "*":
                        mine_result[a][b] = "*"

#결과값 출력
for i in range(n):
    for j in range(n):
        print(mine_result[i][j], end='')
    print()
```

