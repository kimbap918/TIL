# [문법] 파이썬 빠른 입출력(백준 BOJ 15552)

파이썬을 공부하다가 몰랐던 내용이 있어서 남긴다.



## input()대신 sys.stdin.readline()을 사용하기 💡 

이전에 풀었던 T(반복횟수)를 입력받고 A와 B를 입력받아 더하는 문제를 제출했던 내용이다.

``` python
T = int(input())
a = []
b = []

for i in range(T):
   A, B = map(int, input().split())
   a.append(A)
   b.append(B)

for i in range(T):
    print(a[i] + b[i])
```

보면 for 문에서 A, B를 입력받을 때 input()을 사용했는데 반복문으로 여러줄을 입력받는 상황에서는 이 방법이 좋지 못하다고 한다.

그래서 사용하는 문법이 **sys.stdin.readline()**이다.

다만, sys.stdin.readline()은 문자열을 저장하는 경우에 개행문자까지 같이 받기때문에 **.rstrip()** 를 추가해주는것이 좋다.



### 수정하기 📝

``` python
import sys

T = int(input())

for i in range(T):
   A, B = map(int, sys.stdin.readline().split())
   # map()은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수
   # 위와 같이 사용하면 a,b에 대해 각각 int형으로 형변환을 할수있다.
   print(A+B)
```

1. 먼저 sys.stdin.readline()을 사용하기 위해 **sys**를 import 했다.



![python1](/Users/mac/Desktop/python1.png)

2. 문제에서 입력과 출력 예제가 위와 같이 나와서 예시와 똑같이 나오게 하려고 입력을 모두 받고 배열에 담아서 출력하게끔 만들었는데 **입력 스트림과 출력 스트림은 달라서** 하나 입력 받고 하나 출력하는 방식으로 해도 문제 없다고한다. 그래서 수정했다.



## sys.stdin.readline()에 대한 추가적인 이야기 💬

1. 한개의 정수를 입력받을때

```python
import sys
a = int(sys.stdin.readline())
a = int(sys.stdin.readline().strip()) # strip() -> 개행문자를 제거
```

위와 같은 경우에 그냥  `a = sys.stdin.readline()` 로 하면

`sys.stdin.readline()`은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력받아진다.

만약 1 을 입력했다면, `1\n` 이 입력받아지기 때문에 개행문자를 제거해야 한다.

그리고 변수 타입이 문자열 형태(str)로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야한다.