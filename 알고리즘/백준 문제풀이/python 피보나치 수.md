## 파이썬 피보나치 수 풀이

<br>

### 피보나치 수열?

피보나치 수열(Fibonacci Sequence)는 **상당히 단순한 단조 증가(monotonically increasing) 수열로 0번째 항은 0, 1번째 항은 1, 그 외 항은 전번, 전전번 항의 합으로 표현된다.**

> F*0* = 0
>
> F*1* = 1
>
> F*n* = F*n-1* + F*n-2*

1 1 2 3 5 8 13 21 34 55 ...

위의 숫자들은 피보나치 수열을 10까지 적어놓은것이다. 위 설명대로 0번째 항은 0, 1번째 항은 1, 2번째 항부턴 전번, 전전번 항의 합으로 표현되고 있다.

<br>

### 피보나치 수 5(BOJ 10870)

0이상의 정수, N이 주어질 때, N번째 피보나치 수를 구해보자.

일반적인 피보나치 수를 푸는 방법은 다음과 같다.

``` python
# 일반적인 피보나치 수 (피보나치 수 5 boj 10870)
 def fib(N):
     res = 0 
     if N < 2:
         return N
     else:
         res = fib(N-1) + fib(N-2)
         return res
```

N이 2번째 수열 미만일때는 N을 그대로 리턴하고

그외엔 res에 N의 전번, 전전번을 fib함수로 더해서 반환한다.

이 방법은 적은 수에서는 문제없이 작동하겠지만, 함수가 한번 호출되면 다시 두 번 호출되기 때문에 시간복잡도가 O(2^N)이 된다.

<br>

### 피보나치 수 (BOJ 2747)

'메모이제이션 사용'

위의 코드에서 문제점은 이항계수3(BOJ 11401)때 언급한 것과 같이 부분 문제의 중복(overlapping subproblems)에 있다.

위 코드에서 N = 5를 입력하면 함수 안에서는 fib(4) + fib(3)이 실행될테고, 또 각각의 fib(3) + fib(2), fib(2) + fib(1) 이 실행될것이다. fib(3)에서도 fib(2) + fib(1)이 실행된다. 

5를 입력해도 함수 안에서 같은 부분이 중복되어 실행되는것이 보인다.

이를 해결하기 위해 부분 문제를 해결할때 마다 그걸 저장하고, 필요할때 가져다 쓸 수 있는 메모이제이션을 사용한다.

```python
# 2747 피보나치 수
memo = [0 for _ in range(45+1)]
memo[1] = 1

def fib(N):    
    if N <= 1:
        return N
    elif memo[N] != 0:
        return memo[N]
    else:
        memo[N] = fib(N-1) + fib(N-2)
        return memo[N] 
```

문제에서 N의 범위는 45까지이다. N번째 피보나치 수를 저장할 배열을 만들어놓고, 1번째 항에 1을 저장해둔다.

그외엔 이전과 아주 비슷하다.  N이 1보다 작거나 같으면 N을 반환하고 저장된 N번째 항의 값이 0이 아니면 N번째 항을 반환한다.

그외엔 N번째 항에 피보나치 수를 계산한 값을 저장하고 N번째 항을 반환한다.

이 방법을 사용하면 시간복잡도는 O(N)이 된다.

<br>

### 피보나치 수 2(BOJ 2748)

더 넓은 범위의 피보나치 수, 메모이제이션 사용.

더 넓은 범위의 피보나치 수다. 여기서 N은 90까지 주어진다.

하지만 이 문제도 위의 메모이제이션으로 쉽게 풀 수 있다.

```python
# 2748 피보나치 수 2
def fib(N):
    memo = [0, 1]
    if N < 2:
        return N
    else:
        for i in range(2, N+1):
            memo.append(memo[i-1] + memo[i-2])
        return memo[N]
```

 <br>

### 피보나치 수 3(BOJ 2749)

피사노 주기(Pisano Period) 사용

> 피보나치 수를 K로 나눈 나머지는 항상 주기를 갖게된다

