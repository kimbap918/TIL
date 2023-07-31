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
group by m.mem_name
having sum(b.price*b.amount) >= 1000;
```