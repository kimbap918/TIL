## 파이썬 구간 합 구하기 4(백준 BOJ 11659)

<br>

## 문제

수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

<br>

## 출력

총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

<br>

## 제한

- 1 ≤ N ≤ 100,000
- 1 ≤ M ≤ 100,000
- 1 ≤ i ≤ j ≤ N

<br>

## 예제 입력 1 복사

```
5 3
5 4 3 2 1
1 3
2 4
5 5
```

## 예제 출력 1 복사

```
12
9
1
```

<br>

## 📝 풀어보기

📌 시간초과 방지를 위해 readline을 사용한다.

수의 개수 N과 합을 구해야하는 개수 M을 입력받고 arr에 수의 개수만큼 입력한다.

이 문제는 수의 범위가 넓으므로 구할때마다 arr의 인덱스를 찾아 합산을 하면 시간초과가 발생한다. 그러므로 합산을 한 값을 미리 리스트에 담아두고 찾는 방식을 사용한다.

arr의 요소를 반복하면서 temp에 arr 요소의 값을 누적시키고 구간 합의 값을 미리 prefix_sum에 저장한다.

M의 범위만큼 반복하면서 구해야하는 구간 n, m을 입력받고 prefix_sum[m] - prefix_sum[n-1]를 출력한다.

``` python
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in arr:
    temp += i
    prefix_sum.append(temp) # 구간 합의 값을 미리 저장해둠


for j in range(M):
    n, m = map(int, input().split())
    print(prefix_sum[m] - prefix_sum[n-1])
```

