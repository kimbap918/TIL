## SeSAC - 데이터 분석 기초 2일차

2023.07.19

---

### pandas documentation

[User Guide — pandas 2.0.3 documentation](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)

<br>

### 03-1 행 삭제하기

```python
# 인덱스 0, 1 행을 drop
ns_book2 = ns_book.drop([0,1])
ns_book2.head()
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 3 | 나도 한 문장 잘 쓰면 바랄 게 없겠네 | 김선영 지음 | 블랙피쉬 | 2021 | 9788968332982 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 3 | 4 | 예루살렘 해변 | 이도 게펜 지음, 임재희 옮김 | 문학세계사 | 2021 | 9788970759906 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 4 | 5 | 김성곤의 중국한시기행 : 장강·황하 편 | 김성곤 지음 | 김영사 | 2021 | 9788934990833 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 5 | 6 | 처음 읽는 음식의 세계사 | 미야자키 마사카츠 지음, 한세희 옮김 | 탐나는책 | 2021 | 9791189550370 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 6 | 7 | 아르센 벵거 자서전 My Life in Red and White | 아르센 벵거 지음, 이성모 옮김 | 한즈미디어(한스미디어) | 2021 | 9791160075793 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |

```python
# 2번째 행부터 잘라내서 ns_book2에 저장
ns_book2 = ns_book[2:]
ns_book2.head()
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 3 | 나도 한 문장 잘 쓰면 바랄 게 없겠네 | 김선영 지음 | 블랙피쉬 | 2021 | 9788968332982 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 3 | 4 | 예루살렘 해변 | 이도 게펜 지음, 임재희 옮김 | 문학세계사 | 2021 | 9788970759906 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 4 | 5 | 김성곤의 중국한시기행 : 장강·황하 편 | 김성곤 지음 | 김영사 | 2021 | 9788934990833 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 5 | 6 | 처음 읽는 음식의 세계사 | 미야자키 마사카츠 지음, 한세희 옮김 | 탐나는책 | 2021 | 9791189550370 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 6 | 7 | 아르센 벵거 자서전 My Life in Red and White | 아르센 벵거 지음, 이성모 옮김 | 한즈미디어(한스미디어) | 2021 | 9791160075793 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |

```python
# 0번째 인덱스부터 2번째 인덱스까지 잘라내서 ns_book2에 저장
ns_book2 = ns_book[0:2]
ns_book2.head()
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 인공지능과 흙 | 김동훈 지음 | 민음사 | 2021 | 9788937444319 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 1 | 2 | 가짜 행복 권하는 사회 | 김태형 지음 | 갈매나무 | 2021 | 9791190123969 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |

```python
# ns_df의 '출판사'가 '한빛미디어'에 해당하는지 여부, bool값을 selected_rows에 저장
selected_rows = ns_df['출판사'] == '한빛미디어'
ns_book2 = ns_book[selected_rows]
ns_book2.head()
```

- 여기서 selected_rows를 따로 출력해보면 다음과 같다.

```
0         False
1         False
2         False
3         False
4         False
          ...  
401677    False
401678    False
401679    False
401680    False
401681    False
Name: 출판사, Length: 401682, dtype: bool
```

selected_rows에 담기는 정보는 해당 인덱스의 도서 ‘출판사’가 ‘한빛미디어’에 해당하는지 여부, boolean값을 담고있다.

```
ns_book2 = ns_book.loc[selected_rows]
ns_book2.head()
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 60 | 61 | (맛있는 디자인)프리미어 프로 CC: 쉽게 배워 제대로 써먹는 유튜브 영상 편집 | 정지원,심수진,윤성우,김덕영 지음 | 한빛미디어 | 2021 | 9791162244029 | NaN | 1 | 2021 | 005.567 | 1 | 1 | 2021-03-15 |
| 70 | 71 | 처음 배우는 애저 (Azure Portal로 배우는 애저 도입부터 활용까지) | 김도균 | 한빛미디어 | 2020 | 9791162243695 | NaN | NaN | NaN | 005.74 | 1 | 1 | 2021-03-15 |
| 88 | 89 | 맛있는 디자인 프리미어 프로 CC 2021 - 쉽게 배워 제대로 써먹는 유튜브 영상 편집 | 정지원, 심수진, 윤성우, 김덕영 (지은이) | 한빛미디어 | 2021 | 9791162244029 | NaN | NaN | NaN | NaN | 0 | 0 | 2021-03-15 |
| 156 | 157 | 실전 보고서 작성 기술 with 파워포인트, 워드, 한글 | 홍장표 지음 | 한빛미디어 | 2020 | 9791162243763 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-12 |
| 198 | 199 | 처음 배우는 리액트 네이티브 | 김범준 지음 | 한빛미디어 | 2021 | 9791162243879 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-12 |

```python
# 대출건수 칼럼의 값이 1000 초과인값만 저장
ns_book2 = ns_book[ns_book['대출건수'] > 1000]
ns_book2.head()
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 94781 | 94782 | 사피엔스 :유인원에서 사이보그까지, 인간 역사의 대담하고 위대한 질문 | 유발 하라리 지음 ;조현욱 옮김 | 김영사 | 2016 | 9788934972464 | NaN | NaN | NaN | 909 | 30 | 1468 | 2016-04-22 |
| 346944 | 346945 | 해커스 토익:Listening | David Cho 지음 | 해커스어학연구소 | 2005 | 9788990700148 | NaN | 1 | NaN | 740.77 | 29 | 1065 | 2005-02-01 |

<br>

### 중복된 행 찾기

```python
# 전체에서 중복된 값을 찾아 sum
sum(ns_book.duplicated())

-> 0
```

```python
# 특정칼럼. 도서명, 저자, ISBN이 중복된 값을 찾아 sum 
sum(ns_book.duplicated(subset=['도서명', '저자', 'ISBN']))

