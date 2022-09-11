## 파이썬 N과 M(2)(BOJ 15650)

<br>

## 문제

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

<br>

## 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

<br>

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

<br>

## 예제 입력 1 

```
3 1
```

## 예제 출력 1 

```
1
2
3
```

## 예제 입력 2

```
4 2
```

## 예제 출력 2

```
1 2
1 3
1 4
2 3
2 4
3 4
```

## 예제 입력 3 

```
4 4
```

## 예제 출력 3

```
1 2 3 4
```

<br>

## 📝 풀어보기

📌 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열이고 수열은 오름차순이다.

N, M을 입력받고, 수열을 담을 리스트 arr을 생성한다.

``` python
N, M = map(int, input().split())
arr = []
```

<br>

📌 dfs 함수를 생성해서 `들어온 인자의 값부터 N+1의 범위`까지 반복하면서 arr에 i값이 없을 경우 arr에 i를 추가하고, i+1 값을 dfs 함수에 다시 실행시킨다. 그리고 arr의 마지막 값은 꺼낸다.

arr의 길이가 M과 같을 경우에는 arr 내의 값을 공백과 함께 출력하고 반환한다. 

``` python
def dfs(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, N+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()
dfs(1)
```

<br>

#### 전체코드

``` python
N, M = map(int, input().split())
arr = []

def dfs(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, N+1): # 시작지점을 i+1지점부터 
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()
dfs(1)
```

