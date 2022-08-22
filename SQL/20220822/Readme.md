### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT * FROM playlist_track A ORDER BY A.PlaylistId DESC LIMIT 5;
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT * FROM tracks B ORDER BY B.TrackId LIMIT 5;
``` 
 
### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
SELECT * FROM playlist_track A, tracks B WHERE A.trackId = B.trackId ORDER BY A.PlaylistId DESC LIMIT 10;
```  
### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT * FROM playlist_track A, tracks B WHERE A.trackId = B.trackId and A.PlaylistId = 10 ORDER BY B.Name  DESC LIMIT 5;
``` 

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT *
FROM tracks A JOIN artists B
ON A.Composer = B.Name;
```

```
SELECT *
FROM 테이블1 [INNER](생략가능) JOIN 테이블2
ON 테이블1.컬럼 = 테이블2.컬럼
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT *
FROM tracks A LEFT OUTER JOIN artists B
ON A.Composer = B.Name;
```

```
SELECT *
FROM 테이블1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2
ON 테이블1.컬럼 = 테이블2.컬럼
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
INNER JOIN은 두 테이블이 모두 일치하는(교집합) 값을 반환하지만 LEFT JOIN은 OUTER JOIN이라 동일한 값이 없는 행도 반환하기 때문
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT * FROM invoice_items ORDER BY InvoiceId LIMIT 5;
``` 

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT * FROM invoices ORDER BY InvoiceId LIMIT 5;
``` 

### 10. 각 invoice_items에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT * FROM invoice_items A, invoices B WHERE A.invoiceId = B.invoiceId ORDER BY A.InvoiceId DESC LIMIT 5;
``` 


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT * FROM invoices A, customers B WHERE A.CustomerId = B.CustomerId ORDER BY A.InvoiceId DESC LIMIT 5;
``` 

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT * FROM invoice_items A, invoices B, customers C WHERE A.invoiceId = B.invoiceId AND B.CustomerId = C.CustomerID ORDER BY A.InvoiceId DESC LIMIT 5;
```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT C.Country, COUNT(A.InvoiceLineId) FROM invoice_items A, invoices B, customers C WHERE A.invoiceId = B.invoiceId AND B.CustomerId = C.CustomerID AND B.InvoiceDate LIKE '2010%' GROUP BY C.Country ORDER BY COUNT(A.InvoiceLineId) DESC LIMIT 10;
```


