# 마크다운



## 제목/소제목(Heading)

#의 개수에 따라 h1 ~ h6까지 표현 가능하다.

### h3

#### h4

##### h5

###### h6



## 목록(List)

### 1. 순서가 없는 리스트 : -(hypen), *(asterisk)

- 사과
- 바나나
  - -> 엔터 후 탭
  - 미니 바나나
- 딸기
  - 산딸기
  - 들딸기
  - 바다딸기
- -> shift + tab시 단계 조절 가능

### 2. 순서가 있는 리스트 : 1.

아침에 일어나서 KDT 교육 듣기

1. 세수하고 양치
2. 산책
3. Syllaverse



## 코드블록

### 1. fenced Code block

- `(backtick) 기호 3개를 활용하여 작성한다
- 특정 언어를 명시하면 Syntax highlighting 기능이 적용된다.

```python
print('hello')

if True:
  print('t')
else:
  print('f')
```

```html
print('hello')
# 주석
<h1>
	제목
</h1>
<!-- 주석 -->
```

### 2. Inline Code block

`(backtick) 기호 두개로 원하는 것을 감싼다

`print`는 파이썬에서 출력하는 함수이다.



## 링크

1. 일반 링크 : [문자열]+(url)로 가능

[네이버](www.naver.com)

2. 이미지 링크 : ![문자열]+(url)로 가능

![image1](Markdown.assets/image1.png)



## 인용문

'>'를 통해 사용가능

> life is short, you need python 



## table(표) 

option + command + T

본문 -> 표 -> 표 삽입 

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |



## 텍스트

1. **볼드** : ****

2. *이텔릭* : **  

3. ~~취소선~~ : ~~~~

   

## 수평선

방법 1. `---`

방법 2. `___`

방법 3. `***`



