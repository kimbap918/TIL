## SQL(2) - 기본 함수와 연산

#### 문자열 함수

* SUBSTR(문자열, start, length) : 문자열 자르기

  * 시작 인덱스는 1, 마지막 인덱스는 -1

* TRIM(문자열), LTRIM(문자열), RTRIM(문자열) : 문자열 공백 제거

* LENGTH(문자열) : 문자열 길이

  ``` sqlite
  SELECT LENGTH(first_name), first_name
    FROM users
   LIMIT 5;
  ```

* REPLACE(문자열, 패턴, 변경값) : 패턴에 일치하는 부분을 변경

  ``` sqlite
  SELECT first_name, REPLACE(phone, '-', '')
    FROM users
   LIMIT 5;
  ```

  

* UPPER(문자열), LOWER(문자열) : 대소문자 변경

* || : 문자열 합치기(concatenation)

  ``` sqlite
  SELECT last_name || first_name 이름, age, country, phone, balance
  	FROM users
   LIMIT 5;
  ```

<br>

#### 숫자 함수

* ABS(숫자) : 절대 값

* SIGN(숫자) : 부호(양수 1, 음수 -1, 0 0)

* MOD(숫자1, 숫자2) : 숫자1을 숫자2로 나눈 나머지

  ``` sqlite
  SELECT MOD(5, 2)
    FROM users
   LIMIT 1;
  ```

* CEIL(숫자), FLOOR(숫자), ROUND(숫자, 자리) : 올림, 내림, 반올림

  ``` sqlite
  SELECT CEIL(3, 14), FLOOR(3.14), ROUND(3.14)
    FROM users
   LIMIT 1;
  ```

* POWER(숫자1, 숫자2) : 숫자1의 숫자2 제곱

  ``` sqlite
  SELECT POWER(9, 2) FROM users LIMIT 1;
  ```

* SQRT(숫자) : 제곱근 

  ``` sqlite
  SELECT SQRT(9) FROM users LIMIT 1;
  ```

<br>

#### 산술 연산자

* +, -, *, /와 같은 산술 연산자와 우선 순위를 지정하는 ()기호를 연산에 활용할 수 있음

<br>

## GROUP BY

#### GROUP BY

* "make a set of summary rows from a set of rows"

* SELECT 문의 optional 절

* 행 집합에서 요약 행 집합을 만듦

* 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦

* **문장에 WHERE절이 포함된 경우 반드시 WHERE절 뒤에 작성해야함**

  ``` sqlite
  SELECT * FROM 테이블이름 GROUP BY 컬럼1, 컬럼2;
  ```

* 지정된 컬럼의 값이 같은 행들로 묶음

* **집계함수와 활용하였을 때 의미가 있음**

* 그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨짐

``` sqlite
-- 성별 갯수
SELECT COUNT(*) FROM users GROUP BY last_name;
```

<br>

#### HAVING

* 집계함수는 WHERE절의 조건식에서는 **사용할 수 없음**(실행 순서에 의해)

  * WHERE로 처리하는 것이 GROUP BY 그룹화보다 순서상 앞서있기 때문

* 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 HAVING을 활용

  ``` sqlite
  SELECT * FROM 테이블 이름 GROUP BY 컬럼1, 컬럼2
  HAVING 그룹조건;
  ```

  <br>

#### SELECT 문장 실행 순서

* FROM => WHERE => GROUP BY => HAVING => SELECT => ORDER BY
* FROM 테이블을 대상으로
* WHERE 제약조건에 맞춰서 뽑아서
* GROUP BY 그룹화 한다.
* HAVING 그룹 중에 조건과 맞는 것 만을
* SELECT 조회하여
* ORDER BY 정렬하고
* LIMIT/OFFSET 특정 위치의 값을 가져온다.

``` sqlite
  SELECT 컬럼명
    FROM 테이블명
   WHERE 조건식
GROUP BY 컬럼 혹은 표현식
  HAVING 그룹조건식
ORDER BY 컬럼 혹은 표현식
   LIMIT 숫자 OFFSET 숫자;
```

<br>

## ALTER TABLE

#### ALTER TABLE

1. 테이블 이름 변경
2. 새로운 column추가
3. column 이름 수정(new in sqlite 3.35.0)
4. column 삭제(new in sqlite 3.35.0)

``` sqlite
-- 1. 테이블 이름 변경
ALTER TABLE table_name
rename to new_name;

-- 2. 새로운 컬럼 추가
ALTER TABLE table_name
ADD COLUMN column_definition;

-- 3. 컬럼 이름 수정
ALTER TABLE table_name
RENAME COLUMN current_name to new_name;

-- 4. 컬럼 삭제
ALTER TABLE table_name
DROP COLUMN column_name;
```

<br>