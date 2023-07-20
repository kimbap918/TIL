# SeSAC - SQL로 데이터 베이스 다루기 1일차

2023.07.20

---

### Database

- 데이터베이스(Database, DB)는 ‘데이터의 집합’
- DBMS(Database Management System)은 데이터베이스를 관리하고 운영하는 소프트웨어다.
- DBMS에는 Oracle, MySQL, MariaDB 등이 있다.
- DBMS는 분류에 따라 계층형, 망형, 관계형, 객체지향형, 객체관계형 등의 종류가 있으나, 우리가 사용할 SQL을 포함해서 대부분의 DBMS는 관계형(Relational) DBMS(RDBMS)다.

[관계형 데이터베이스(RDBMS)란 무엇인가요?  |  Google Cloud](https://cloud.google.com/learn/what-is-a-relational-database?hl=ko)

<br>

### MySQL, MySQL Workbench  설치(mac)

- MacOS BigSur를 사용하고 있어서 버전이 안맞을수도 있습니다.

[MySQL :: Download MySQL Community Server](https://dev.mysql.com/downloads/mysql/)

1. MySQL Community Server 8.0.34 선택 후 다운로드(제목 옆 버전 꼭 확인할것!)

![스크린샷 2023-07-20 오전 9 17 42](https://github.com/kimbap918/TIL/assets/75712723/d2dab7e3-3d26-42d4-b0c4-d69b091a500f)

2. 로그인 필요없음. 아래의 No thanks, just start my download 선택 

![스크린샷 2023-07-20 오전 9 20 44 (1)](https://github.com/kimbap918/TIL/assets/75712723/229b76a8-d214-4628-8cab-dc2b392f8d10)

3. 다운로드 받은 패키지 파일 실행 

![스크린샷 2023-07-20 오전 9 42 32 (1)](https://github.com/kimbap918/TIL/assets/75712723/6370ffbb-138c-4304-af0d-11bf0a334b9b)

4. 설치 진행, 설치 과정 중간에 root 비밀번호 설정 필수

![스크린샷 2023-07-20 오전 9 43 25](https://github.com/kimbap918/TIL/assets/75712723/0af8dd6e-b723-4f78-8a49-86ee10556cea)

5. 아래 링크를 클릭해서 MySQL Workbench 설치

[MySQL :: Download MySQL Workbench (Archived Versions)](https://downloads.mysql.com/archives/workbench/)

6. Workbench 아이콘을 Applications에 드래그

![스크린샷 2023-07-20 오전 9 46 49](https://github.com/kimbap918/TIL/assets/75712723/af02fb1b-06c6-4c0f-80d1-52581c9a5654)

7. 설치완료

![스크린샷 2023-07-20 오전 9 48 05](https://github.com/kimbap918/TIL/assets/75712723/ea533d35-4ffa-4a9b-85b6-aa83415294eb)

<br>

### MySQL World database설치

* Mac에는 샘플 데이터가 없어서 샘플 데이터를 따로 받아서 설치합니다.

[MySQL :: Setting Up the world Database :: 2 Installation](https://dev.mysql.com/doc/world-setup/en/world-setup-installation.html)

1. 화면의 링크 클릭

![스크린샷 2023-07-20 오전 9 59 59](https://github.com/kimbap918/TIL/assets/75712723/4778921a-7255-4c35-9191-62586d5fe6bc)

2. world database, sakila database 다운로드

![스크린샷 2023-07-20 오전 10 00 27](https://github.com/kimbap918/TIL/assets/75712723/d9068737-4a76-4e5d-8a2c-10163f8e08e4)샘플

3. 데이터 폴더로 이동해서 sql파일 각각 실행 후 쿼리실행


![스크린샷 2023-07-20 오전 10 03 47](https://github.com/kimbap918/TIL/assets/75712723/b8e1d2e6-03dc-4894-bbea-8628f8d224d8)

![스크린샷 2023-07-20 오전 10 08 06](https://github.com/kimbap918/TIL/assets/75712723/11ef041b-b783-4023-8a04-fae6253f6093)

![스크린샷 2023-07-20 오전 10 08 14](https://github.com/kimbap918/TIL/assets/75712723/8035d351-2431-453c-9c06-d4bc8f615484)

4. 쿼리 실행버튼은 번개모양 ⚡️

![스크린샷 2023-07-20 오전 10 16 47](https://github.com/kimbap918/TIL/assets/75712723/f89856ee-6c0d-453d-9f29-7bd8668f33a3)

<br>

### 스키마(Schema) 생성하기

1. Schemas 클릭

![스크린샷 2023-07-20 오전 10 16 47 (2)](https://github.com/kimbap918/TIL/assets/75712723/589a0021-190c-44ed-bceb-2a55f5fef97c)

2. 마우스 우클릭 후 Create Schema 클릭

![스크린샷 2023-07-20 오전 10 35 33](https://github.com/kimbap918/TIL/assets/75712723/74d0d804-2fdf-4667-9cb0-c5b6bee549e8)

3. 스키마 이름 작성 후 apply

![스크린샷 2023-07-20 오전 10 34 39](https://github.com/kimbap918/TIL/assets/75712723/aa868509-4d01-486e-b5cc-e4fc528bad1e)

<br>

### 테이블(table) 생성하기(혼자 공부하는 SQL 71p, 72p 실습)

1. 만들어진 shop_db의 Table 탭 마우스 우클릭 후 Create Table

![스크린샷 2023-07-20 오전 10 44 54](https://github.com/kimbap918/TIL/assets/75712723/20d283ae-b8f0-4407-b8d6-753b8ffba1ca)

2. 제약조건에 맞게 테이블 칼럼 생성 후 apply

![스크린샷 2023-07-20 오전 10 27 18](https://github.com/kimbap918/TIL/assets/75712723/92995a18-2a38-4f92-803c-27480fd987c6)

3. 내용 확인 후 apply

![스크린샷 2023-07-20 오전 10 27 41](https://github.com/kimbap918/TIL/assets/75712723/4071cc3d-53ea-4fce-a849-e1ff79f7e3e6)

<br>

### 데이터 입력하기(75p 실습)

1. 생성된 테이블에 마우스 오른쪽 클릭 후 Select Rows 클릭

![스크린샷 2023-07-20 오전 10 38 48](https://github.com/kimbap918/TIL/assets/75712723/99816f65-e533-4448-8662-b9d9a634a360)

2. Result Grid에 데이터를 입력하고 apply

![스크린샷 2023-07-20 오전 10 54 29](https://github.com/kimbap918/TIL/assets/75712723/f93deff8-4944-459f-b9e3-0cc333799c1f)

3. 입력한 데이터 확인 후 apply

![스크린샷 2023-07-20 오전 10 44 20](https://github.com/kimbap918/TIL/assets/75712723/7df1c7aa-ef7a-4800-8bdd-62fb4bb37aaa)

<br>

- (참고) 테이블의 내용을 바꾸고 싶을때

```sql
/* 주소가 경기 고양시 장항동인 박진영의 주소를 장향동으로 바꾸기 위해선 다음과 같이 구문을 작성한다.*/
UPDATE shop_db.member
SET member_addr = '경기 고양시 장향동' 
WHERE (member_id = 'jyp');
```

- (참고) 테이블의 내용을 삭제하고 싶을때

```sql
/* 박진영을 삭제하고 싶을땐 member_id가 jyp인 값을 찾아 삭제한다. 
	여기서 where 절에 member_id를 사용하는 이유는 이 테이블에서 member_id가 
	유일한 값을 가지는 PK이기 때문이다.(유일한 값이기 때문에 데이터를 구분할 수 있음) */
DELETE 
FROM shop_db.member 
WHERE (member_id = 'jyp');
```

<br>

### 뷰(View)

뷰는 가상 테이블이다. 뷰는 실제 데이터를 가지고 있지 않고 진짜 테이블에 링크된 개념이다.

윈도우를 예로 들면 아이콘이 있고, 바로가기 아이콘을 생성해서 사용하는것과 비슷하다고 볼수 있다. 뷰를 생성하는 방법은 다음과 같다.

```sql
CREATE VIEW member_view -- 이름은 원하는대로 설정 
AS
SELECT * FROM member;
```

생성 후 조회 했을때는 member 테이블과 같이 조회가 가능하다.

![스크린샷 2023-07-20 오전 11 22 17 (1)](https://github.com/kimbap918/TIL/assets/75712723/8d6bbd38-a623-4f37-8f47-ed0cc0de7fd2)

<br>

### 실습 - 인터넷 마켓 DB

아래의 sql 다운로드 후 쿼리 실행

[market_db.sql](https://cloud.lahion.com/s/RQHm9ARqqGPDdTK)

샘플데이터의 내용

```sql
DROP DATABASE IF EXISTS market_db; -- 만약 market_db가 존재하면 우선 삭제한다.
CREATE DATABASE market_db; -- 데이터베이스 'market_db' 생성

USE market_db;

CREATE TABLE member -- 회원 테이블
-- 테이블의 필드
( mem_id  		CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  mem_name    	VARCHAR(10) NOT NULL, -- 이름
  mem_number    INT NOT NULL,  -- 인원수
  addr	  		CHAR(2) NOT NULL, -- 지역(경기,서울,경남 식으로 2글자만입력)
  phone1		CHAR(3), -- 연락처의 국번(02, 031, 055 등)
  phone2		CHAR(8), -- 연락처의 나머지 전화번호(하이픈제외)
  height    	SMALLINT,  -- 평균 키
  debut_date	DATE  -- 데뷔 일자
);

CREATE TABLE buy -- 구매 테이블
-- 테이블의 필드
(  num 		INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   mem_id  	CHAR(8) NOT NULL, -- 아이디(FK)
   prod_name 	CHAR(6) NOT NULL, --  제품이름
   group_name 	CHAR(4)  , -- 분류
   price     	INT  NOT NULL, -- 가격
   amount    	SMALLINT  NOT NULL, -- 수량
	 -- buy 테이블의 mem_id는 member 테이블의 mem_id를 가리킨다.
   FOREIGN KEY (mem_id) REFERENCES member(mem_id) 
);

INSERT INTO member VALUES('TWC', '트와이스', 9, '서울', '02', '11111111', 167, '2015.10.19');
INSERT INTO member VALUES('BLK', '블랙핑크', 4, '경남', '055', '22222222', 163, '2016.08.08');
INSERT INTO member VALUES('WMN', '여자친구', 6, '경기', '031', '33333333', 166, '2015.01.15');
INSERT INTO member VALUES('OMY', '오마이걸', 7, '서울', NULL, NULL, 160, '2015.04.21');
INSERT INTO member VALUES('GRL', '소녀시대', 8, '서울', '02', '44444444', 168, '2007.08.02');
INSERT INTO member VALUES('ITZ', '잇지', 5, '경남', NULL, NULL, 167, '2019.02.12');
INSERT INTO member VALUES('RED', '레드벨벳', 4, '경북', '054', '55555555', 161, '2014.08.01');
INSERT INTO member VALUES('APN', '에이핑크', 6, '경기', '031', '77777777', 164, '2011.02.10');
INSERT INTO member VALUES('SPC', '우주소녀', 13, '서울', '02', '88888888', 162, '2016.02.25');
INSERT INTO member VALUES('MMU', '마마무', 4, '전남', '061', '99999999', 165, '2014.06.19');

INSERT INTO buy VALUES(NULL, 'BLK', '지갑', NULL, 30, 2);
INSERT INTO buy VALUES(NULL, 'BLK', '맥북프로', '디지털', 1000, 1);
INSERT INTO buy VALUES(NULL, 'APN', '아이폰', '디지털', 200, 1);
INSERT INTO buy VALUES(NULL, 'MMU', '아이폰', '디지털', 200, 5);
INSERT INTO buy VALUES(NULL, 'BLK', '청바지', '패션', 50, 3);
INSERT INTO buy VALUES(NULL, 'MMU', '에어팟', '디지털', 80, 10);
INSERT INTO buy VALUES(NULL, 'GRL', '혼공SQL', '서적', 15, 5);
INSERT INTO buy VALUES(NULL, 'APN', '혼공SQL', '서적', 15, 2);
INSERT INTO buy VALUES(NULL, 'APN', '청바지', '패션', 50, 1);
INSERT INTO buy VALUES(NULL, 'MMU', '지갑', NULL, 30, 1);
INSERT INTO buy VALUES(NULL, 'APN', '혼공SQL', '서적', 15, 1);
INSERT INTO buy VALUES(NULL, 'MMU', '지갑', NULL, 30, 4);

SELECT * FROM member;
SELECT * FROM buy;
```

<br>

### SELECT 와 FROM

(SQL의 명령문은 대문자로 작성하는것이 좋지만 편의상 소문자로 작성했습니다.)

- select, from에 앞서 SQL문법은 다음과 같은 순서로 작성된다.
- 여기서 실제 작동 순서는 주석의 숫자대로 흘러간다.
- 아래에 적어둔 내용처럼 생각해보면 순서를 알기 쉽다.

```sql
	SELECT 열_이름 -- 5
		FROM 테이블_이름 -- 1
	 WHERE 조건식 -- 2
GROUP BY 열_이름 -- 3
  HAVING 조건식 -- 4
ORDER BY 열_이름 -- 6
   LIMIT 숫자 -- 7

어떤 테이블에서(from), 내가 정한 조건으로(where), 그룹화를 하는데(group by), 
그룹을 묶기위한 조건을 설정해서(having) 뽑아낸다(select).
뽑아낸 열은 (order by)로 정렬하고, 출력의 개수는 (limit)으로 제한한다. 
```

```sql
use market_db; -- 처음에만 사용

-- market_db의 member 테이블 전체를 조회
select * 
	from member;

-- member 테이블의 mem_name, addr을 조회
select mem_name, addr 
	from member;
```

<br>

### WHERE

- where절에서는 조회의 조건을 정할수 있다.

```sql
-- member 테이블의 키가 165이상, 멤버의 숫자가 4명 초과인 정보 전체를 조회
select *
	from member
 where height >= 165 and mem_number > 4;

-- or은 둘 중 하나만 참이어도 가져온다.
-- where height >= 165 or mem_number > 4; 

-- 키가 165이상, 169미만
-- where height >= 165 and height < 169

-- where height between 165 and 168 도 가능하다.
```

<br>

### IN

```sql
select mem_name, addr
	from member
 where addr = '경기' or addr = '전남' or addr = '경남';

-- in()을 사용해서 아래와 같이 나타낼 수 있다.
select mem_name, addr
	from member
 where addr in('경기', '전남', '경남');
```

<br>

### LIKE

- 문자열의 일부 글자를 검색하기 위해 사용한다.

```sql
-- 첫 글자가 우로 시작하는 회원 무엇이든(%) 허용
select *
	from member
 where mem_name like '우%';
```

<br>

### 서브쿼리(subquary)

* 서브쿼리(subquery)란 다른 쿼리 내부에 포함되어 있는 SELETE 문을 의미한다.

* 서브쿼리도 종류가 있는데 서브쿼리의 종류는 다음과 같다.

  ``` SQL
  SELECT col1, (SELECT ...) -- 스칼라 서브쿼리(Scalar Subquery): 하나의 컬럼처럼 사용 (표현 용도)
  FROM (SELECT ...)         -- 인라인 뷰(Inline View): 하나의 테이블처럼 사용 (테이블 대체 용도)
  WHERE col = (SELECT ...)  -- 일반 서브쿼리: 하나의 변수(상수)처럼 사용 (서브쿼리의 결과에 따라 달라지는 조건절)
  ```

```sql
-- 그룹 이름이 에이핑크인 그룹의 평균키보다 큰 그룹의 이름과 평균키
select mem_name, height
	from member
 where height > (select height
									 from member
									where mem_name = '에이핑크' );
```

<br>

### 서브쿼리 응용해보기

```sql
-- 이름이 핑크로 끝나는 그룹의 인원 수(6, 4)와 하나라도 같거나, 평균키가 167 이하인 그룹(에이핑크, 블랙핑크, 잇지, 마마무, 오마이걸, 레드벨벳, 우주소녀, 트와이스, 여자친구)의 이름을 출력
select mem_name
  from member
 where mem_number in(select mem_number 
											  from member 
											 where mem_name like '%핑크') or height <= 167;
											 
-- 이름이 핑크로 끝나는 그룹들의 각 인원수(6, 4)와 다르고,
-- 평균키가 167 이하인 그룹(잇지, 오마이걸, 우주소녀, 트와이스)의 이름을 출력
select mem_name
  from member
 where mem_number not in(select mem_number
						 						   from member
						  						where mem_name like '%핑크') and height <= 167;
											 
```

```sql
-- 이름이 핑크로 끝나는 그룹의 인원 수와 하나라도 같거나, 평균키가 167 이하인 그룹의 이름을 출력
select mem_name
  from member
 where mem_number IN (select mem_number 
											  from member 
											 where mem_name like '%핑크');
```

<br>

### ORDER BY

```sql
	select mem_id, mem_name, debut_date
	  from member
order by debut_date desc; -- desc는 내림차순, asc는 오름차순, 기본은 오름차순이라 적지 않아도 된다.
```

<br>

### LIMIT

- limit은 출력의 개수를 입력한 숫자만큼 제한한다.
- limit의 형식은 LIMIT 시작, 개수다.

```sql
-- limit에 숫자 1개만 넣으면 개수만 제한한다.
	select mem_id, mem_name, debut_date
	  from member
order by debut_date, desc limit 1; 
```

- limit의 시작을 정할때에, 시작 인덱스는 0이다.

```sql
select mem_name, height
  from member
order by height desc limit 0, 1; -- 시작지점 0부터 1개만 출력

-- 출력결과를 보면 평균키가 168로 가장 큰 소녀시대가 출력된다.
-- 키가 2번째로 큰 그룹의 키 보다 작은 그룹들의 그룹 명을 출력

select mem_name
  from member
 where height < (select height
								   from member
							 order by height desc
								  limit 1, 1);
```

<br>

### DISTINCT

- 중복을 제거한다.

```sql
select distinct addr
  from member;
```

<br>

### GROUP BY

- 그룹으로 묶어주는 역할을 한다.
- GROUP BY와 함께 집계함수를 사용하는데, 주로 사용하는 함수의 종류는 다음과 같다.

| SUM()           | 합계                  |
| --------------- | --------------------- |
| AVG()           | 평균                  |
| MIN()           | 최소                  |
| MAX()           | 최대                  |
| COUNT()         | 행의 개수             |
| COUNT(DISTINCT) | 중복이 없는 행의 개수 |

```sql
select mem_id, sum(amount)
from buy
group by mem_id; -- mem_id로 그룹화
```

<br>

### HAVING

- 집계함수는 조건절(where)에서 사용할 수 없다.
- 이 때에 where 대신 사용하는것이 having이다.

```sql
	select mem_id, sum(price*amount)
	  from buy
group by mem_id
  having sum(price*amount) > 1000
order by sum(price*amount) desc;

-- 집계함수를 사용하다보면 이름이 길어지기때문에 다음과 같이 사용이 가능하다.
	select mem_id, sum(price*amount) buy_sum
	  from buy
group by mem_id
  having buy_sum > 1000
order by buy_sum desc;
```

<br>

### 실습 문제

```sql
-- buy 테이블로 진행
-- 분류 별로 가장 많이 판매된 순으로 정렬해서 출력

	select group_name 분류, sum(amount) 판매량
		from buy
group by 분류
order by 판매량 desc;
```