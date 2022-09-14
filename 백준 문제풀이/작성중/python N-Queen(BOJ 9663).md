## 파이썬 N-Queen(백준 BOJ 9663)

<br>

## 문제

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 N이 주어진다. (1 ≤ N < 15)

<br>

## 출력

첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

<br>

## 예제 입력 1

```
8
```

## 예제 출력 1

```
92
```

## 힌트

<iframe width="560" height="315" src="https://www.youtube.com/embed/t99KH0TR-J4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" style="box-sizing: border-box; border-radius: 0px !important;"></iframe>

<br>

## 📝 풀어보기

``` python
def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i]-col[x]) == x-i:
            return False
    return True

def dfs(x):
    global res
    if x == n:
        res += 1
        return
    for i in range(n):
        col[x] = i
        if check(x):
            dfs(x+1)

n = int(input())
res = 0
col = [0]*15

dfs(0)
print(res)
```

