## 파이썬 행렬 제곱(백준 BOJ 10830)

<br>

## 문제

크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

<br>

## 입력

첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

<br>

## 출력

첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.

<br>

## 예제 입력 1 

```
2 5
1 2
3 4
```

## 예제 출력 1 

```
69 558
337 406
```

## 예제 입력 2 

```
3 3
1 2 3
4 5 6
7 8 9
```

## 예제 출력 2 

```
468 576 684
62 305 548
656 34 412
```

## 예제 입력 3 

```
5 10
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
```

## 예제 출력 3

```
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
```

<br>

## 📝 풀어보기

앞서 행렬 곱셈을 풀었다면 행렬 곱셈과 분할정복을 이용하여 행렬 제곱을 풀 수 있다.

<br>

행렬의 결과값을 담을 리스트를 생성 후에 행렬 곱셈을 하는 함수를 만든다.

행렬 곱셈은 `res[i][j] 를 구할 때, 두 행렬 matrix_A[i][k] matrix_B[k][j]의 곱이다.`

여기서 결과값의 1000을 나눈 나머지를 저장한다.

``` python
import sys
input = sys.stdin.readline

def multiple_matrix(N, matrix_A, matrix_B):
  res = [list(0 for _ in range(N)) for _ in range(N)]
  
  # 행렬 곱셈
  for i in range(N):
    for j in range(N):
      for k in range(N):
        res[i][j] += matrix_A[i][k] * matrix_B[k][j]
    	res[i][j] %= 1000
  return res
```

<br>

분할 정복 함수를 생성한다. 인자는 크기(N), 제곱(B), 행렬(matrix)이다.

B가 1일땐, 제곱을 해도 값이 같으므로 행렬을 그대로 반환한다.

그외엔 분할정복으로 제곱을 2로 나는 몫을 사용해 divide_matrix 값을 저장하여

B의 나머지가 0일때, 0이 아닐때를 계산하면 된다.

``` python
def divide_matrix(N, B, matrix):
  if B == 1:
    return matrix
  else:
  	temp = divide_matrix(N, B//2, matrix)
  	if B%2 == 0:
    	return multiple_matrix(N, temp, temp)
  	else:
    	return multiple_matrix(N, multiple_matrix(N, temp, temp), matrix)
```

<br>

N, B를 입력받고 행렬 A를 입력받아 저장한다.

함수를 실행시켜 저장하고, 저장된 값에서 반복문을 통해 값을 출력한다.

마지막 출력에서도 %1000을 해주지 않으면, N = 2 B = 1

입력이 

1000 1000 

1000 1000

인 경우에 0을 배출하지 않고 1000을 배출하므로 마지막에 %1000을 해준다.

```python
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
res = divide_matrix(N, B, A)

for i in res:
  for j in i:
    print(j%1000, end=' ')
  print('')
```

<br>

### 전체코드

``` python
import sys
input = sys.stdin.readline

def multiple_matrix(N, matrix_A, matrix_B):
    res = [list(0 for _ in range(N)) for _ in range(N)]
    # 행렬 곱셈for i in range(N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += matrix_A[i][k] * matrix_B[k][j]
        		res[i][j] %= 1000
    return res

def divide_matrix(N, B, matrix):
    if B == 1:
        return matrix
    else:
        temp = divide_matrix(N, B//2, matrix)
        
        if B%2 == 0:
            return multiple_matrix(N, temp, temp)
        else:
            return multiple_matrix(N, multiple_matrix(N, temp, temp), matrix)
        
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
res = divide_matrix(N, B, A)

for i in res:
    for j in i:
        print(j%1000, end=' ')
    print('')    
```

