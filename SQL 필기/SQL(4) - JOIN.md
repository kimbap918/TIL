## Join

관계형 데이터베이스의 가장 큰 장점이자 핵심적인 기능

일반적으로 데이터베이스에는 하나의 테이블에 많은 데이터를 저장하는것이 아닌, 여러 테이블로 나눠 저장하게 되며, 여러 테이블을 결합(Join)하여 출력하여 활용한다. 일반적으로 레코드는 기본키(PK)나 외래키(FK) 값의 관계에 의해 결합한다.



#### 대표적인 JOIN

* INNER JOIN : 두 테이블에 모두 일치하는 행만 반환 (교집합)

  ``` sqlite
  -- 테이블1과 테이블2에서 값이 일치하는 것들만 가져옴
  SELECT *
  FROM 테이블1 [INNER](생략가능) JOIN 테이블2
  ON 테이블1.컬럼 = 테이블2.컬럼
  
  SELECT *
  FROM users JOIN role
  ON users.role_id = role.id;
  -- 스태프(2)만 출력
  SELECT *
  FROM users JOIN role
  ON users.role_id = role.id
  WHERE role.id = 2;
  -- 이름을 내림차순으로
  SELECT *
  FROM users JOIN role
  ON users.role_id = role.id
  WHERE role.id = 2
  ORDER BY users.name DESC;
  ```

* OUTER JOIN : 동일한 값이 없는 행도 반환할때 사용 

  * 기준이 되는 테이블에 따라 LEFT/RIGHT/FULL을 지정함

  ``` sqlite
  SELECT *
  FROM 테이블1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2
  ON 테이블1.컬럼 = 테이블2.컬럼
  
  SELECT *
  FROM articles LEFT OUTER JOIN users
  ON articles.user_id = users.id;
  ```

* CROSS JOIN : 모든 데이터의 조합

  ``` sqlite
  SELECT *
  FROM users CROSS JOIN role
  ```

  