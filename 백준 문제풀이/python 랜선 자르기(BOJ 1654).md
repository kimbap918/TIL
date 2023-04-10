## 파이썬 랜선 자르기(BOJ 1654)

<br>

## 문제

집에서 시간을 보내던 오영식은 박성원의 부름을 받고 급히 달려왔다. 박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.

이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다. 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)

편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다. 랜선의 길이는 231-1보다 작거나 같은 자연수이다.

<br>

## 출력

첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.

<br>

## 예제 입력 1

```
4 11
802
743
457
539
```

## 예제 출력 1

```
200
```

<br>

## 📝 풀어보기

랜선의 길이를 움직여서 랜선의 개수를 맞춰보기

![binary_search](../../binary_search.gif)

<br>

갖고있는 랜선의 개수 K, 만들어야하는 랜선의 개수 N을 입력받고

현재 보유중인 랜선의 길이를 저장한다.

가장 짧은 길이를 1, 가장 긴 길이를 보유중인 랜선의 최대값으로 설정한다.

``` python
import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
start, end = 1, max(lines)
```

<br>

이분 탐색 함수를 구현한다.

start가 end보다 크거나 같아질때까지 반복하면서, 보유중인 랜선을 차례대로 mid값에 나눠보고 

랜선이 만들어야하는 랜선의 개수보다 크거나 같으면 start를 mid + 1로 갱신 시키고

랜선이 맨들어야하는 랜선의 개수보다 작으면 end를 mid -1로 갱신 시킨다.

``` python
def binary_search(start, end):
    while start <= end:
        mid = (start+end)//2
        line = 0
        for i in lines:
            line += i // mid
        if line >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search(start, end))
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
start, end = 1, max(lines)

def binary_search(start, end):
    while start <= end:
        mid = (start+end)//2
        line = 0
        for i in lines:
            line += i // mid
        if line >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search(start, end))
```



