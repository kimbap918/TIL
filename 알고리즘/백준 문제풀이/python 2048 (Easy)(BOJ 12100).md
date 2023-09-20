

## 파이썬 2048 (Easy)(BOJ 12100)

<br>

## 문제

2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다. 이 [링크](https://gabrielecirulli.github.io/2048/)를 누르면 게임을 해볼 수 있다.

이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다. 이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다. 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다. (실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)

| ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/1.png) | ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/2.png) | ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/3.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <그림 1>                                                     | <그림 2>                                                     | <그림 3>                                                     |

<그림 1>의 경우에서 위로 블록을 이동시키면 <그림 2>의 상태가 된다. 여기서, 왼쪽으로 블록을 이동시키면 <그림 3>의 상태가 된다.

| ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/4.png) | ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/5.png) | ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/6.png) | ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/7.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <그림 4>                                                     | <그림 5>                                                     | <그림 6>                                                     | <그림 7>                                                     |

<그림 4>의 상태에서 블록을 오른쪽으로 이동시키면 <그림 5>가 되고, 여기서 다시 위로 블록을 이동시키면 <그림 6>이 된다. 여기서 오른쪽으로 블록을 이동시켜 <그림 7>을 만들 수 있다.

| ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/8.png) | ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/10.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <그림 8>                                                     | <그림 9>                                                     |

<그림 8>의 상태에서 왼쪽으로 블록을 옮기면 어떻게 될까? 2가 충돌하기 때문에, 4로 합쳐지게 되고 <그림 9>의 상태가 된다.

| ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/17.png) | ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/18.png) | ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/19.png) | ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/20.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <그림 10>                                                    | <그림 11>                                                    | <그림 12>                                                    | <그림 13>                                                    |

<그림 10>에서 위로 블록을 이동시키면 <그림 11>의 상태가 된다. 

<그림 12>의 경우에 위로 블록을 이동시키면 <그림 13>의 상태가 되는데, 그 이유는 한 번의 이동에서 이미 합쳐진 블록은 또 합쳐질 수 없기 때문이다.