| n       | 0     | 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8    | 9    | 10   | 11   | 12   | 13   | 14   | 15   |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Fn      | 0     | 1     | 1     | 2     | 3     | 5     | 8     | 13    | 21   | 34   | 55   | 89   | 144  | 233  | 377  | 610  |
| Fn mod3 | **0** | **1** | **1** | **2** | **0** | **2** | **2** | **1** | *0*  | *1*  | *1*  | *2*  | *0*  | *2*  | *2*  | *1*  |

주기의 길이가 P 이면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같다.

M = 10^k 일 때, k > 2 라면, 주기는 항상 15 × 10^k-1 이 된다. 

이 사실을 모른다고 해도, 주기를 구하는 코드를 이용해서 문제를 풀 수 있다.

```python
# 2749 피보나치 수 3
mod = 1000000
p = mod//10*15
memo = [0, 1]
def fib(N):
    if N < 2:
        return N
    else:
        for i in range(2, p):
            memo.append(memo[i-1] + memo[i-2])
            memo[i] %= mod
        return memo[N]
N = int(input())
print(fib(N%p))
```

M = 10^6 이기 때문에, 주기는 15 × 10^5 = 1500000가 된다.

이 문제의 N은 1,000,000,000,000,000,000으로 매우매우 크다. 이때 까지 했던 위의 방법이라면 컴퓨터가 멈춰버릴것이다.

그렇기 때문에 위에서 살펴본 피사노 주기와, 메모이제이션을 같이 사용해서 문제를푼다.

코드가 그렇게 어렵지는 않다.

이 문제에서는 N번째 피보나치 수를 1,000,000으로 나누어야 하므로 해당 값을 저장해 두고, 주기값을 저장해둔다.

메모이제이션을 하기 위한 배열 또한 저장해둔다.

N이 2미만이면 N을 리턴하고 그외엔 2부터 p까지 배열에 피보나치 수를 1,000,000을 나눈 나머지값을 저장하고 리턴해준다. 

<br>

### 피보나치 수 6(BOJ 11444)

행렬 곱셈, 분할 정복 이용

이항계수(BOJ 11401), 행렬 곱셈(BOJ 2740)에서 사용했던 분할 정복과 행렬 곱셈을 이용하여 피보나치 수를 구하는 방법이다.

n번째 피보나치 수를 F*n*이라고 할 때, 피보나치 수를 아래와 같이 행렬화 할 수 있다.

![fibonacci]({{site.baseurl}}/images/fib.png) 

이 식을 통하면 오른쪽 행렬을 *n* 번 제곱하면 나오는 행렬의 [0, 1] 또는 [1, 0] 값이 F*n*이 된다. 즉, 행렬 곱셈을 통해 피보나치 수를 구할 것이다.

```python
import sys
input = sys.stdin.readline

N = int(input())
# 곱셈을 시작해 나갈 기본 행렬
matrix = [[1, 1], [1, 0]]

# 행렬 곱셈
def multiple_matrix(matrix_A, matrix_B):
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += matrix_A[i][k] * matrix_B[k][j] % 1000000007
    return res

# 분할 정복
def nth(A, B):
    if B == 1:
        return A
    else:
        # a^(B//2)
        temp = nth(A, B//2)
        if B % 2 == 0:
            return multiple_matrix(temp, temp)
        else:
            return multiple_matrix(multiple_matrix(temp, temp), A)

res = nth(matrix, N)

print(res[0][1] % 1000000007)
```

N을 입력받고, 곱셈을 시작해 나갈 기본 행렬을 저장해 둔다.

이 문제는 너비와 길이가 같은 정방형의 행렬만 취급하기 때문에 간단히 행렬곱셈을 구현할 수 있다.

`res[i][j] += matrix_A[i][k] * matrix_B[k][j]`

여기에 1,000,000,007을 나눈 값을 저장한다.

들어온 matrix를 분할 정복으로 거듭제곱 해준다. 들어온 N이 1이면 matrix를 반환한다. 

res의 `[0][1]`이 F*n* 이므로 해당 값에 1,000,000,007을 나눈 나머지를 출력한다

해당 방법으로 행렬의 거듭제곱 형태로 풀게되면 시간 복잡도는 O(logN)이 된다.
