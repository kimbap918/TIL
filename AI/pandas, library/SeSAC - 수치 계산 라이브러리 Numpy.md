## SeSAC - 수치 계산 라이브러리 Numpy

<br>

### Numpy?

수치 해석용 파이썬 패키지

다차원의 배열 자료구조를 다룰 수 있으며, 백터와 행렬을 사용하는 선형대수 계산에 주로 사용 → 머신러닝에서 필수

<br>

### numpy의 행렬

```python
 import numpy as np
```

- np.array : 행렬로 변환

```python
import numpy as np

array1 = np.array([1,2,3])
print(type(array1))
print(array1.shape)

->
<class 'numpy.ndarray'>
(3,)
```

위 코드는 리스트를 행렬로 변환했다.

행렬과 리스트의 차이는?

```python
# [1,2,3] + 3을 실행하면?
# 리스트에서는 에러가 난다.

np.array([1,2,3]) + 3
# 행렬에 3을 더하면 동시에 모든 값에 3이 더해진다. 
```

```python
# 2차원 행렬
array2 = np.array([[1,2,3], [4,5,6]])
print(type(array2))
print(array2.shape)

->
<class 'numpy.ndarray'>
(2, 3)
```

- ndim : 차원 확인

```python
print(array1.ndim)
print(array2.ndim)

->
1
2
```

- 데이터 타입 확인

```python
list1 = [1,2,3]
print(type(list1))
print(type(array1))
print(type(array1))
print(array1, array1.dtype)

->
<class 'list'>
<class 'numpy.ndarray'>
<class 'numpy.ndarray'>
[1 2 3] int64
```

```python
# 문자열이 포함될 경우 
list2 = [1,2,3, 'test']
array2 = np.array(list2)
print(array2, array2.dtype)

-> 
# 모두 문자열로 바뀐다.
['1' '2' '3' 'test'] <U21

# astype로 변환이 가능하다.
array_int = np.array([1,2,3])
# int32, int64
array_float = array_int.astype('float64')
print(array_float, array_float.dtype)

-> 
[1. 2. 3.] float64

# 만약 실수를 정수로 바꿀 경우 뒤의 소수점이 전부 버림처리된다.
```

<br>

### 행렬 생성하기

- np.arrange : 행렬 편리하게 생성하기

```python
sequence_array = np.arange(10)
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)

->
[0 1 2 3 4 5 6 7 8 9]
int64 (10,)
```

- zeros : 0으로 채워진 행렬 만들기
- ones : 1로 채워진 행렬 만들기

```python
# (3,2) -> 3행 2열
zero_array = np.zeros((3,2), dtype='int32')
# one_array = np.ones((3,2), dtype='int32')
print(zero_array)
print(zero_array.dtype, zero_array.shape)

->
[[0 0]
 [0 0]
 [0 0]]
int32 (3, 2)
```

- reshape : 차원바꾸기
- 단, 개수가 같아야 한다.

```python
array1 = np.arange(10)
print('array1:\n', array1)

array2 = array1.reshape(2,5)
print('array2:\n', array2)

->
array1:
 [0 1 2 3 4 5 6 7 8 9]
array2:
 [[0 1 2 3 4]
 [5 6 7 8 9]]

# 3차원으로 변경
array1 = np.arange(8)
print('array1:\n', array1)

array3d = array1.reshape(2,2,2)
print('array3d:\n', array3d.tolist())

->
array1:
 [0 1 2 3 4 5 6 7]
array3d:
 [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
```

- 인덱싱

```python
array1 = np.arange(start=1, stop=10)
print('array1', array1)

value = array1[2]
print('value', value)

->
array1 [1 2 3 4 5 6 7 8 9]
value 3

# 값 바꾸기
array1[0] = 9
array1[8] = 0

# 슬라이싱
array2 = array[:3]
```

- 불리언 인덱싱

```python
array1d = np.arange(start=1, stop=10)
array3 = array1d[array1d > 5]
print(array3)

->
[6 7 8 9]
```

<br>

### 행렬 정렬

- sort()

```python
org_array = np.array([3, 1, 9, 5])
print('원본 행렬', org_array)
sort_array1 = np.sort(org_array)
print(sort_array1)

->
[3 1 9 5]
[1 3 5 9]
```

- sort()의 axis 값 설정

```python
array2d = np.array([[8, 12], [7, 1]])
# axis = 0 행방향
# axis = 1 열방향
sort_array2d_axis = np.sort(array2d, axis=0)
print(sort_array2d_axis)

->
[[ 7  1]
 [ 8 12]]
# 열방향(1) ->
[[8 12]
[1 7]]
```

- argsort()

```python
org_array = np.array([3, 1, 9, 5])
sort_indices = np.argsort(org_array)
print(sort_indices)

->
# 정렬된 인덱스 값을 가져옴
# 정렬된 [1, 3, 5, 9]의 인덱스 값
[1 0 3 2]
```

<br>

### 행렬 내적

- 행렬끼리의 곱셈

```python
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])
dot_product = np.dot(A,B)
print(dot_product)

->
[[ 58  64]
 [139 154]]

# (1 2 3  * (7 8
# 4 5 6)		 9 10
# 					 11 12)
```

<br>

### 전치 행렬

- 행과 열 바꾸기

```python
A = np.array([[1, 2], [3, 4]])
transpose_mat = np.transpose(A)
print(transpose_mat)

[[1 3]
 [2 4]]
```