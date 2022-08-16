## Database

* 데이터베이스는 **체계화된 데이터**의 모임
* 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
* 논리적으로 연관된(하나 이상의) 자료의 모음, 내용을 구조화 하여 검색과 갱신의 효율화를 꾀한것
* 몇 개의 **자료 파일을 조직적으로 통합**하여 자료 항목의 **중복을 없애고** **자료를 구조화**하여 기억시켜 놓은 자료의 집합체

<br>

#### 데이터베이스로 얻는 장점들

* 데이터 중복 최소화
* 데이터 무결성(정확한 정보를 저장)
* 데이터 일관성
* 데이터 독립성(물리적 / 논리적)
* 데이터 표준화
* 데이터 보안 유지

<br>

## RDB

#### 관계형 데이터베이스(RDB, Relational Database)

* 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
* 키(Key)와 값(Value)들의 간단한 관계를 표 형태로 정리한 데이터베이스

#### 스키마(schema)

* 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적 명세를 기술한 것

| column  | datatype |
| ------- | -------- |
| id      | INT      |
| name    | TEXT     |
| address | TEXT     |
| age     | INT      |

#### 테이블(table)

* 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

| id   | name   | address | age  |
| ---- | ------ | ------- | ---- |
| 1    | 홍길동 | 제주    | 20   |
| 2    | 김길동 | 서울    | 30   |
| 3    | 박길동 | 독도    | 40   |

* 행(row) : 실제 데이터가 저장되는 형태
* **기본키(Primary Key)** : 각 행(레코드)의 고유 값
  * 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용 됨(여기서는 id가 PK)

<br>

## RDBMS

* 관계형 데이터베이스 관리 시스템
  * 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미

<br>

## SQL

#### SQL(Structured Query Language)

* 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적 프로그래밍 언어
* 데이터베이스 스키마 생성 및 수정
* 자료의 검색 및 관리
* 데이터베이스 객체 접근 조정 관리

| 분류                            | 개념                                                   | 예시                            |
| ------------------------------- | ------------------------------------------------------ | ------------------------------- |
| DDL(Data Definition Language)   | 관계형 데이터베이스 구조를 정의하기 위한 명령어        | CREATE, DROP, ALTER             |
| DML(Data Manipulation Language) | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어  | INSERT, SELECT, UPDATE, DELETE  |
| DCL(Data Control Language)      | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어 | GRANT, REVOKE, COMMIT, ROLLBACK |

<br>

## 명령어(SQLite 기준)

테이블 생성 및 삭제

``` sqlite
-- classmates 라는 이름의 테이블 생성
CREATE TABLE classmates (
	id INTEGER PRIMARY KEY,
  name TEXT
);

-- 테이블 목록 조회
.table

-- 특정 테이블 스키마 조회
.schema classmates

-- 값 추가
INSERT INTO classmates VALUE(1, '조세호');

-- 테이블 조회
SELECT * FROM classmates;

-- 테이블 삭제
DROP TABLE classmates;
```

<br>

#### 필드 제약 조건

* NOT NULL : NULL 값 입력 금지
* UNIQUE : 중복 값 입력 금지(NULL 값은 중복 입력 가능)
* PRIMARY KEY : 테이블에서 반드시 하나. NOT NULL + UNIQUE
* FOREIGN KEY : 외래키, 다른 테이블의 key
* CHECK : 조건으로 설정된 값만 입력 허용
* DEFAULT : 기본 설정 값

``` sqlite
CREATE TABLE students (
	id INTEGER PRIMATY KEY, -- PK
  name TEXT NOT NULL, -- null값이 될 수 없음
  age INTEGER DEFAULT 1 CHECK (0 < age) -- 나이는 0보다 큰 값을 확인, 기본은 1
)
```

<br>

#### INSERT

* "insert a single row into a table"

* > INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3)

* > INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2)

``` sqlite
INSERT INFO classmates(name, age) VALUES ('홍길동', 23);
```

#### SELECT

* "query data from table"
* 테이블에서 데이터를 조회
* SELECT 문은 SQLite에서 가장 기본이 되는 문이며 다양한 절(clause)와 함께 사용
  * ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY

``` sqlite
SELECT rowid, name FROM classmates;
```

#### LIMIT

* "constrain the number of rows returned by query"
* 쿼리에서 반환되는 행 수를 제한
* 특정 행부터 시작해서 조회하기 위해 **OFFSET** 키워드와 함께 사용하기도 함

OFFSET : 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형

예시 

1. 문자열 'abcdef' 에서 문자 'c'는 시작점 'a'에서 2의 OFFSET을 지님
2. SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5
   * 6번째 행 부터 10개 행을 조회(6번째 행부터 10개를 출력)
   * 0부터 시작함

``` sqlite
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2; -- classmates 테이블에서 id, name 컬럼값을 세 번째에 있는 하나만 조회
```

#### WHERE

* "specify the search condition for rows returned by the query"
* 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정

``` sqlite
SELECT * FROM classmates WHERE address = 'seoul' -- classmates 테이블에서 주소가 서울인 값을 출력 
```

#### SELECT DISTINCT 

* "remove duplicate rows in the result set"
* 조회 결과에서 중복 행을 제거
* DISTINCT 절은 SELECT 키워드 바로 뒤에서 작성해야 함

``` sqlite
SELECT DISTINCT age FROM classmates -- age의 중복값 제거
```

<br>