-> 22096
```

```python
# keep : 중복된 대상을 어떻게 표기할 것인지에 대한 파라미터
# first : (default) 중복되는 대상이 처음 나올 때, False로 처리하고, 이후 중복 값들은 모두 True로 반환
# last : 중복되는 대상이 마지막으로 나왔을 때만, 중복을 나타내는 True를 반환하고, 전에 나왔던 중복 값들은 False로 반환
# False : 모든 중복되는 대상을 True로 반환
dup_rows = ns_book.duplicated(subset=['도서명', '저자', 'ISBN'], keep=False)
ns_book3 = ns_book[dup_rows]
ns_book3.head()
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109 | 110 | 파친코 | 이민진 지음 ;이미정 옮김 | 문학사상 | 2018 | 9788970129815 | 9788970129808 | 0 | 1 | 843.6 | 1 | 0 | 2021-03-12 |
| 110 | 111 | 파친코 | 이민진 지음 ;이미정 옮김 | 문학사상 | 2018 | 9788970129822 | 9788970129808 | 0 | 2 | 843.6 | 1 | 0 | 2021-03-12 |
| 111 | 112 | 보건교사 안은영 :정세랑 장편소설 | 지은이: 정세랑 | 민음사 | 2021 | 9788937479953 | NaN | 0 | NaN | 813.7 | 1 | 0 | 2021-03-12 |
| 112 | 113 | 보건교사 안은영 :정세랑 장편소설 | 지은이: 정세랑 | 민음사 | 2021 | 9788937479953 | NaN | 0 | NaN | 813.7 | 1 | 1 | 2021-03-12 |
| 113 | 114 | 스토너 | 존 윌리엄스 지음 ;김승욱 옮김 | RHK(알에이치코리아) | 2021 | 9788925538297 | NaN | 0 | NaN | 843.5 | 1 | 0 | 2021-03-12 |

```python
count_df = ns_book[['도서명', '저자', 'ISBN', '권', '대출건수']]
```

```python
# count_df에 대해, 도서명, 저자, ISBN, 권 으로 묶는다(groupby)
group_df = count_df.groupby(by=['도서명', '저자', 'ISBN', '권'], dropna=False)
```

```python
loan_count = count_df.groupby(by=['도서명', '저자', 'ISBN', '권'], dropna=False).sum()
# print(loan_count)
loan_count.head()
```

|  |  |  |  | 대출건수 |
| --- | --- | --- | --- | --- |
| 도서명 | 저자 | ISBN | 권 |  |
| (꼭 필요한 것부터 쉽게 배우는) 자신만만 블로그 차근차근 배우기 | 김상현 지음 | 9788955025637 | NaN | 38 |
| (맨처음 배우는) 세상의 직업 | 엘레오노라 바르소티 글 ·그림 ;김태은 옮김 | 9788992924146 | NaN | 10 |
| (영잘원 리스닝과 패턴 영어의 절묘한 만남으로 태어난 ) 리스닝 ABC : 입문편 | JD Kim 지음 | 9788993466089 | NaN | 4 |
| (즉석에서 바로바로 활용하는) 일상생활 베트남어 첫걸음 | FL4U컨텐츠 지음 | 9788971728000 | NaN | 3 |
| ,에게 | 이기린(이진희) | 9791196137014 | NaN | 0 |
- 여기서, loan_count를 출력하면 다음과 같다.
- ['도서명', '저자', 'ISBN', '권', '대출건수']를 저장한 **count_df에 대해** [도서명, 저자, ISBN, 권]을 기준으로 그룹화 하고, '대출건수' 열을 합산해서 새로운 데이터프레임을 생성한다.

```
대출건수
도서명                                             저자                       ISBN          권        
 (꼭 필요한 것부터 쉽게 배우는) 자신만만 블로그 차근차근 배우기           김상현 지음                   9788955025637 NaN    38
 (맨처음 배우는) 세상의 직업                               엘레오노라 바르소티 글 ·그림 ;김태은 옮김 9788992924146 NaN    10
 (영잘원 리스닝과 패턴 영어의 절묘한 만남으로 태어난 ) 리스닝 ABC : 입문편  JD Kim 지음                9788993466089 NaN     4
 (즉석에서 바로바로 활용하는) 일상생활 베트남어 첫걸음                 FL4U컨텐츠 지음               9788971728000 NaN     3
 ,에게                                            이기린(이진희)                 9791196137014 NaN     0
...                                                                                          ...
NaN                                             히라야마 쯔요시 외 5인            9788997924318 NaN     0
                                                ？德峰(Yang Defeng)         9788960716957 NaN     0
                                                NaN                      9788971990155 NaN     2
                                                                         9788972803997 NaN     0
                                                                         9788973561537 NaN     0

[384591 rows x 1 columns]
```

```python
# 여기에는 False 혹은 True가 담겨있다.
dup_rows = ns_book.duplicated(subset=['도서명', '저자', 'ISBN', '권'])
# ~ : NOT, Inverse
# dup_rows의 True가 아닌것. 즉, 중복이 아닌것들이 unique_rows에 들어있다.
unique_rows = ~dup_rows
# ns_book3에는 중복값을 빼고 unique 값만 들어있다.
ns_book3 = ns_book[unique_rows].copy()
```

- 중복 확인

```python
sum(ns_book3.duplicated(subset=['도서명', '저자', 'ISBN', '권']))

-> 0
```

```python
# '도서명', '저자', 'ISBN', '권'을 하나의 인덱스로 만든다.
ns_book3.set_index(['도서명', '저자', 'ISBN', '권'], inplace=True)
ns_book3.head()
```

|  |  |  |  | 번호 | 출판사 | 발행년도 | 세트 ISBN | 부가기호 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 도서명 | 저자 | ISBN | 권 |  |  |  |  |  |  |  |  |  |
| 인공지능과 흙 | 김동훈 지음 | 9788937444319 | NaN | 1 | 민음사 | 2021 | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 가짜 행복 권하는 사회 | 김태형 지음 | 9791190123969 | NaN | 2 | 갈매나무 | 2021 | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 나도 한 문장 잘 쓰면 바랄 게 없겠네 | 김선영 지음 | 9788968332982 | NaN | 3 | 블랙피쉬 | 2021 | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 예루살렘 해변 | 이도 게펜 지음, 임재희 옮김 | 9788970759906 | NaN | 4 | 문학세계사 | 2021 | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 김성곤의 중국한시기행 : 장강·황하 편 | 김성곤 지음 | 9788934990833 | NaN | 5 | 김영사 | 2021 | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |

```python
# loan_count 데이터프레임을 가지고 ns_book3 데이터프레임을 업데이트
# SQL의 inner join과 같다.
ns_book3.update(loan_count)
ns_book3.head()
```

```sql
// SQL의 inner join으로 표현하면 다음과 같다.(이것은 예시로, 정확하지 않을 수 있다.)
SELECT *
FROM ns_book3
INNER JOIN loan_count
ON ns_book3.common_column = loan_count.common_column;
```

|  |  |  |  | 번호 | 출판사 | 발행년도 | 세트 ISBN | 부가기호 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 도서명 | 저자 | ISBN | 권 |  |  |  |  |  |  |  |  |  |
| 인공지능과 흙 | 김동훈 지음 | 9788937444319 | NaN | 1 | 민음사 | 2021 | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 가짜 행복 권하는 사회 | 김태형 지음 | 9791190123969 | NaN | 2 | 갈매나무 | 2021 | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 나도 한 문장 잘 쓰면 바랄 게 없겠네 | 김선영 지음 | 9788968332982 | NaN | 3 | 블랙피쉬 | 2021 | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 예루살렘 해변 | 이도 게펜 지음, 임재희 옮김 | 9788970759906 | NaN | 4 | 문학세계사 | 2021 | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 김성곤의 중국한시기행 : 장강·황하 편 | 김성곤 지음 | 9788934990833 | NaN | 5 | 김영사 | 2021 | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
- SQL의 JOIN