| ![img](https://www.acmicpc.net/problem/12100) | ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/12094/22.png) |
| --------------------------------------------- | ------------------------------------------------------------ |
| <그림 14>                                     | <그림 15>                                                    |

마지막으로, 똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다. 예를 들어, 위로 이동시키는 경우에는 위쪽에 있는 블록이 먼저 합쳐지게 된다. <그림 14>의 경우에 위로 이동하면 <그림 15>를 만든다.

이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다. 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.

<br>

## 출력

최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.

<br>

## 예제 입력 1

```
3
2 2 2
4 4 4
8 8 8
```

## 예제 출력 1 

```
16
```

<br>

## 📝 풀어보기

#### 깊은 복사(Deep Copy) 사용하기

깊은 복사에 관해선 https://crackerjacks.tistory.com/14 블로그를 참고했다.

깊은 복사(Deep Copy)는 원본배열을 보존하면서 배열을 복사할 수 있는 방법이다.

``` python
a = [1, 2, 3, 4]
b = a
print(a, b) # [1, 2, 3, 4] [1, 2, 3, 4]
b[1] = 0 # 배열 b의 두번째 값을 0으로 바꿔준다.
print(a, b) # [1, 0, 3, 4] [1, 0, 3, 4]
```

위 글에서 처럼 배열을 복사하면 **Mutable한 리스트는 원본 객체의 주소값을 복사**해서 b의 값을 수정하면 a또한 수정된다. 하지만, 이번에 풀어볼 2048문제에는 원본 리스트를 보존하면서 리스트를 사용해야한다.

**깊은 복사(Deep Copy)는 참조값의 복사가 아닌 객체 자체를 복사한다.**

``` python
import copy

a = [1, 2, 3, 4]
b = copy.deepcopy(a)
b[1] = 0
print(a, b) # [1, 2, 3, 4] [1, 0, 3, 4]
```

이 점을 염두해두고 코드를 살펴보자.

<br>

깊은 복사 사용을 위해 copy모듈의 deepcopy를 import 한다.

보드의 크기 N을 입력받고 게임판의 상태를 입력받아 board에 저장한다.

ans는 **최대 5번**을 이동시켜서 얻을 수 있는 가장 큰 블록의 크기를 담을 변수다.

``` python
import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
```

<br>

DFS를 정의한다. 최대 5번이므로, cnt가 5가 되면 보드의 가로, 세로 크기만큼 탐색하면서 ans에 ans와 board의 탐색값 중 최대값을 저장해 리턴한다.

2048은 위, 아래, 왼쪽 오른쪽을 움직이면서 같은 숫자를 병합한다. 그러므로 4번 반복하면서 tmp에 move함수를 실행한 값을 저장하고, tmp와 cnt를 1 증가시킨 값을 인자로 해서 DFS를 수행한다.

```python
def DFS(board, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, board[i][j])
        return
    
    # 위, 왼쪽, 아래, 오른쪽
    for i in range(4):
        tmp = move(deepcopy(board), i)
        DFS(tmp, cnt+1)
```

<br>

보드에서의 상, 하, 좌, 우 움직임에 따른 move함수를 정의한다.

여기서 옮길 블록은 `board[i][j]`이고 바뀌게 될 자리는 `board[i][cur]`값이 된다.

```python
# 동, 서, 남, 북으로 이동
def move(board, dir):
    if dir == 0: # 방향이 왼쪽
        for i in range(N):
            cur = 0
            for j in range(1, N):
                if board[i][j] != 0: # 0이 아닌값이 있을경우
                    tmp = board[i][j]
                    board[i][j] = 0 # 합쳐질 것이기 때문에 비운다.

                    if board[i][cur] == 0: # 비어있는 공간이면
                        board[i][cur] = tmp # 값을 옮긴다.
                    
                    elif board[i][cur] == tmp: # 값이 같으면
                        board[i][cur] *= 2 # 합친다
                        cur += 1
                    
                    else: # 비어있지 않고, 다른 값이면
                        cur += 1
                        board[i][cur] = tmp
        # print(board)
    elif dir == 1: # 방향이 오른쪽
        for i in range(N):
            cur = N-1
            for j in range(N-1, -1, -1):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[i][cur] == 0:
                        board[i][cur] = tmp

                    elif board[i][cur] == tmp:
                        board[i][cur] *= 2
                        cur -= 1
                    
                    else:
                        cur -= 1
                        board[i][cur] = tmp

    elif dir == 2: # 방향이 위
        for j in range(N):
            cur = 0
            for i in range(N):
                if board[i][j] != 0: 
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[cur][j] == 0: 
                        board[cur][j] = tmp

                    elif board[cur][j] == tmp:
                        board[cur][j] *= 2
                        cur += 1

                    else:
                        cur += 1
                        board[cur][j] = tmp
                        
    else:
        for i in range(N):
            cur = N-1
            for j in range(N-1, -1, -1):
                if board[j][i] != 0:
                    tmp = board[j][i]
                    board[j][i] = 0

                    if board[cur][i] == 0:
                        board[cur][i] = tmp

                    elif board[cur][i] == tmp:
                        board[cur][i] *= 2
                        cur -= 1
                    
                    else:
                        cur -= 1
                        board[cur][i] = tmp
    return board
```

<br>

#### 전체코드

``` python
import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 동, 서, 남, 북으로 이동
def move(board, dir):
    if dir == 0: # 방향이 왼쪽
        for i in range(N):
            cur = 0
            for j in range(1, N):
                if board[i][j] != 0: # 0이 아닌값이 있을경우
                    tmp = board[i][j]
                    board[i][j] = 0 # 합쳐질 것이기 때문에 비운다.

                    if board[i][cur] == 0: # 비어있는 공간이면
                        board[i][cur] = tmp # 값을 옮긴다.
                    
                    elif board[i][cur] == tmp: # 값이 같으면
                        board[i][cur] *= 2 # 합친다
                        cur += 1
                    
                    else: # 비어있지 않고, 다른 값이면
                        cur += 1
                        board[i][cur] = tmp
        # print(board)
    elif dir == 1: # 방향이 오른쪽
        for i in range(N):
            cur = N-1
            for j in range(N-1, -1, -1):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[i][cur] == 0:
                        board[i][cur] = tmp

                    elif board[i][cur] == tmp:
                        board[i][cur] *= 2
                        cur -= 1
                    
                    else:
                        cur -= 1
                        board[i][cur] = tmp

    elif dir == 2: # 방향이 위
        for j in range(N):
            cur = 0
            for i in range(N):
                if board[i][j] != 0: 
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[cur][j] == 0: 
                        board[cur][j] = tmp

                    elif board[cur][j] == tmp:
                        board[cur][j] *= 2
                        cur += 1

                    else:
                        cur += 1
                        board[cur][j] = tmp
                        
    else:
        for i in range(N):
            cur = N-1
            for j in range(N-1, -1, -1):
                if board[j][i] != 0:
                    tmp = board[j][i]
                    board[j][i] = 0

                    if board[cur][i] == 0:
                        board[cur][i] = tmp

                    elif board[cur][i] == tmp:
                        board[cur][i] *= 2
                        cur -= 1
                    
                    else:
                        cur -= 1
                        board[cur][i] = tmp
    return board

def DFS(board, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, board[i][j])
        return
    
    # 위, 왼쪽, 아래, 오른쪽
    for i in range(4):
        tmp = move(deepcopy(board), i)
        DFS(tmp, cnt+1)

DFS(board, 0)
print(ans)
```

