
### 시작하기 전에
1. AWS는 잘못 생성 시 많은 요금이 부과될수 있으므로 프리티어를 꼭 확인해야합니다.
2. 아래 설명에서 표기한것 이외에 설정을 건드리면 요금이 부과될수 있으니 주의해야합니다.

<br>


### 1. AWS RDS 생성하기

1. Amazon AWS 가입 후 RDS 접속
![](https://i.imgur.com/agphMb4.png)

<br>


2. 데이터베이스 생성 클릭
![](https://i.imgur.com/pidH8WE.png)


<br>

3. MariaDB 선택
![](https://i.imgur.com/RhWYQJb.png)


<br>

4. 사용하려는 DB버전 선택 후 **프리티어** 반드시 체크 
![](https://i.imgur.com/kZdy4IN.png)

<br>

5. 사용자 이름(id) 선택 및 암호 생성, 암호는 영문대문자, 숫자, 특수문자를 포함합니다.
![](https://i.imgur.com/57rWfat.png)

<br>

6. 사용할 DB요금제는 db.t4g.micro 사용
![](Screenshot%202024-08-13%20at%202.02.27%20PM.png)

<br>

7. 스토리지는 기본값을 사용합니다.
![](https://i.imgur.com/Rt2A2B0.png)


<br>

8. 퍼블릭 엑세스 설정을 "예"로 변경
![](https://i.imgur.com/qpOFMuT.png)

<br>

9. 보안 그룹 '새로 생성', 보안 그룹의 이름을 지정해줍니다.
![](https://i.imgur.com/b5cZRoL.png)

<br>

10. 보안 그룹 추가 구성의 데이터베이스 포트를 확인해줍니다.(기본 3306)
![](https://i.imgur.com/Q1qykel.png)

<br>

11. 데이터베이스 이름을 지정해줍니다. 파라미터 그룹은 건드리지 않았습니다. 백업기간은 7일로 늘려줬습니다.
![](https://i.imgur.com/DZxC025.png)


<br>

12. DB생성 전 프리티어 사용량 확인
![](https://i.imgur.com/qKx7XDx.png)


<br>

###  2. RDS 설정하기

1. 데이터베이스 생성 후 파라미터 그룹으로 넘어가 **파라미터 그룹 생성**을 클릭
![](https://i.imgur.com/2aJVXO3.png)

<br>

2. 파라미터 그룹 이름, 설명, 엔진 유형, 그룹 패밀리를 설정 후 생성 합니다.
* 그룹 이름은 자유입니다.
* 설명은 제가 실수를 했는데, 영어로 작성해야합니다.
* 엔진 유형은 MariaDB를 사용
* 그룹 패밀리는 생성시 사용한 MariaDB의 버전과 똑같이 합니다.
![](https://i.imgur.com/0B0tFAo.png)

<br>

3. 파라미터 그룹을 생성 후 파라미터 그룹 수정을 클릭해 파라미터를 수정합니다.
![](https://i.imgur.com/sjuZl8M.png)
`time_zone을 검색해 Asia/Seoul로 변경`

<br>


![](https://i.imgur.com/ar3Jggd.png)
`char을 검색해 utf8mb4로 변경, utf8mb4는 이모지를 인식합니다.`

<br>



![](https://i.imgur.com/JIX03Vc.png)
![](https://i.imgur.com/kssgIpy.png)
`collation을 검색해 utf8mb4_general_ci로 변경`

<br>


![](https://i.imgur.com/r9nHsxa.png)
`lower를 검색해 1로 변경, 1일경우 테이블명의 대소문자를 구분하지 않습니다.`

<br>

3. 수정 완료 후 데이터베이스 탭의 생성된 데이터베이스 선택 후 수정버튼 클릭
![](https://i.imgur.com/PJEJChb.png)


<br>

4. 파라미터 그룹을 설정한 그룹 이름으로 변경합니다.
![](https://i.imgur.com/kKBVJ6v.png)


<br>

5. 즉시 적용후 수정
![](https://i.imgur.com/H5tiaAr.png)

<br>

6. 재부팅 합니다.
![](https://i.imgur.com/cAjyS5Z.png)

<br>

### 3. 로컬 PC에서 접속하기

1. 생성된 데이터베이스 선택 후 연결 및 보안의 보안그룹을 클릭합니다.
![](https://i.imgur.com/HXCEcwI.png)

<br>


2. 보안 그룹 ID를 미리 복사해두고 해당 ID를 클릭해서 페이지로 접속합니다.
![](https://i.imgur.com/1B8jsGm.png)

<br>

3. 인바운드 규칙 편집을 클릭
![](https://i.imgur.com/CtZubA2.png)


<br>

4. 규칙 추가를 클릭해서 보안그룹 ID를 붙혀넣기하고 기존에 있던 탭은 내 IP로 변경후에 저장합니다.
![](https://i.imgur.com/apxnbYi.png)


<br>

5. MySQL workbench를 설치 후 스패너 버튼 클릭
![](https://i.imgur.com/nSpPWIT.png)

<br>

6. 그림과 같이 설정 후 Test Connection 클릭
![](https://i.imgur.com/3w8TiPg.png)


<br>


7. 성공 시 아래의 메세지가 뜹니다. 

![](https://i.imgur.com/BybMyHp.png)


<br>


8. close버튼 클릭 후 접속하면 이제 DB를 사용할 수 있습니다.
![](https://i.imgur.com/Zhv2Enn.png)