[SQL 기본 문법: JOIN(INNER, OUTER, CROSS, SELF JOIN)](https://hongong.hanbit.co.kr/sql-기본-문법-joininner-outer-cross-self-join/)

```python
# ns_book3의 인덱스를 초기화
ns_book4 = ns_book3.reset_index()
ns_book4.head()
```

|  | 도서명 | 저자 | ISBN | 권 | 번호 | 출판사 | 발행년도 | 세트 ISBN | 부가기호 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 인공지능과 흙 | 김동훈 지음 | 9788937444319 | NaN | 1 | 민음사 | 2021 | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 1 | 가짜 행복 권하는 사회 | 김태형 지음 | 9791190123969 | NaN | 2 | 갈매나무 | 2021 | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 2 | 나도 한 문장 잘 쓰면 바랄 게 없겠네 | 김선영 지음 | 9788968332982 | NaN | 3 | 블랙피쉬 | 2021 | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 3 | 예루살렘 해변 | 이도 게펜 지음, 임재희 옮김 | 9788970759906 | NaN | 4 | 문학세계사 | 2021 | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 4 | 김성곤의 중국한시기행 : 장강·황하 편 | 김성곤 지음 | 9788934990833 | NaN | 5 | 김영사 | 2021 | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |

```python
sum(ns_book['대출건수'] > 100)

-> 2311

sum(ns_book4['대출건수'] > 100)

-> 2550
```

```python
ns_book4 = ns_book4[ns_book.columns]
ns_book4.head()
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 인공지능과 흙 | 김동훈 지음 | 민음사 | 2021 | 9788937444319 | NaN | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 1 | 2 | 가짜 행복 권하는 사회 | 김태형 지음 | 갈매나무 | 2021 | 9791190123969 | NaN | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 2 | 3 | 나도 한 문장 잘 쓰면 바랄 게 없겠네 | 김선영 지음 | 블랙피쉬 | 2021 | 9788968332982 | NaN | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 3 | 4 | 예루살렘 해변 | 이도 게펜 지음, 임재희 옮김 | 문학세계사 | 2021 | 9788970759906 | NaN | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 4 | 5 | 김성곤의 중국한시기행 : 장강·황하 편 | 김성곤 지음 | 김영사 | 2021 | 9788934990833 | NaN | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |

```python
ns_book4.to_csv('ns_book4.csv', index=False)
```

```python
def data_cleaning(filename):
  # 파일을 데이터프레임으로 읽음
  ns_df = pd.read_csv(filename, low_memory=False)
  # NaN인 열 삭제
  ns_book = ns_df.dropna(axis=1, how='all')

  # 대출 건수를 합치기 위해 행만 추출하여 count_df 데이터프레임을 만든다.
  count_df = ns_book[['도서명', '저자', 'ISBN', '권', '대출건수']]
  # 도서명, 저자, ISBN, 권을 기준으로 대출건수를 그룹바이
  loan_count = count_df.groupby(by=['도서명', '저자', 'ISBN', '권'], dropna=False).sum()
  # 원본 데이터프레임에서 중복된 행을 제외하고 고유한 행만 추출하여 복사
  dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN','권'])
  unique_rows = ~dup_rows
  ns_book3 = ns_book[unique_rows].copy()
  # 도서명, 저자, ISBN, 권을 인덱스로 설정합
  ns_book3.set_index(['도서명','저자','ISBN','권'], inplace=True)
  # load_count에 저장된 누적 대출건수를 업데이트
  ns_book3.update(loan_count)
  
  # 인덱스 재설정
  ns_book4 = ns_book3.reset_index()
  # 원본 데이터프레임의 열 순서로 변경
  ns_book4 = ns_book4[ns_book.columns]
  
  return ns_book4
```

```python
new_ns_book4 = data_cleaning('ns_202104.csv')

ns_book4.equals(new_ns_book4)
```

<br>

### 03-2 잘못된 데이터 수정하기

<br>

### 데이터프레임 정보 요약 확인하기

```python
import gdown

gdown.download('https://bit.ly/3GisL6J', 'ns_book4.csv', quiet=False)
```

```
Downloading...
From: https://bit.ly/3GisL6J
To: /content/ns_book4.csv
100%|██████████| 55.5M/55.5M [00:00<00:00, 107MB/s]
'ns_book4.csv
```

```python
import pandas as pd

ns_book4 = pd.read_csv('ns_book4.csv', low_memory=False)
ns_book4.head()
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 인공지능과 흙 | 김동훈 지음 | 민음사 | 2021 | 9788937444319 | NaN | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 1 | 2 | 가짜 행복 권하는 사회 | 김태형 지음 | 갈매나무 | 2021 | 9791190123969 | NaN | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 2 | 3 | 나도 한 문장 잘 쓰면 바랄 게 없겠네 | 김선영 지음 | 블랙피쉬 | 2021 | 9788968332982 | NaN | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 3 | 4 | 예루살렘 해변 | 이도 게펜 지음, 임재희 옮김 | 문학세계사 | 2021 | 9788970759906 | NaN | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |
| 4 | 5 | 김성곤의 중국한시기행 : 장강·황하 편 | 김성곤 지음 | 김영사 | 2021 | 9788934990833 | NaN | NaN | NaN | NaN | 1 | 0.0 | 2021-03-19 |

```python
# 칼럼명 총 13개
# int64 = 64비트 정수
ns_book4.info()
```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 384591 entries, 0 to 384590
Data columns (total 13 columns):
 #   Column   Non-Null Count   Dtype  
---  ------   --------------   -----  
 0   번호       384591 non-null  int64  
 1   도서명      384188 non-null  object 
 2   저자       384393 non-null  object 
 3   출판사      379950 non-null  object 
 4   발행년도     384577 non-null  object 
 5   ISBN     384591 non-null  object 
 6   세트 ISBN  56576 non-null   object 
 7   부가기호     310386 non-null  object 
 8   권        63378 non-null   object 
 9   주제분류번호   364727 non-null  object 
 10  도서권수     384591 non-null  int64  
 11  대출건수     384591 non-null  float64
 12  등록일자     384591 non-null  object 
dtypes: float64(1), int64(2), object(10)
memory usage: 38.1+ MB
```

```python
ns_book4.info(memory_usage='deep')
```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 384591 entries, 0 to 384590
Data columns (total 13 columns):
 #   Column   Non-Null Count   Dtype  
---  ------   --------------   -----  
 0   번호       384591 non-null  int64  
 1   도서명      384188 non-null  object 
 2   저자       384393 non-null  object 
 3   출판사      379950 non-null  object 
 4   발행년도     384577 non-null  object 
 5   ISBN     384591 non-null  object 
 6   세트 ISBN  56576 non-null   object 
 7   부가기호     310386 non-null  object 
 8   권        63378 non-null   object 
 9   주제분류번호   364727 non-null  object 
 10  도서권수     384591 non-null  int64  
 11  대출건수     384591 non-null  float64
 12  등록일자     384591 non-null  object 
dtypes: float64(1), int64(2), object(10)
memory usage: 266.2 MB
```

```python
# is NaN?
ns_book4.isna().sum()
```

```
번호              0
도서명           403
저자            198
출판사          4641
발행년도           14
ISBN            0
세트 ISBN    328015
부가기호        74205
권          321213
주제분류번호      19864
도서권수            0
대출건수            0
등록일자            0
dtype: int64
```

```python
# 0(1번째 행)의 도서권수 칼럼을 None으로 변경
ns_book4.loc[0, '도서권수'] = None
# NaN인지 확인
ns_book4['도서권수'].isna().sum()
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 인공지능과 흙 | 김동훈 지음 | 민음사 | 2021 | 9788937444319 | NaN | NaN | NaN | NaN | NaN | 0.0 | 2021-03-19 |
| 1 | 2 | 가짜 행복 권하는 사회 | 김태형 지음 | 갈매나무 | 2021 | 9791190123969 | NaN | NaN | NaN | NaN | 1.0 | 0.0 | 2021-03-19 |

```python
ns_book4.loc[0, '도서권수'] = 1
# 실수 값으로 되어있는것을 32비트 정수로 변경 
ns_book4 = ns_book4.astype({'도서권수' : 'int32', '대출건수' : 'int32'})
ns_book4.head(2)
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 인공지능과 흙 | 김동훈 지음 | 민음사 | 2021 | 9788937444319 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 1 | 2 | 가짜 행복 권하는 사회 | 김태형 지음 | 갈매나무 | 2021 | 9791190123969 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |

```python
# 숫자가 아닌 값에는 NaN이 적용되지 않는다.
ns_book4.loc[0, '부가기호'] = None
ns_book4.head(2)
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 인공지능과 흙 | 김동훈 지음 | 민음사 | 2021 | 9788937444319 | NaN | None | NaN | NaN | 1 | 0 | 2021-03-19 |
| 1 | 2 | 가짜 행복 권하는 사회 | 김태형 지음 | 갈매나무 | 2021 | 9791190123969 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |

```python
# 문자를 NaN으로 표기하기 위해 numpy 사용 
import numpy as np

ns_book4.loc[0, '부가기호'] = np.nan
ns_book4.head(2)
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 인공지능과 흙 | 김동훈 지음 | 민음사 | 2021 | 9788937444319 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 1 | 2 | 가짜 행복 권하는 사회 | 김태형 지음 | 갈매나무 | 2021 | 9791190123969 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |

```python
# ns_book4의 '세트 ISBN'이 아무것도 없는 값을 찾아 set_isbn_na_rows에 저장
set_isbn_na_rows = ns_book4['세트 ISBN'].isna()
# 해당 값을 '' 공백으로 처리.
ns_book4.loc[set_isbn_na_rows, '세트 ISBN'] = ''
ns_book4['세트 ISBN'].isna().sum()

-> 0
```

```python
# 아무것도 없는 값을 '없음' 으로 채운다.
ns_book4.fillna('없음').isna().sum()
```

```
번호         0
도서명        0
저자         0
출판사        0
발행년도       0
ISBN       0
세트 ISBN    0
부가기호       0
권          0
주제분류번호     0
도서권수       0
대출건수       0
등록일자       0
dtype: int64
```

```python
# '부가기호'를 '없음' 으로 처리
ns_book4['부가기호'].fillna('없음').isna().sum()
```

```python
ns_book4.fillna({'부가기호':'없음'}).isna().sum()
```

```
번호              0
도서명           403
저자            198
출판사          4641
발행년도           14
ISBN            0
세트 ISBN         0
부가기호            0
권          321213
주제분류번호      19864
도서권수            0
대출건수            0
등록일자            0
dtype: int64
```

```python
# np.nan을 '없음'으로 처리
ns_book4.replace(np.nan, '없음').isna().sum()
```

```
번호         0
도서명        0
저자         0
출판사        0
발행년도       0
ISBN       0
세트 ISBN    0
부가기호       0
권          0
주제분류번호     0
도서권수       0
대출건수       0
등록일자       0
dtype: int64
```

```python
# '부가기호'가 np.nan이면 '없음' 으로 key와 value값으로 처리
ns_book4.replace({'부가기호': np.nan}, '없음').head(2)
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 인공지능과 흙 | 김동훈 지음 | 민음사 | 2021 | 9788937444319 |  | 없음 | NaN | NaN | 1 | 0 | 2021-03-19 |
| 1 | 2 | 가짜 행복 권하는 사회 | 김태형 지음 | 갈매나무 | 2021 | 9791190123969 |  | 없음 | NaN | NaN | 1 | 0 | 2021-03-19 |

```python
# '부가기호'가 np.nan이면 '없음'으로, '발행년도'가 '2021'이면 '21'으로 대치
ns_book4.replace({'부가기호': {np.nan: '없음'}, '발행년도': {'2021': '21'}}).head(2)
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 인공지능과 흙 | 김동훈 지음 | 민음사 | 21 | 9788937444319 |  | 없음 | NaN | NaN | 1 | 0 | 2021-03-19 |
| 1 | 2 | 가짜 행복 권하는 사회 | 김태형 지음 | 갈매나무 | 21 | 9791190123969 |  | 없음 | NaN | NaN | 1 | 0 | 2021-03-19 |

<br>

### 정규 표현식(Regular Expression)

- 데이터 전처리 시 가장 많이 사용하는 방법

https://pandas.pydata.org/docs/user_guide/missing_data.html#string-regular-expression-replacement

https://velog.io/@hhhs101/Pandas-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D-str.extractstr.contains

```python
# 발행년도가 '2021' 인 값을 '21'로 표현
# 데이터프레임의 100번부터 101번까지 슬라이싱
ns_book4.replace({'발행년도': {'2021': '21'}})[100:102]
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | 101 | No라고 말할 줄 아는 남편과 아내 - 개정판 | 헨리 클라우드, 존 타운센드 (지은이), 김진웅 (옮긴이) | 좋은씨앗 | 2018 | 9788958743019 |  | NaN | NaN | 234.9 | 1 | 1 | 2021-03-15 |
| 101 | 102 | D2C 레볼루션 - 스타트업부터 글로벌 기업까지, 마켓 체인저의 필수 전략 | 로런스 인그래시아 (지은이), 안기순 (옮긴이) | 부키 | 21 | 9788960518483 |  | NaN | NaN | 325.1 | 1 | 0 | 2021-03-15 |
- 정규표현식 사용

```python
# regex=True == regular expression = True 
# r'\d\d(\d\d)' -> 숫자 4개 중 뒤의 2자리를 그룹으로 묶음
# r'\1' -> 뒤의 2자리 그룹을 사용
ns_book4.replace({'발행년도': {r'\d\d(\d\d)': r'\1'}}, regex=True)[100:102]
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | 101 | No라고 말할 줄 아는 남편과 아내 - 개정판 | 헨리 클라우드, 존 타운센드 (지은이), 김진웅 (옮긴이) | 좋은씨앗 | 18 | 9788958743019 |  | NaN | NaN | 234.9 | 1 | 1 | 2021-03-15 |
| 101 | 102 | D2C 레볼루션 - 스타트업부터 글로벌 기업까지, 마켓 체인저의 필수 전략 | 로런스 인그래시아 (지은이), 안기순 (옮긴이) | 부키 | 21 | 9788960518483 |  | NaN | NaN | 325.1 | 1 | 0 | 2021-03-15 |

```python
# 위의 표현과 같다.
ns_book4.replace({'발행년도': {r'\d{2}(\d{2})': r'\1'}}, regex=True)[100:102]
```

```python
# (.*)\s\(지은이\) -> 0개 이상의 문자와 space가 나온뒤, (지은이)가 나타난다.
# (.*)\s\(옮긴이\) -> 0개 이상의 문자와 space가 나온뒤, (옮긴이)가 나타난다.
# r'\1\2 지정한 그룹 1과, 그룹 2를 사용.
ns_book4.replace({'저자': {r'(.*)\s\(지은이\)(.*)\s\(옮긴이\)': r'\1\2'},
                  '발행년도': {r'\d{2}(\d{2})': r'\1'}}, regex=True)[100:102]
```

- chat GPT 설명 첨부

![스크린샷 2023-07-19 오후 1 45 16](https://github.com/kimbap918/TIL/assets/75712723/a49214e6-a1d1-4fbb-9cc1-d1cb5a8e6d41)

<br>

### 잘못된 값 바꾸기

```python
# (\d{4}) 4개의 숫자가 묶인 그룹
# .*  앞뒤로 0개 이상의 문자
# \1 첫번째 그룹을 가져와 치환
ns_book5 = ns_book4.replace({'발행년도':r'.*(\d{4}).*'}, r'\1', regex=True)
ns_book5[invalid_number].head()
```

|       | 번호  | 도서명                  | 저자                                              | 출판사             | 발행년도 | ISBN          | 세트 ISBN     | 부가기호 | 권   | 주제분류번호 | 도서권수 | 대출건수 | 등록일자   |
| ----- | ----- | ----------------------- | ------------------------------------------------- | ------------------ | -------- | ------------- | ------------- | -------- | ---- | ------------ | -------- | -------- | ---------- |
| 19138 | 19565 | 단국강토                | 홍태수 저                                         | 매일경제신문사     | 1988     | 9788974420031 |               | NaN      | NaN  | 511.1        | 1        | 1        | 2019-12-19 |
| 19227 | 19736 | 삼성의 역사             | 송부웅 撰                                         | 삼양               | 2001     | 9788985464369 |               | 0        | NaN  | 911.02       | 1        | 1        | 2019-12-06 |
| 26097 | 26812 | 배고픈 애벌레           | 에릭 칼 글·그림 ;이희재 옮김                      | 더큰컴퍼니         | 2019     | 9788959514083 |               | NaN      | NaN  | 843          | 1        | 0        | 2019-08-12 |
| 29817 | 30586 | (The) Sopranos sessions | Matt Zoller Seitz,$eAlan Sepinwall,$eLaura Lip... | Harry N Abrams Inc | 2019     | 9781419734946 |               | NaN      | NaN  | 326.76       | 1        | 0        | 2019-06-13 |
| 29940 | 30709 | 다음엔 너야             | 에른스트 얀들 글;노르만 융에 그림;박상순 옮김     | 비룡소             | 2018     | 9788949110646 | 9788949110004 | 7        | NaN  | 853          | 1        | 9        | 2019-06-04 |

```python
# 발행년도에서, \D 숫자가 아닌것들
unkown_year = ns_book5['발행년도'].str.contains('\D', na=True)
print(unkown_year.sum())
ns_book5[unkown_year].head()
```

```
67

```

|        | 번호   | 도서명                        | 저자            | 출판사         | 발행년도     | ISBN          | 세트 ISBN     | 부가기호 | 권   | 주제분류번호 | 도서권수 | 대출건수 | 등록일자   |
| ------ | ------ | ----------------------------- | --------------- | -------------- | ------------ | ------------- | ------------- | -------- | ---- | ------------ | -------- | -------- | ---------- |
| 30838  | 31616  | 본격 한중일 세계사 5          | 굽시니스트 지음 | 위즈덤하우스   | NaN          | 9791190065092 |               | NaN      | NaN  | NaN          | 0        | 0        | 2019-05-28 |
| 39130  | 40141  | 정책금융의 현황과 발전과제    | 정책금융연구회  | 한국산업은행   | NaN          | 9788992784108 |               | NaN      | NaN  | 327.1        | 1        | 0        | 2019-01-22 |
| 39256  | 40268  | 서울지역 유적 발굴조사 총서 3 | 서울역사박물관  | 서울역사박물관 | NaN          | 9791186324714 | 9791186324431 | NaN      | NaN  | NaN          | 0        | 0        | 2019-01-22 |
| 76836  | 81202  | 흰머리 큰줄기                 | 한호진 지음     | 秀文出版社     | [발행년불명] | 9788973010769 |               | 0        | NaN  | 699.1        | 1        | 1        | 2016-11-10 |
| 150543 | 160436 | (속) 경제학사                 | 박장환 지음     | NaN            | [20--]       | 9788994339207 |               | 1        | NaN  | 320.9        | 1        | 2        | 2012-11-19 |

```python
# unkown_year에 해당하는 발행년도를 '-1'로 바꿔준다.
ns_book5.loc[unkown_year, '발행년도'] = '-1'
# ns_book5의 '발행년도'를 32비트 정수로 변경 
ns_book5 = ns_book5.astype({'발행년도': 'int32'})
```

```python
# gt = greater than 
# 발행년도가 4000 큰 값들 개수
ns_book5['발행년도'].gt(4000).sum()

-> 131
```

```python
# 해당 년도를 단기로 저장
dangun_yy_rows = ns_book5['발행년도'].gt(4000)
# 단기에서 2333년을 빼서 서기로 저장
ns_book5.loc[dangun_yy_rows, '발행년도'] = ns_book5.loc[dangun_yy_rows, '발행년도'] - 2333
```

```python
# 위의 작업 후에도 단기로 나오는 데이터를
dangun_year = ns_book5['발행년도'].gt(4000)
print(dangun_year.sum())
ns_book5[dangun_year].head(2)
```

```python
# -1로 저장해 버린다.
ns_book5.loc[dangun_year, '발행년도'] = -1
```

```python
# 0보다 크고 1900년대 이전의 책은 old_books
old_books = ns_book5['발행년도'].gt(0) & ns_book5['발행년도'].lt(1900)
ns_book5[old_books]
```

```python
# old_books 또한 -1처리하여 버린다.
ns_book5.loc[old_books, '발행년도'] = -1
```

```python
# 버린 책의 총 수량
ns_book5['발행년도'].eq(-1).sum()

-> 86
```

<br>

### 누락된 정보 채우기

- BeautifulSoup

[](https://defineall.tistory.com/640)

```python
# BeautifulSoup
# HTML정보로 부터 원하는 데이터를 가져오기 쉽게, 
# 비슷한 분류의 데이터별로 나누어주는(parsing) 파이썬 라이브러리
import requests
from bs4 import BeautifulSoup
```

```python
def get_book_title(isbn):
    # Yes24 도서 검색 페이지 URL
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    # URL에 ISBN을 넣어 HTML 가져옵니다.
    r = requests.get(url.format(isbn))
    soup = BeautifulSoup(r.text, 'html.parser')   # HTML 파싱
    # 클래스 이름이 'gd_name'인 a 태그의 텍스트를 가져옵니다.
    title = soup.find('a', attrs={'class':'gd_name'}) \
            .get_text()
    return title
```

```python
get_book_title(9791191266054)

-> '골목의 시간을 그리다'
```

```python
# 'ns_book5' 데이터프레임의 일부 행에서 
# 도서 정보를 가져오는 함수인 get_book_info를 정의
import re

def get_book_info(row):
    title = row['도서명']
    author = row['저자']
    pub = row['출판사']
    year = row['발행년도']
    # Yes24 도서 검색 페이지 URL
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    # URL에 ISBN을 넣어 HTML 가져옵니다.
    r = requests.get(url.format(row['ISBN']))
    soup = BeautifulSoup(r.text, 'html.parser')   # HTML 파싱
    try:
				# 타이틀이 비어있으면(isna)
        if pd.isna(title):
            # 클래스 이름이 'gd_name'인 a 태그의 텍스트를 가져옵니다.
            title = soup.find('a', attrs={'class':'gd_name'}) \
                    .get_text()
    except AttributeError:
        pass

    try:
				# 저자가 비어있으면
        if pd.isna(author):
            # 클래스 이름이 'info_auth'인 span 태그 아래 a 태그의 텍스트를 가져옵니다.
            authors = soup.find('span', attrs={'class':'info_auth'}) \
                          .find_all('a')
            author_list = [auth.get_text() for auth in authors]
            author = ','.join(author_list)
    except AttributeError:
        pass

    try:
				# 출판사가 비어있으면
        if pd.isna(pub):
            # 클래스 이름이 'info_auth'인 span 태그 아래 a 태그의 텍스트를 가져옵니다.
            pub = soup.find('span', attrs={'class':'info_pub'}) \
                      .find('a') \
                      .get_text()
    except AttributeError:
        pass

    try:
				# 발행년도가 -1(버린책)이면
        if year == -1:
            # 클래스 이름이 'info_date'인 span 태그 아래 텍스트를 가져옵니다.
            year_str = soup.find('span', attrs={'class':'info_date'}) \
                           .get_text()
            # 정규식으로 찾은 값 중에 첫 번째 것만 사용합니다.
            year = re.findall(r'\d{4}', year_str)[0]
    except AttributeError:
        pass

    return title, author, pub, year
```

```python
# ns_book5 데이터프레임에서 누락된 도서 정보(도서명, 저자, 출판사, 발행년도 중 누락된)
# 가 있는 행 중에서 처음 2행을 가져온다.
updated_sample = ns_book5[na_rows].head(2).apply(get_book_info,
    axis=1, result_type ='expand')
updated_sample
```

|      | 0                    | 1                  | 2                    | 3    |
| ---- | -------------------- | ------------------ | -------------------- | ---- |
| 78   | 아산 정주영 레거시   | 김화진             | 서울대학교출판문화원 | 2021 |
| 265  | 골목의 시간을 그리다 | 정명섭.김효찬 지음 | 초록비책공방         | 2021 |

<br>

### 실습 전 - 아이리스 데이터를 왜 사용할까?

[아이리스 데이터](https://hoon427.tistory.com/28)

<br>

### 실습 - 타이타닉

- 해당 코드는 주관적으로 작성되어 정답이 아닐 수 있다.

```
조건

1. 캐글에서 타이타닉 데이터를 찾아 train.csv 다운 받아 사용합니다. 

2. 가져온 데이터에서 이름 성별, 나이, 캐빈 칼럼만 떼어내 데이터 프레임을 새로 만듭니다. 

   * Name, Sex, Age, Cabin

3. 새로만든 데이터 프레임에 대하여 성별에 male은 man, female은 woman으로 변경합니다. 

4. 나이의 nan은 모두 0으로 변경합니다. 

5. 정규 표현식으로 캐빈에 앞의 영문자 즉 등급만 저장합니다. 

6. 모두 수정한 데이터를 train_v2.csv로 저장합니다.
```

```python
# 1. 캐글에서 타이타닉 데이터를 찾아 train.csv 다운 받아 사용합니다. 
import pandas as pd

df = pd.read_csv('/content/train.csv')
df.head()
```

|      | PassengerId | Survived | Pclass | Name                                              | Sex    | Age  | SibSp | Parch | Ticket           | Fare    | Cabin | Embarked |
| ---- | ----------- | -------- | ------ | ------------------------------------------------- | ------ | ---- | ----- | ----- | ---------------- | ------- | ----- | -------- |
| 0    | 1           | 0        | 3      | Braund, Mr. Owen Harris                           | male   | 22.0 | 1     | 0     | A/5 21171        | 7.2500  | NaN   | S        |
| 1    | 2           | 1        | 1      | Cumings, Mrs. John Bradley (Florence Briggs Th... | female | 38.0 | 1     | 0     | PC 17599         | 71.2833 | C85   | C        |
| 2    | 3           | 1        | 3      | Heikkinen, Miss. Laina                            | female | 26.0 | 0     | 0     | STON/O2. 3101282 | 7.9250  | NaN   | S        |
| 3    | 4           | 1        | 1      | Futrelle, Mrs. Jacques Heath (Lily May Peel)      | female | 35.0 | 1     | 0     | 113803           | 53.1000 | C123  | S        |
| 4    | 5           | 0        | 3      | Allen, Mr. William Henry                          | male   | 35.0 | 0     | 0     | 373450           | 8.0500  | NaN   | S        |

```python
# 2. 가져온 데이터에서 이름 성별, 나이, 캐빈 칼럼만 떼어네 데이터 프레임을 새로 만듭니다. 
# * Name, Sex, Age, Cabin
df_ship = df[['Name', 'Sex', 'Age', 'Cabin']]
df_ship.head()
```

|      | Name                                              | Sex    | Age  | Cabin |
| ---- | ------------------------------------------------- | ------ | ---- | ----- |
| 0    | Braund, Mr. Owen Harris                           | male   | 22.0 | NaN   |
| 1    | Cumings, Mrs. John Bradley (Florence Briggs Th... | female | 38.0 | C85   |
| 2    | Heikkinen, Miss. Laina                            | female | 26.0 | NaN   |
| 3    | Futrelle, Mrs. Jacques Heath (Lily May Peel)      | female | 35.0 | C123  |
| 4    | Allen, Mr. William Henry                          | male   | 35.0 | NaN   |

```python
# 3. 새로만든 데이터 프레임에 대하여 성별에 male은 man, female은 woman으로 변경합니다. 
df_sex = df_ship.replace({'Sex' : {'male': 'man', 'female': 'woman'}})
df_sex.head()
```

|      | Name                                              | Sex   | Age  | Cabin |
| ---- | ------------------------------------------------- | ----- | ---- | ----- |
| 0    | Braund, Mr. Owen Harris                           | man   | 22.0 | NaN   |
| 1    | Cumings, Mrs. John Bradley (Florence Briggs Th... | woman | 38.0 | C85   |
| 2    | Heikkinen, Miss. Laina                            | woman | 26.0 | NaN   |
| 3    | Futrelle, Mrs. Jacques Heath (Lily May Peel)      | woman | 35.0 | C123  |
| 4    | Allen, Mr. William Henry                          | man   | 35.0 | NaN   |

```python
# 4. 나이의 nan은 모두 0으로 변경합니다. 
# Age의 NaN인 값의 개수를 조회했다.
df_sex['Age'].isna().sum()

-> 177
```

```python
# df_age에 df_sex를 복사해 저장
df_age = df_sex.copy()
```

```python
# df_age['Age']에 df_sex['Age']값 중 NaN을 0으로 치환 후 저장
df_age['Age'] = df_sex['Age'].fillna(0)
# NaN 개수 확인
# df_age['Age'].isna().sum()
df_age.head()
```

|      | Name                                              | Sex   | Age  | Cabin |
| ---- | ------------------------------------------------- | ----- | ---- | ----- |
| 0    | Braund, Mr. Owen Harris                           | man   | 22.0 | NaN   |
| 1    | Cumings, Mrs. John Bradley (Florence Briggs Th... | woman | 38.0 | C85   |
| 2    | Heikkinen, Miss. Laina                            | woman | 26.0 | NaN   |
| 3    | Futrelle, Mrs. Jacques Heath (Lily May Peel)      | woman | 35.0 | C123  |
| 4    | Allen, Mr. William Henry                          | man   | 35.0 | NaN   |

```python
# 5. 정규 표현식으로 캐빈에 앞의 영문자 즉 등급만 저장합니다. 
# df_cabin에 df_age를 복사해 저장
df_cabin = df_age.copy()
df_cabin.head()
```

|      | Name                                              | Sex   | Age  | Cabin |
| ---- | ------------------------------------------------- | ----- | ---- | ----- |
| 0    | Braund, Mr. Owen Harris                           | man   | 22.0 | NaN   |
| 1    | Cumings, Mrs. John Bradley (Florence Briggs Th... | woman | 38.0 | C85   |
| 2    | Heikkinen, Miss. Laina                            | woman | 26.0 | NaN   |
| 3    | Futrelle, Mrs. Jacques Heath (Lily May Peel)      | woman | 35.0 | C123  |
| 4    | Allen, Mr. William Henry                          | man   | 35.0 | NaN   |

```python
# df_cabin에 'Cabin' 칼럼의 맨 앞문자(\w)와 .* 0줄이상의 문자열 중 첫번째 그룹을 사용.
df_cabin = df_cabin.replace({'Cabin' : {r'(\w).*': r'\1'}}, regex=True)
# df_cabin[df_cabin['Cabin'].notnull()].head()
df_cabin.head()
```

|      | Name                                              | Sex   | Age  | Cabin |
| ---- | ------------------------------------------------- | ----- | ---- | ----- |
| 0    | Braund, Mr. Owen Harris                           | man   | 22.0 | NaN   |
| 1    | Cumings, Mrs. John Bradley (Florence Briggs Th... | woman | 38.0 | C     |
| 2    | Heikkinen, Miss. Laina                            | woman | 26.0 | NaN   |
| 3    | Futrelle, Mrs. Jacques Heath (Lily May Peel)      | woman | 35.0 | C     |
| 4    | Allen, Mr. William Henry                          | man   | 35.0 | NaN   |

```python
# 6. 모두 수정한 데이터를 train_v2.csv로 저장합니다.
df_cabin.to_csv('train_v2.csv', index=False)
```

<br>

### 04-1 통계로 요약하기

### 기술통계 구하기

```python
import pandas as pd

ns_book6 = pd.read_csv('ns_book6.csv', low_memory=False)
ns_book6.head()
```

|      | 번호 | 도서명                               | 저자                        | 출판사     | 발행년도 | ISBN          | 세트 ISBN | 부가기호 | 권   | 주제분류번호 | 도서권수 | 대출건수 | 등록일자   |
| ---- | ---- | ------------------------------------ | --------------------------- | ---------- | -------- | ------------- | --------- | -------- | ---- | ------------ | -------- | -------- | ---------- |
| 0    | 1    | 인공지능과 흙                        | 김동훈 지음                 | 민음사     | 2021.0   | 9788937444319 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 1    | 2    | 가짜 행복 권하는 사회                | 김태형 지음                 | 갈매나무   | 2021.0   | 9791190123969 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 2    | 3    | 나도 한 문장 잘 쓰면 바랄 게 없겠네  | 김선영 지음                 | 블랙피쉬   | 2021.0   | 9788968332982 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 3    | 4    | 예루살렘 해변                        | 이도 게펜 지음, 임재희 옮김 | 문학세계사 | 2021.0   | 9788970759906 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 4    | 5    | 김성곤의 중국한시기행 : 장강·황하 편 | 김성곤 지음                 | 김영사     | 2021.0   | 9788934990833 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |

```python
# 데이터프레임의 기술통계를 산출해서 보여준다.
ns_book6.describe()
# ns_book6.info()
```

|       | 번호          | 발행년도      | 도서권수      | 대출건수      |
| ----- | ------------- | ------------- | ------------- | ------------- |
| count | 379976.000000 | 379976.000000 | 379976.000000 | 379976.000000 |
| mean  | 201726.332847 | 2008.516306   | 1.135874      | 11.504629     |
| std   | 115836.454596 | 8.780529      | 0.483343      | 19.241926     |
| min   | 1.000000      | 1947.000000   | 0.000000      | 0.000000      |
| 25%   | 102202.750000 | 2003.000000   | 1.000000      | 2.000000      |
| 50%   | 203179.500000 | 2009.000000   | 1.000000      | 6.000000      |
| 75%   | 301630.250000 | 2015.000000   | 1.000000      | 14.000000     |
| max   | 401681.000000 | 2650.000000   | 40.000000     | 1765.000000   |

### (참고) 선형 회귀와 정규화

[선형 회귀](https://ko.wikipedia.org/wiki/선형_회귀)

[[파이썬/머신러닝] 회귀분석(Regression)(6) - 정규화(Regularized Regression/Regularization) 이론](https://blog.naver.com/PostView.nhn?blogId=winddori2002&logNo=221824408166)