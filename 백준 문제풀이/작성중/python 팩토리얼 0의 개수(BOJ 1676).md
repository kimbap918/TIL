## 파이썬 팩토리얼 0의 개수(BOJ 1676)

<br>

## 문제

N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

<br>

## 출력

첫째 줄에 구한 0의 개수를 출력한다.

<br>

## 예제 입력 1 

```
10
```

## 예제 출력 1 

```
2
```

## 예제 입력 2 

```
3
```

## 예제 출력 2 

```
0
```

<br>

## 📝 풀어보기

``` python
def factorial(x):
    if (x > 1):
        return x * factorial(x-1)
    else:
        return 1

N = int(input())
cnt = 0

for i in str(factorial(N))[::-1]: # 문자로 반환된 factorial(N)을 역순으로 세 가며 0이 나오지 않으면 멈춘다
    if i != '0':
        break
    cnt += 1
print(cnt)
```

