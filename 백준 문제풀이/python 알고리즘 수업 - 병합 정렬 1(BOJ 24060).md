## 파이썬 알고리즘 수업 - 병합 정렬 1(백준 BOJ 24060)

<br>

## 문제

오늘도 서준이는 병합 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

*N*개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 *K* 번째 저장되는 수를 구해서 우리 서준이를 도와주자.

크기가 *N*인 배열에 대한 병합 정렬 의사 코드는 다음과 같다.

```
merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
    if (p < r) then {
        q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
        merge_sort(A, p, q);      # 전반부 정렬
        merge_sort(A, q + 1, r);  # 후반부 정렬
        merge(A, p, q, r);        # 병합
    }
}

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
merge(A[], p, q, r) {
    i <- p; j <- q + 1; t <- 1;
    while (i ≤ q and j ≤ r) {
        if (A[i] ≤ A[j])
        then tmp[t++] <- A[i++]; # tmp[t] <- A[i]; t++; i++;
        else tmp[t++] <- A[j++]; # tmp[t] <- A[j]; t++; j++;
    }
    while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
        tmp[t++] <- A[i++];
    while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
        tmp[t++] <- A[j++];
    i <- p; t <- 1;
    while (i ≤ r)  # 결과를 A[p..r]에 저장
        A[i++] <- tmp[t++]; 
}
```

<br>

## 입력

첫째 줄에 배열 A의 크기 *N*(5 ≤ *N* ≤ 500,000), 저장 횟수 *K*(1 ≤ *K* ≤ 108)가 주어진다.

다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

<br>

## 출력

배열 A에 *K* 번째 저장 되는 수를 출력한다. 저장 횟수가 *K* 보다 작으면 -1을 출력한다.

<br>

## 예제 입력 1 

```
5 7
4 5 1 3 2
```

## 예제 출력 1 

```
3
```

4 5 1 3 2 -> **4** 5 1 3 2 -> 4 **5** 1 3 2 -> **1** 5 1 3 2 -> 1 **4** 1 3 2 -> 1 4 **5** 3 2 -> 1 4 5 **2** 2 -> 1 4 5 2 **3** -> **1** 4 5 2 3 -> 1 **2** 5 2 3 -> 1 2 **3** 2 3 -> 1 2 3 **4** 3 -> 1 2 3 4 **5**. 총 12회 저장이 발생하고 일곱 번째 저장되는 수는 3이다.

## 예제 입력 2 

```
5 13
4 5 1 3 2
```

## 예제 출력 2 

```
-1
```

저장 횟수 12가 *K* 보다 작으므로 -1을 출력한다.

<br>

## 📝 풀어보기

위의 병합 정렬 의사코드를 파이썬에 맞게 옮겨 적는다. 

배열 A의 크기를 입력받고 저장횟수 K를 입력받는다. result의 기본값은 -1로 저장한다.

여기서 이 코드를 그대로 사용하면 시간초과가 발생하기 때문에 몇가지 수정을 한다.

merge 함수에 count, result를 전역변수로 지정한다. 지역변수로 설정하면 메모리와 시간을 차지한다.

merge_sort 함수의 if문에 and 조건으로 count와 K번째 수가 일치할 때 K번째 수를 저장할 수 있게 한다.

merge 함수의 결과를 A[p..r]에 저장하는 부분에서 count와 K가 같으면 결과값을 저장하고 빠져나오게 한다. break를 걸지 않으면 시간초과가 발생한다.

``` python
def merge_sort(A, p, r):
    # merge함수의 병합정렬 결과에 count증가와 
    # count와 K번째 수가 일치 할 경우 K번째 수를 저장한다.
    if(p < r and count <= K):
        q = (p + r) // 2 # q는 p, r의 중간 지점
        merge_sort(A, p , q) # 전반부 정렬
        merge_sort(A, q + 1, r) # 후반부 정렬
        merge(A, p, q, r) # 병합

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(A, p, q, r):
    # count. result를 전역변수로 설정, 지역변수로 설정시 메모리와 시간 차지
    global count, result
    i, j = p, q + 1 # i = p, j = q+1
    tmp = []
  
    while i <= q and j <= r:
        if(A[i] <= A[j]):
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    # 왼쪽 배열 부분이 남은 경우
    while i <= q:
        tmp.append(A[i])
        i += 1
    # 오른쪽 배열 부분이 남은 경우
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    i, t = p, 0
    # 결과를 A[p..r]에 저장
    while i <= r:
        A[i] = tmp[t]
        count += 1
        # K번째 수를 찾을 경우 리턴하는 코드를 추가
        # 루프 탈출을 하지 않으면 시간초과가 발생
        if count == K:
            result = A[i]
            break
        i += 1
        t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
result = -1
merge_sort(A, 0, N - 1)
print(result)
```

