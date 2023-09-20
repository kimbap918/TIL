## UPDATE

|      | 구문   | 예시                                                         |
| ---- | ------ | ------------------------------------------------------------ |
| C    | INSERT | **INSERT INTO** 테이블 이름(컬럼1, 컬럼2, ...) **VALUES** (값1, 값2) |
| R    | SELECT | **SELECT** * **FROM** 테이블 이름 **WHERE** 조건;            |
| U    | UPDATE | **UPDATE** 테이블이름 **SET** 컬럼1=값1, 컬럼2=값2 **WHERE** 조건; |
| D    | DELETE | **DELETE FROM** 테이블이름 **WHERE** 조건;                   |

<br>

## WHERE

WHERE절에서 사용할 수 있는 연산자

* 비교 연산자

  * =, >, >=, <, <= 는 숫자 혹은 문자 값의 대/소, 동일 여부를 확

    인하는 연산자

* 논리 연산자

  * AND
    * 앞에 있는 조건과 뒤에 있는 조건이 모두 참인 경우
  * OR
    * 앞의 조건이나 뒤의 조건이 참인 경우
  * NOT
    * 뒤에 오는 조건의 결과를 반대로

``` sqlite
-- 주의!
-- 1.키가 175이거나, 키가 183이면서 몸무게가 80인 사람
WHERE HEIGHT = 175 OR HEIGHT = 183 AND WEIGHT = 80;
-- 2. 키가 175 또는 183인 사람 중에서 몸무게가 80인 사람
WHERE (HEIGHT = 175 OR HEIGHT = 183) AND WEIGHT = 80;
```

* SQL 사용할 수 있는 연산자
  * BETWEEN 값1 AND 값2
    * 값1과 값2 사이의 비교(값1 <= 비교값 <= 값2)
  * IN(값1, 값2, ...)
    * 목록 중에 값이 하나라도 일치하면 성공
  * LIKE
    * 비교 문자열과 형태 일치
    * 와일드카드(% : 0개 이상 문자, _:1개 단일 문자)
  * IS NULL / IS NOT NULL
    * NULL 여부를 확인할 때는 항상 = 대신에 IS 사용
  * 부정 연산자
    * 같지 않다(!=, ^=, <>)
    * ~와 같지 않다.(NOT 컬럼명 =)
    * ~보다 크지 않다.(NOT 컬럼명 >)
* 연산자 우선순위
  * 1순위 : 괄호()
  * 2순위 : NOT
  * 3순위 : 비교 연산자, SQL
  * 4순위 : AND
  * 5순위 : OR

<br>

#### Aggregate function(집계함수)

* 값 집합에 대한 계산을 수행하고 단일 값을 반환
  * 여러 행으로부터 하나의 결괏값을 반환하는 함수
* SELECT  구문에서만 사용됨
* COUNT : 그룹 항목 수를 가져옴

``` sqlite
-- users에서 나이가 30과 같거나 더 큰 사람의 수
SELECT COUNT(*) FROM users WHERE age >= 30;
```

* AVG : 모든 값의 평균을 계산

``` sqlite
-- users에서 나이가 30과 같거나 더 큰 사람의 평균나이
SELECT AVG(age) FROM users WHERE age >= 30;
```

* MAX : 그룹에 있는 모든 값의 최대값을 가져옴

``` sqlite
-- users에서 제일 잔액이 많은 사람, 이름
SELECT MAX(balance), first_name FROM users;
```

* MIN : 그룹에 있는 모든 값의 최소값을 가져옴

``` sqlite
-- users에서 나이가 30과 같거나 더 큰 사람의 최소 나이
SELECT MIN(age) FROM users WHERE age >= 30;
-- users에서 나이가 30과 같거나 더 크면서 성이 '이' 씨인 사람의 이름과 최소 나이
SELECT MIN(age), first_name FROM users WHERE last_name = '이';
```

* SUM : 모든 값의 합을 계산
* 예시
  * 테이블 전체 행 수를 구하는 COUNT(*)
  * age 컬럼 전체 평균 값을 구하는 AVG(age)

<br>

#### LIKE

* "query data based on pattern matching"
* 패턴 일치를 기반으로 데이터를 조회하는 방법
* SQLite는 패턴 구성을 위한 2개의 wildcards를 제공
  * %(percent sign) : 0개 이상의 문자
  * _(underscore) : 임의의 단일 문자

``` sqlite
SELECT * FROM 테이블이름 WHERE 컬럼 LIKE '패턴';
```

| 와일드카드 패턴 |                                               |
| --------------- | --------------------------------------------- |
| 2%              | 2로 시작하는 값                               |
| %2              | 2로 끝나는 값                                 |
| %2%             | 2가 들어가는 값                               |
| _2%             | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
| 1___            | 1로 시작하고 총 4자리인 값                    |
| `2_%_%` / 2__%  | 2로 시작하고 적어도 3자리인 값                |

``` sqlite
SELECT COUNT(*) FROM users WHERE phone like '02-%';
```

<br>

#### ORDER BY

* "sort a result set of a query"
* 조회 결과 집합을 정렬
* SELECT 문에 추가하여 사용
* 정렬 순서를 위한 2개의 키워드 제공
  * ASC - 오름차순(기본)
  * DESC - 내림차순

``` sqlite
SELECT * FROM 테이블이름 ORDER BY 컬럼 ASC;
SELECT * FROM 테이블이름 ORDER BY 컬럼 DESC;
-- users에서 나이 오름차순으로 상위 10개만 나열한다면?
SELECT first_name FROM users ORDER BY age ASC LIMIT 10;
```

