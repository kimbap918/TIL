## CASE

* CASE문은 특정 상황에서 데이터를 변환하여 사용할 수 있음

* ELSE를 생략하는 경우 NULL값이 지정됨

  ``` sqlite
  CASE
  	WHEN 조건식 THEN 식
  	WHEN 조건식 THEN 식
  	ELSE 식
  END
  
  SELECT
  	id,
  	CASE
  		WHEN gender = 1 THEN '남자'
  		WHEN gender = 2 THEN '여자'
  	END AS 성별
  FROM healthcare
  LIMIT 5;
  ```

<br>

## 서브쿼리

* 단일행 서브쿼리 
  * 서브쿼리의 결과가 0 또는 1개인 경우
  * 단일행 비교 연산자와 함께 사용 (=, <, <=, >= <>)
* 다중행 서브쿼리
  * 서브쿼리 결과가 2개 이상인 경우
  * 다중행 비교 연산자와 함께 사용(IN, EXISTS 등)
* 다중컬럼 서브쿼리

<br>

``` sqlite
SELECT COUNT(*)
FROM users
WHERE age = 15;

-- 서브쿼리
SELECT COUNT(*)
FROM users	
WHERE age = (SELECT MIN(age) FROM users);

-- 단일행 서브쿼리(WHERE)
SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

-- 단일행 서브쿼리(WHERE)
SELECT COUNT(*)
FROM users
WHERE contry = (SELECT contry FROM users WHERE last_name = '유' AND first_name = '은정')

-- 단일행 서브쿼리(SELECT)
SELECT (SELECT COUNT(*) FROM users) AS 총인원,
			 (SELECT AVG(salary) FROM users) AS 평균연봉;

-- 단일행 서브쿼리(UPDATE에서의 활용)
UPDATE users
SET balance = (SELECT AVG(balance) FROM users);

-- 다중행 서브쿼리
-- 이은정과 같은 지역에 사는 사람 수?
SELECT COUNT(*)
FROM users
WHERE contry IN (
	SELECT country
  FROM user
  WHERE first_name = '은정' AND last_name = '이'
);

-- 다중컬럼 서브쿼리
-- 특정 성씨별로 가장 적은 나이
SELECT
	last_name,
	first_name,
	age
FROM users
WHERE (last_name, age) IN (SELECT last_name, MIN(age) FROM users GROUP BY last_name) 
ORDER BY = last_name;
```

