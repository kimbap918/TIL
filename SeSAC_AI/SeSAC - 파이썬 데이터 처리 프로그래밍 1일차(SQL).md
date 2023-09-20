## SeSAC - 파이썬 데이터 처리 프로그래밍 1일차(SQL)

2023.07.31

<br>

### JOIN

두 개의 테이블을 서로 묶어서 하나의 결과를 만들어 내는 것

- 두 개의 테이블을 묶기 위해선 기준점이 필요하다.
- 두 테이블의 조인을 위해서는 테이블이 일대다(one to many)관계로 연결되어야 한다.
- 일대다 관계는 주로 기본키(PK)와 외래 키(FK)관계로 맺어져 있다.

<br>

### 내부조인(inner join)

일반적으로 조인이라 부르는 것은 내부조인(inner join)을 말한다. 조인 중에서 가장 많이 사용되는 방법이다.

```sql
select *
from buy -- 기준이 되는 테이블
inner join member -- member 테이블을 join
on buy.mem_id  = member.mem_id; -- 각 테이블의 mem_id를 기준으로 테이블을 묶는다.
```

<br>

### 주의점

```sql
select prod_name, mem_name, addr, mem_id -- 오류!
from buy
inner join member 
on buy.mem_id  = member.mem_id;
-- Error Code: 1052. Column 'mem_id' in field list is ambiguous
```

위의 SQL문은 조회 시 오류가 생긴다.

SELECT에서 mem_id가 buy, member 테이블에 모두 있기때문에 mem_id를 조회하기 위해서는 어느 테이블의 mem_id인지 반드시 지정을 해줘야한다.

```sql
select prod_name, mem_name, addr, b.mem_id -- buy의 mem_id
from buy b -- 별칭을 지정해준다.
inner join member 
on b.mem_id  = member.mem_id;
```

<br>

### 외부 조인(outer join)

내부 조인은 두 테이블에 모두 데이터가 있어야 결과가 나온다. 하지만 외부 조인은 한쪽에만 데이터가 있어도 결과가 나온다.

```sql
select m.mem_id, m.mem_name, b.prod_name, m.addr
from member m -- 회원 테이블을 기준으로 외부조인한다.
left outer join buy b
on m.mem_id = b.mem_id 
order by m.mem_id;
```

