## 파이썬 택시 기하학(백준 BOJ 3053)

<br>

## 문제

19세기 독일 수학자 헤르만 민코프스키는 비유클리드 기하학 중 택시 기하학을 고안했다.

택시 기하학에서 두 점 T1(x1,y1), T2(x2,y2) 사이의 거리는 다음과 같이 구할 수 있다.

D(T1,T2) = |x1-x2| + |y1-y2|

두 점 사이의 거리를 제외한 나머지 정의는 유클리드 기하학에서의 정의와 같다.

따라서 택시 기하학에서 원의 정의는 유클리드 기하학에서 원의 정의와 같다.

원: 평면 상의 어떤 점에서 거리가 일정한 점들의 집합

반지름 R이 주어졌을 때, 유클리드 기하학에서 원의 넓이와, 택시 기하학에서 원의 넓이를 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 반지름 R이 주어진다. R은 10,000보다 작거나 같은 자연수이다.

<br>

## 출력

첫째 줄에는 유클리드 기하학에서 반지름이 R인 원의 넓이를, 둘째 줄에는 택시 기하학에서 반지름이 R인 원의 넓이를 출력한다. 정답과의 오차는 0.0001까지 허용한다.

<br>

## 예제 입력 1

```
1
```

## 예제 출력 1

```
3.141593
2.000000
```

## 예제 입력 2

```
21
```

## 예제 출력 2

```
1385.442360
882.000000
```

## 예제 입력 3 복사

```
42
```

## 예제 출력 3

```
5541.769441
3528.000000
```

<br>

## 힌트

유클리드 기하학: [한국어 위키](http://ko.wikipedia.org/wiki/유클리드_기하학) [영문 위키](http://en.wikipedia.org/wiki/Euclidean_geometry) [Wolfram Mathworld](http://mathworld.wolfram.com/EuclideanGeometry.html)

비유클리드 기하학: [한국어 위키](http://ko.wikipedia.org/wiki/비유클리드_기하학) [영문 위키](http://en.wikipedia.org/wiki/Non-Euclidean_geometry) [Wolfram Mathworld](http://mathworld.wolfram.com/Non-EuclideanGeometry.html)

택시 기하학: [한국어 위키](http://ko.wikipedia.org/wiki/택시기하학) [영문 위키](http://en.wikipedia.org/wiki/Taxicab_geometry) [Wolfram Mathworld](http://mathworld.wolfram.com/TaxicabMetric.html)

<br>

## 📝 풀어보기

``` python
import math
# 원의 넓이(원의 반지름) X (원의 반지름) X (원주율)
# 택시 기하학 원의 넓이 2 * r^2 
R = int(input())

print("{0:.6f}".format(R*R*math.pi))
print("{0:.6f}".format(2*R**2))
```

