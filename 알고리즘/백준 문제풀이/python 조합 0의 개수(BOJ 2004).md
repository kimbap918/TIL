## 조합 0의 개수(백준 BOJ 2004)

<br>

## 문제

 (nm)$n \choose m$의 끝자리 0$0$의 개수를 출력하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 정수 n$n$, m$m$ (0≤m≤n≤2,000,000,000$0 \le m \le n \le 2,000,000,000$, n≠0$n \ne 0$)이 들어온다.

<br>

## 출력

첫째 줄에 (nm)$n \choose m$의 끝자리 0$0$의 개수를 출력한다.

<br>

## 예제 입력 1 

```
25 12
```

## 예제 출력 1 

```
2
```

<br>

## 📝 풀어보기

📌 끝자리가 0이 되는 값의 개수를 구하는 것이므로 10의 배수를 구한다.

10은 2와 5로 구성되어 있으므로 2의 개수와 5의 개수를 구하고 둘 중 더 작은 값이 10의 개수가 된다.

숫자의 개수를 셀 numCount함수를 생성한다.

반환값인 ans를 생성하고 a가 0이 될때까지 a를 num으로 나눈 몫을 다시 a에 넣고 반복시킨다.

 ``` python
 def numCount(a, num): 
     ans = 0
     while a != 0: # a가 0이 나올때까지 
         a = a//num # a를 num으로 나눈 몫 구하기 n : 25//5 = 5, 5//5 = 1, 1//5 = 0
                    # m : 12//5 = 2, 2//5 = 0
                    # n-m : 13//5 = 2, 2//5 = 0
         ans += a # 5 + 1 = 6, 2,  2
     return ans
 ```

<br>

📌  두 수 n, m을 입력받는다.

변수 five에 `numCount(n, 5), numCount(m, 5), numCount(n-m, 5)` 를 실행시킨 값을 빼서 저장하고 two에도 똑같이 저장한다.

`five, two` 중 최소값을 출력한다.  

``` python
n, m = map(int, input().split()) # 25, 12

five = numCount(n, 5) - numCount(m, 5) - numCount(n-m, 5) # 6 - 2 - 2
two = numCount(n, 2) - numCount(m, 2) - numCount(n-m, 2)

print(min(five, two))
```

<br>

#### 전체 코드

``` python
def numCount(a, num): 
    ans = 0
    while a != 0: # a가 0이 나올때까지 
        a = a//num # a를 num으로 나눈 몫 구하기 n : 25//5 = 5, 5//5 = 1, 1//5 = 0
                   # m : 12//5 = 2, 2//5 = 0
                   # n-m : 13//5 = 2, 2//5 = 0
        ans += a # 5 + 1 = 6, 2,  2
    return ans

# 끝자리가 0이라는 것은 10의 배수
# 10은 2와 5로 구성되어 있음
# 2와 5 짝이 맞아야 10이 되므로 2의 개수와 5의 개수중 더 작은게 10의 개수이다.
n, m = map(int, input().split()) # 25, 12

five = numCount(n, 5) - numCount(m, 5) - numCount(n-m, 5) # 6 - 2 - 2
two = numCount(n, 2) - numCount(m, 2) - numCount(n-m, 2)

print(min(five, two))
```