![스크린샷 2023-07-31 오전 9 34 00](https://github.com/kimbap918/TIL/assets/75712723/a2c9879c-2989-4de7-8cf8-fb1399fed85a)

비교를 위해 inner join을 같이 확인해보자.

```sql
select m.mem_id, m.mem_name, b.prod_name, m.addr
from buy b
inner join member m
on b.mem_id  = m.mem_id;
```

![스크린샷 2023-07-31 오전 9 35 20](https://github.com/kimbap918/TIL/assets/75712723/9b1253f2-aa6b-461f-a32e-470d84bb0704)

outer join은 null 값을 가진 데이터 또한 조회되는것을 확인할 수 있다.

또한, 외부 조인에서 left outer ~ 구문은 생략 가능하다.

```sql
select m.mem_id, m.mem_name, b.prod_name, m.addr
from member m -- 회원 테이블을 기준으로 외부조인한다.
join buy b
on m.mem_id = b.mem_id 
order by m.mem_id;
```

<br>

### 기타 조인

- 상호 조인(cross join) : 한쪽 테이블의 모든 행과 다른 쪽 테이블의 모든 행을 조인시키는 기능, 카테시안 곱(cartesian product) 라고도 한다.
- 자체 조인(self join) : 내부 조인, 외부 조인, 상호 조인은 2개의 테이블을 조인하는것과 달리 자체 조인은 자신이 자신을 조인하며, 1개의 테이블을 사용한다.

<br>

### 실습 문제

1. 전체 걸그룹의 평균(AVG) 멤버보다 많은 멤버로 이루어진 걸그룹이 구매한 상품명과 걸그룹명 출력

```sql
-- 전체 걸그룹의 평균(AVG) 멤버보다 많은 멤버로 이루어진 걸그룹이 구매한 상품명과 걸그룹명 출력
select m.mem_name, b.prod_name
from buy b
join member m
on m.mem_id = b.mem_id
where mem_number > (select avg(mem_number) from member);
```

2. 서울에 사는 걸그룹 중 소비금액이 1000원 이상인 걸그룹명과 소비금액을 출력

```sql
-- 서울에 사는 걸그룹 중 소비금액이 1000원 이상인 걸그룹명과 소비금액을 출력
select m.mem_name, sum(b.price*b.amount) 소비금액
from buy b
join member m
on m.mem_id = b.mem_id
where m.addr = '서울'
group by m.mem_name
having sum(b.price*b.amount) >= 1000;
```

<br>

## Jupyter Notebook 설치

파이썬이 설치 되지 않았다면 https://kosb.tistory.com/124 참고

주피터 노트북 설치

```
pip install notebook
```

실행

```
jupyter notebook
```

![무제](https://github.com/kimbap918/TIL/assets/75712723/90c10c08-fb39-4449-a7c9-702d356f802d)

<br>

### 실행 후 화면

1. Desktop을 눌러서 바탕화면으로 진입

![스크린샷 2023-07-31 오전 11 34 37](https://github.com/kimbap918/TIL/assets/75712723/260e2cd3-7523-4c50-858c-5c890512cf7d)

2. New를 클릭해서 Notebook 생성

![스크린샷 2023-07-31 오전 11 35 01](https://github.com/kimbap918/TIL/assets/75712723/81968ef3-8d83-4183-a5bb-ab2abc9c287d)

3. 실행된 노트북에서 아래의 명령 실행

```
!pip3 install requests selenium webdriver_manager
```

![스크린샷 2023-07-31 오후 12 00 55](https://github.com/kimbap918/TIL/assets/75712723/cc5215bc-1078-4b29-9555-7003e605221c)

<br>

### 주의할 점

jupyter notebook 실행 중 터미널을 종료하면 jupyter notebook 또한 종료되므로 터미널을 종료하지 않는다.

<br>

### 데이터 가져오기

jupyter에서 웹 데이터를 가져와보자.

```python
import requests

res = requests.get("https://www.naver.com")
print(res.text)
```

<br>

위의 코드는 네이버에서 정보를 가져오는 코드다. 보통 웹 사이트에서 크롤러나 자동화 도구를 사용하면 차단을 하는데 이런 경우에 아래와 같은 fake_useragent를 사용한다.

```python
!pip3 install fake_useragent
```

```python
import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    "User-Agent" : ua.random
}

res = requests.get("https://www.naver.com", headers=headers)
print(res.text)
```

<br>

### 인터넷 뉴스 기사 가져와보기

1. chrome에서 네이버 뉴스 페이지 접속 https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105 

![스크린샷 2023-07-31 오후 2 36 23](https://github.com/kimbap918/TIL/assets/75712723/220951f0-9670-45ad-af23-34039f5fa971)

2. (mac)command+option+i 로 콘솔 창을 연 후, 원하는 태그 검색

* class는 `.`, id는 `#` 로 검색 가능

![스크린샷 2023-07-31 오후 2 15 15](https://github.com/kimbap918/TIL/assets/75712723/2be5d9b9-7288-4ebe-89ab-943f47a9cac1)

3. Jupyter notebook에서 코드 입력 

```python
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup # BeautifulSoup import

ua = UserAgent()
headers = {
    "User-Agent" : ua.random
}

res = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105", headers=headers) 

bs = BeautifulSoup(res.text, 'html.parser') # 가지고 온 텍스트를 html로 parsing
elem = bs.select_one("a.list_tit") # a 태그의 list_tit class 중 하나만 가져옴

# <a href="https://n.news.naver.com/mnews/ranking/article/055/0001077601?ntype=RANKING&amp;sid=001" class="list_tit nclicks('rig.renws2')">현직 특수교사, 주호민 향해 "사람 갈구는 일진 놀음"</a>

print(elem.text)

# 기사를 전부 가져와서 한줄씩 출력할때
# elem = bs.select("a.list_tit")
# for e in elem:
#     print(e.text)
```

<br>

* 태그에서 id값을 가져올 때

``` python
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
headers = {
    "User-Agent" : ua.random
}

res = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105", headers=headers)


bs = BeautifulSoup(res.text, 'html.parser')
area = bs.select_one("#_rankingList0")
elem = area.select("a.list_tit")
for e in elem:
    print(e.text)
```

<br>

### 실습 - 분야별 주요 뉴스 15개 수집

```python
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
headers = {
    "User-Agent" : ua.random
}

res = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105", headers=headers)


bs = BeautifulSoup(res.text, 'html.parser')
area = bs.select_one("#right_dailyList") 
# > 는 바로 밑에 라는 의미다.
elem = area.select("#right_dailyList > div > ul > li > a")

f = open("article.csv", "w", encoding="utf-8")

for e in elem:
#    print(e.text)
#    print(e.attrs['href'])
    title = e.text.replace(".", "-")
    count = title.count(" ")
    link = e.attrs.get("href", "")
    f.write(f"{title},{count},{link}\n")
    
f.close()
```

<br>

### 실습 - 파이썬 검색 정보 수집

```python
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
headers = {
    "User-Agent" : ua.random
}

# 파이썬 검색 주소
res = requests.get("https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC", headers=headers)


bs = BeautifulSoup(res.text, 'html.parser')

area = bs.select_one(".lst_total") 
lis = area.select("._svp_item")


f = open("search.csv", "w", encoding="utf-8")

# 제목, 설명 2줄, 날짜
for li in lis:
    title = li.select_one(".total_tit")
    title = title.text.replace(",", "-")
    
    content = li.select_one(".dsc_txt")
    content = content.text.replace(",", "-")
    
    dates = li.select_one(".source_txt")
    if not dates:
        dates = li.select_one(".sub_txt")
    dates = dates.text
    
    f.write(f"{title},{content},{dates}\n")

f.close()
```

<br>

### 실습 - 주식 top 종목 가져오기

``` python
# tds = area.select("td를 가져오는 코드")
# tds : 리스트
# tds[0] : 가격
# tds[1] : 변동가격
# tds[2] : 변동률

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
headers = {
    "User-Agent" : ua.random
}

res = requests.get("https://finance.naver.com/", headers=headers)


bs = BeautifulSoup(res.text, 'html.parser')
tbody = bs.select_one("#_topItems1")
trs = tbody.select("tr")

for tr in trs:
    name = tr.select_one("th > a")
    name = name.text

    tds = tr.select("td")
    price = tds[0].text
    diff = tds[1].text
    rate = tds[2].text

    print(name, price+"원", diff+"원", rate)
    print('')    
```

