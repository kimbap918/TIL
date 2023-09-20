## 파이썬 슈퍼마리오(백준 BOJ 2851)

<br>

## 문제

슈퍼 마리오 앞에 10개의 버섯이 일렬로 놓여져 있다. 이 버섯을 먹으면 점수를 받는다.

슈퍼 마리오는 버섯을 처음부터 나온 순서대로 집으려고 한다. 하지만, 모든 버섯을 집을 필요는 없고 중간에 중단할 수 있다. 중간에 버섯을 먹는 것을 중단했다면, 그 이후에 나온 버섯은 모두 먹을 수 없다. 따라서 첫 버섯을 먹지 않았다면, 그 이후 버섯도 모두 먹을 수 없다.

마리오는 받은 점수의 합을 최대한 100에 가깝게 만들려고 한다.

버섯의 점수가 주어졌을 때, 마리오가 받는 점수를 출력하는 프로그램을 작성하시오.

<br>

## 입력

총 10개의 줄에 각각의 버섯의 점수가 주어진다. 이 값은 100보다 작거나 같은 양의 정수이다. 버섯이 나온 순서대로 점수가 주어진다.

<br>

## 출력

첫째 줄에 마리오가 받는 점수를 출력한다. 만약 100에 가까운 수가 2개라면 (예: 98, 102) 마리오는 큰 값을 선택한다.

<br>

## 예제 입력 1

```
10
20
30
40
50
60
70
80
90
100
```

## 예제 출력 1

```
100
```

## 예제 입력 2

```
1
2
3
5
8
13
21
34
55
89
```

## 예제 출력 2

```
87
```

## 예제 입력 3

```
40
40
40
40
40
40
40
40
40
40
```

## 예제 출력 3 

```
120
```

<br>

## 📝 풀어보기

📌 먼저 입력받을 점수를 담을 리스트 `score_list`와, 동일한 차이의 점수가 생겼을 경우 큰 점수와 작은 점수 중 비교를 하기위한 변수 `sc_big`를 생성한다.

``` python
score_list = []
sc_big = 0
```

<br>

📌 10번의 반복동안, 점수를 입력받아 리스트에 담고, 입력받은 리스트의 합계값을 담을 변수 `sc` 를 선언한다.

``` python
for i in range(10):
  score_list.append(int(input()))
sc = sum(score_list)
```

<br>

📌 sc의 합계가 100 미만이면 그대로 출력하고 끝낸다.

그외에는 리스트의 역순으로 진행하면서 **sc가 100 이상인 경우** 리스트의 뒤에서부터 sc에 차감하며 **sc가 100과 같아지면** break한다. **sc가 100 이하로 떨어질 경우** sc_big에 sc값과 바로 직전의 리스트 값을 더해서 저장한다.

``` python
if sc <= 100:
  print(sc)
else:
  for j in range(9, -1, -1):
    if sc > 100:
      sc -= score_list[j]
    elif sc == 100:
      break
    else:
      sc_big = sc + score_list[j+1]
      break
```

<br>

📌 sc가 100인 경우에는 바로 100을 출력하고, 그외에는 sc에서 100을 뺀 절대값과 sc_big에서 100을 뺀 절대값을 비교해서 절대값이 더 작은쪽을 출력시킨다. 마리오는 가까운 수가 2개라면 큰 값을 선택하기 때문이다.

``` python
  if sc == 100:
    print(100)
  else:
    if abs(sc-100) >= abs(sc_big-100):
      print(sc_big)
    else:
      print(sc)
```

<br>

#### 전체코드

``` python
score_list = []
sc_big = 0

for i in range(10):
  score_list.append(int(input()))
sc = sum(score_list)

if sc <= 100:
  print(sc)
else:
  for j in range(9, -1, -1):
    if sc > 100:
      sc -= score_list[j]
    elif sc == 100:
      break
    else:
      sc_big = sc + score_list[j+1]
      break
  
  if sc == 100:
    print(100)
  else:
    if abs(sc-100) >= abs(sc_big-100):
      print(sc_big)
    else:
      print(sc)
```

