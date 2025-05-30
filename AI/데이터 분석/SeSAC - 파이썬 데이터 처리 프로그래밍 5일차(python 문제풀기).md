## SeSAC - 파이썬 데이터 처리 프로그래밍 5일차

2023.08.04

<br>

## 파이썬 실습하기


### up/down 게임(1)

- 프로그램 실행시 랜덤으로 1 ~ 100 사이
- 10번의 기회가 있고 10번동안 숫자를 입력 받아 숫자를 맞추는 게임
- 정답이 아닐 때마다 up/down 출력
- 정답을 맞추면 "정답" 출력
- 10번의 기회동안 정답을 못 맞췄다면 "실패"를 출력

```python
import random

computer = random.randint(1, 100)
cnt = 0 

while True:
    user = int(input())
    cnt += 1 # 10번의 입력할 기회
		# 10번을 입력해서 실패했다면
    if cnt == 10:
        print("실패")
        break # 반복문을 빠져나옴
		# 컴퓨터보다 내 값이 작으면
    if computer > user:
        print("up")
		# 컴퓨터보다 내 값이 크면
    elif computer < user:
        print("down")
		# 컴퓨터와 내 값이 같다면
    else: 
        print("정답")
        break
```

<br>

### up/down게임(2)

- 입력값이 문자거나, 입력값이 1~100범위를 벗어나면 횟수차감이 발생하지 않도록 변경하기

```python
import random

computer = random.randint(1, 100)
cnt = 0 

while True:
    user = input()
    cnt += 1

		# 입력값이 문자거나, 입력값이 1~100 범위를 벗어나면
    if not user.isdigit() or int(user) < 1 or int(user) > 100:
        print("1에서 100사이의 정수를 입력하세요")
        cnt -= 1 # 남은 횟수 차감 없음
        print("남은 횟수 : "+str(10-cnt)) # 남은 횟수를 표시
        continue 
		
		# 정수형으로 형변환
    user = int(user)
    
    if cnt == 10:
        print("실패")
        break
    if computer > user:
        print("up")
        print("남은 횟수 : "+str(10-cnt))
    elif computer < user:
        print("down")
        print("남은 횟수 : "+str(10-cnt))
    else:
        print("정답")
        break
```

```
50
down
남은 횟수 : 9
 25
down
남은 횟수 : 8
 15
down
남은 횟수 : 7
 10
down
남은 횟수 : 6
 5
down
남은 횟수 : 5
 4
down
남은 횟수 : 4
 바보멍청아
1에서 100사이의 정수를 입력하세요
남은 횟수 : 4
 3
정답
```

<br>

### up/down게임(3)

- 메뉴를 만들어 유저가 기능을 선택할 수 있게 작성하기

```python
import random

# 유저명
def name():
    print("안녕하세요! 유저 이름을 입력해주세요.")
    user_name = input()
    menu(user_name) #  입력받은 유저명을 인자로 해서 메뉴로 넘긴다.

# 메뉴
def menu(name):  
    while True:
				# 유저 메뉴 선택
        print(name+"님, 메뉴를 숫자로 선택해주세요.")
        print("1. 게임 시작")
        print("2. 게임 종료")
        user_input = int(input())
		    
				# 1을 입력하면 게임시작
        if user_input == 1:
            start_game()
				# 2를 입력하면 게임종료
        else:
            print("게임을 종료합니다.")
            break

# 게임화면
def start_game():
    computer = random.randint(1, 100)
    cnt = 0 
    print("1~100사이의 숫자를 입력해주세요")
    
    while True:
        user = input()
        cnt += 1
    
        if not user.isdigit() or int(user) < 1 or int(user) > 100:
            print("1에서 100사이의 정수를 입력하세요")
            cnt -= 1
            print("남은 횟수 : "+str(10-cnt))
            continue 
    
        user = int(user)
        
        if cnt == 10:
            print("실패")
            break
        if computer > user:
            print("up")
            print("남은 횟수 : "+str(10-cnt))
        elif computer < user:
            print("down")
            print("남은 횟수 : "+str(10-cnt))
        else:
            print("정답입니다! 메인화면으로 이동합니다.")
            break

name()
```
``` text
안녕하세요! 유저 이름을 입력해주세요.

 최준혁

최준혁님, 메뉴를 숫자로 선택해주세요.
1. 게임 시작
2. 게임 종료

 1

1~100사이의 숫자를 입력해주세요

 50

up
남은 횟수 : 9

 75

up
남은 횟수 : 8

 85

up
남은 횟수 : 7

 95

down
남은 횟수 : 6

 90

up
남은 횟수 : 5

 92

up
남은 횟수 : 4

 93

up
남은 횟수 : 3

 94

정답입니다! 메인화면으로 이동합니다.
최준혁님, 메뉴를 숫자로 선택해주세요.
1. 게임 시작
2. 게임 종료

 2

게임을 종료합니다.
```

<br>

### up/down 게임(4)
* 성공, 실패 횟수 출력하기, 메뉴 만들기
``` python
import random
# 성공, 실패, 성공 평균 시도횟수
success = 0
fail = 0
avg_try = 0

def name():
    print("안녕하세요! 유저 이름을 입력해주세요.")
    user_name = input()
    menu(user_name)

def menu(name):   
    while True:
        print(name+"님, 메뉴를 숫자로 선택해주세요.")
        print("1. 게임 시작")
        print("2. 기록 보기")
        print("3. 게임 종료")
        user_input = int(input())
    
        if user_input == 1:
            start_game()
        # 기록 보기 메뉴 추가
        elif user_input == 2:
            print(name+"님의 기록을 확인합니다.")
            
            print("성공 : "+str(success)+"회")
            print("실패 : "+str(fail)+"회")
            if success == 0:
                print("평균 시도 횟수 : 0회")
            else: 
                print("평균 시도 횟수 : "+str(avg_try/(success+fail)))
        else:    
            print("게임을 종료합니다.")
            break
        
def start_game():
    global success
    global fail
    global avg_try
    
    computer = random.randint(1, 100)
    cnt = 0 
    print("1~100사이의 숫자를 입력해주세요")
    
    while True:
        user = input()
        cnt += 1
        avg_try += 1
    
        if not user.isdigit() or int(user) < 1 or int(user) > 100:
            print("1에서 100사이의 정수를 입력하세요")
            cnt -= 1
            print("남은 횟수 : "+str(10-cnt))
            continue 
    
        user = int(user)
        
        if cnt == 10:
            print("실패")
            fail += 1
            break
        if computer > user:
            print("up")
            print("남은 횟수 : "+str(10-cnt))
        elif computer < user:
            print("down")
            print("남은 횟수 : "+str(10-cnt))
        else:
            print("정답입니다! 메인화면으로 이동합니다.")
            success += 1
            break


name()
```

<br>

## pandas 기초

<br>


### 시리즈와 데이터프레임

1. 시리즈
* 시리즈는 1차원 데이터
* 시리즈는 리스트와는 다르게 같은 자료형을 삽입해야 성능이 보장된다.
* 인덱스 지정이 가능하다.
``` python
import pandas as pd

df = pd.read_csv("bike.csv")

# 시리즈

ser = pd.Series([1,2,3,4], index=["a", "b", "c", "d"])
ser["a"]
-> 1
```

2. 데이터프레임
* 데이터프레임은 2차원 데이터
``` python
df = pd.DataFrame({
    "aa": [1, 2, 3],
    "bb": ["a", "b", "c"]
})
df
```

|     | aa  | bb  |    
| --- | --- | --- | 
| 0   | 1   | a   |  
| 1   | 2   | b   |  
| 2   | 3   | c   |    

### loc, iloc
* loc : 인덱싱을 문자로 하는것
* iloc  : 인덱싱을 정수로 하는것
``` python
df.iloc[0][0] # 앞은 행, 뒤는 열이다.
df.iloc[0, 0] # 콤마로도 표현 가능하다.

df.loc[0, "datetime"] # 0번째 행의 datetime
# -> '2011-01-01 00:00:00'

```

<br>

슬라이싱
``` python
# iloc
df.iloc[0:3, 0] # 3번째 행까지 출력
df.iloc[0:3, 0:3] # 3번째 행, 3번째 열까지 출력(2차원이 된다.)
df.iloc[[0, 100, 1000], 0:3] # 가져오고싶은 필드를 명시할수 있다.

# loc
df.loc[[0, 100, 100], "datetime":"temp"] # 0, 100, 10000번째 행을 datetime부터 temp까지 슬라이싱
```
``` python
# 시즌별로 캐주얼의 평균을 내고싶을때?
d = df.iloc[:, [1, 9]].groupby("season").mean()
d
```
||casual|
|---|---|
|season||
|---|---|
|1|15.489576|
|2|47.446762|
|3|52.220271|
|4|28.580834|


``` python
# 전체 행 중, casual열만. sum, min, max 이름을 써서 함수를 전달
d = df.loc[:, "casual"].agg(["sum", "min", "max"])
d

# -> 
# sum 392135 
# min 0 
# max 367 
# Name: casual, dtype: int64
```

<br>

set
``` python
# 데이터프레임의 시즌이 1인것만 중복을 제거해서 출력

df_sub = df[df.season == 1]
set(df_sub.season)

# ->
# {1}
```

<br>

데이터프레임의 연산

``` python
# 비트연산, season이 1이고, holiday가 1인 값 출력
df_sub = df[(df.season == 1) & (df.holiday == 1)]
df_sub
```
||datetime|season|holiday|workingday|weather|temp|atemp|humidity|windspeed|casual|registered|count|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|372|2011-01-17 00:00:00|1|1.0|0|2|8.20|9.850|47|15.0013|1|16|17.0|
|373|2011-01-17 01:00:00|1|1.0|0|2|8.20|9.850|44|12.9980|1|15|16.0|
|374|2011-01-17 02:00:00|1|1.0|0|2|7.38|8.335|43|16.9979|0|8|8.0|
|375|2011-01-17 03:00:00|1|1.0|0|2|7.38|9.090|43|12.9980|0|2|2.0|
|376|2011-01-17 04:00:00|1|1.0|0|2|7.38|9.850|43|8.9981|1|2|3.0|
|...|...|...|...|...|...|...|...|...|...|...|...|...|
|5799|2012-01-16 19:00:00|1|1.0|0|1|10.66|12.120|56|19.0012|10|134|144.0|
|5800|2012-01-16 20:00:00|1|1.0|0|1|10.66|12.120|60|19.0012|2|88|90.0|
|5801|2012-01-16 21:00:00|1|1.0|0|1|11.48|12.880|52|22.0028|3|46|49.0|
|5802|2012-01-16 22:00:00|1|1.0|0|2|12.30|13.635|49|23.9994|4|39|43.0|
|5803|2012-01-16 23:00:00|1|1.0|0|3|10.66|11.365|70|19.9995|0|28|28.0|

<br>

### 실습 
* casual 값이 10이상인 데이터의 season 별 registered의 합계 구해보기
``` python
# 오답
# casual이 10이상인 데이터를 season별로 구해서 registered를 따로 뽑아내고 합계를 구했다.
# 1차원 데이터가 됨.
df_1 = df.loc[df.casual >= 10].groupby("season")["registered"].sum()
df_1

# -> 
# season 
# 1 170649 
# 2 434124 
# 3 476165 
# 4 393582 
# Name: registered, dtype: int64

df_2 = df[df.casual >= 10].loc[:, ["season", "registered"]].groupby("season").sum()
df_2
```
||registered|
|---|---|
|season||
|---|---|
|1|170649|
|2|434124|
|3|476165|
|4|393582|

<br>

### 결측치 채우기
``` python
# NaN을 1로 채운다.
df.fillna(1)

# count의 평균을 구한다. NaN은 1로 채운다.
df.fillna(df["count"].mean())

# NaN값을 없앰
df.dropna()
```

``` python
# 99%에 해당하는 값보다 작은 casual값(1%)를 날린다.

df_sub = df.loc[df["casual"] < df["casual"].quantile(0.99)]
len(df_sub)

# -> 10777, 총 10886row가 있었다.

# casual을 출력
df_sub = df.loc[df["casual"] < df["casual"].quantile(0.99), ["casual"]]
```

<br>

### 실습
1. song, singer 실습에 사용한 데이터 출력하기
``` python
import pymysql

# DB
db = pymysql.connect(host="localhost", port=3306, user="root", password="jen401018&", db="sba")
cursor = db.cursor()

sql = """
select a.name, a.follower, b.title, b.album
from singer a, song b
where a.id = b.singer_id;
"""

# 가수명, 팔로워수, 노래 제목, 앨범 명
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)

db.close()
```
``` text
('허각', '8.4만', '물론', '물론')
('Agust D', '4731만', '사람 Pt.2 (feat. 아이유)', 'D-DAY')
('Paul Blanco', '11.2만', 'Summer (Feat. BE’O (비오))', 'Summer')
('부석순 (SEVENTEEN)', None, '파이팅 해야지 (Feat. 이영지)', '부석순 1st Single Album "SECOND WIND"')
('임한별', '14.5만', '사랑하지 않아서 그랬어', '사랑하지 않아서 그랬어')
('오마이걸 (OH MY GIRL)', None, '여름이 들려 (Summer Comes)', 'Golden Hourglass')
('성시경', None, '너의 모든 순간', '별에서 온 그대 OST Part.7')
('NCT DREAM', '1289만', 'Candy', 'Candy - Winter Special Mini Album')
('NCT DREAM', '1289만', 'ISTJ', 'ISTJ - The 3rd Album')
('NCT DREAM', '1289만', 'Broken Melodies', 'ISTJ - The 3rd Album')
('NCT DREAM', '1289만', '파랑 (Blue Wave)', 'ISTJ - The 3rd Album')
('NCT DREAM', '1289만', 'Like We Just Met', 'ISTJ - The 3rd Album')
('NCT DREAM', '1289만', 'Yogurt Shake', 'ISTJ - The 3rd Album')
('NCT DREAM', '1289만', 'Poison (모래성)', 'ISTJ - The 3rd Album')
('NCT DREAM', '1289만', 'Skateboard', 'ISTJ - The 3rd Album')
('NCT DREAM', '1289만', 'SOS', 'ISTJ - The 3rd Album')
('NCT DREAM', '1289만', 'Pretzel (♡)', 'ISTJ - The 3rd Album')
('방탄소년단', None, 'Dynamite', 'Dynamite (DayTime Version)')
('방탄소년단', None, 'Butter', 'Butter')
('방탄소년단', None, '봄날', 'YOU NEVER WALK ALONE')
('방탄소년단', None, 'Permission to Dance', 'Butter / Permission to Dance')
('방탄소년단', None, 'Take Two', 'Take Two')
('방탄소년단', None, 'The Planet', 'The Planet')
('IVE (아이브)', '396.4만', 'I AM', 'I"ve IVE')
('IVE (아이브)', '396.4만', 'Kitsch', 'I"ve IVE')
('IVE (아이브)', '396.4만', 'After LIKE', 'After LIKE')
('IVE (아이브)', '396.4만', 'LOVE DIVE', 'LOVE DIVE')
('Lauv', '192.9만', 'Steal The Show (From “엘리멘탈”)', 'Steal The Show (From “엘리멘탈”)')
('탑현', None, '나에게 그대만이', '나에게 그대만이')
('j-hope, J. Cole', None, 'on the street (with J. Cole)', 'on the street (with J. Cole)')
('#안녕', None, '해요 (2022)', '해요 (2022)')
('imase', '54.7만', 'NIGHT DANCER', 'NIGHT DANCER')
('임재현', None, 'Heaven(2023)', '시작은 첫키스 OST Part.1')
('LE SSERAFIM (르세라핌)', None, '이브, 프시케 그리고 푸른 수염의 아내', 'UNFORGIVEN')
('LE SSERAFIM (르세라핌)', None, 'UNFORGIVEN (feat. Nile Rodgers)', 'UNFORGIVEN')
('LE SSERAFIM (르세라핌)', None, 'ANTIFRAGILE', 'ANTIFRAGILE')
('멜로망스', '12.8만', '사랑인가 봐', '사랑인가 봐 (사내맞선 OST 스페셜 트랙)')
('케이시 (Kassy)', '9.9만', '사실말야내가말야그게그러니까말이야', '사실말야내가말야그게그러니까말이야')
('NewJeans', '886.2만', 'Super Shy', 'NewJeans 2nd EP "Get Up"')
('NewJeans', '886.2만', 'ETA', 'NewJeans 2nd EP "Get Up"')
('NewJeans', '886.2만', 'New Jeans', 'NewJeans 2nd EP "Get Up"')
('NewJeans', '886.2만', 'Hype boy', 'NewJeans 1st EP "New Jeans"')
('NewJeans', '886.2만', 'Ditto', 'NewJeans "OMG"')
('NewJeans', '886.2만', 'Attention', 'NewJeans 1st EP "New Jeans"')
('NewJeans', '886.2만', 'OMG', 'NewJeans "OMG"')
('NewJeans', '886.2만', 'Cool With You', 'NewJeans 2nd EP "Get Up"')
('NewJeans', '886.2만', 'ASAP', 'NewJeans 2nd EP "Get Up"')
('NewJeans', '886.2만', 'Get Up', 'NewJeans 2nd EP "Get Up"')
('H1-KEY (하이키)', None, '건물 사이에 피어난 장미 (Rose Blossom)', 'H1-KEY 1st Mini Album [Rose Blossom]')
('제이세라', '1.5만', '사랑의 바보', '사랑의 바보')
('STAYC(스테이씨)', '193.5만', 'Teddy Bear', 'Teddy Bear')
('(여자)아이들', '1122만', '퀸카 (Queencard)', 'I feel')
('(여자)아이들', '1122만', 'Allergy', 'I feel')
('(여자)아이들', '1122만', 'TOMBOY', 'I NEVER DIE')
('(여자)아이들', '1122만', 'Nxde', 'I love')
('ZEROBASEONE (제로베이스원)', None, 'In Bloom', 'YOUTH IN THE SHADE')
('경서예지, 전건호', None, '다정히 내 이름을 부르면', '다정히 내 이름을 부르면 (경서예지 x 전건호)')
('임영웅', '38.7만', '사랑은 늘 도망가', '신사와 아가씨 OST Part.2')
('임영웅', '38.7만', '모래 알갱이', '모래 알갱이')
('임영웅', '38.7만', '우리들의 블루스', 'IM HERO')
('임영웅', '38.7만', '다시 만날 수 있을까', 'IM HERO')
('임영웅', '38.7만', '무지개', 'IM HERO')
('임영웅', '38.7만', '이제 나만 믿어요', '내일은 미스터트롯 우승자 특전곡')
('임영웅', '38.7만', 'London Boy', 'Polaroid')
('임영웅', '38.7만', 'Polaroid', 'Polaroid')
('임영웅', '38.7만', '아버지', 'IM HERO')
('임영웅', '38.7만', '인생찬가', 'IM HERO')
('임영웅', '38.7만', 'A bientot', 'IM HERO')
('임영웅', '38.7만', '손이 참 곱던 그대', 'IM HERO')
('임영웅', '38.7만', '사랑해 진짜', 'IM HERO')
('임영웅', '38.7만', '연애편지', 'IM HERO')
('임영웅', '38.7만', '보금자리', 'IM HERO')
('김민석 (멜로망스)', '33.2만', '취중고백', '취중고백')
('이채연', '247.1만', 'KNOCK', 'Over The Moon')
('테이', '6.7만', 'Monologue', 'Monologue')
('로이킴', '34.1만', '잘 지내자, 우리 (여름날 우리 X 로이킴)', '잘 지내자, 우리 (여름날 우리 X 로이킴)')
('박재정', '13만', '헤어지자 말해요', '1집 Alone')
('Charlie Puth', '1764만', 'I Don"t Think That I Like Her', 'CHARLIE')
('Charlie Puth', '1764만', 'Dangerously', 'Nine Track Mind (Deluxe Edition)')
('Charlie Puth', '1764만', 'That"s Hilarious', 'CHARLIE')
('Charlie Puth', '1764만', 'That’s Not How This Works (feat. Dan + Shay)', 'That’s Not How This Works (feat. Dan + Shay)')
('지수 (JISOO)', '7495만', '꽃', 'ME')
('정국', None, 'Seven (feat. Latto) - Clean Ver.', 'Seven (feat. Latto) - Clean Ver.')
('정국', None, 'Still With You', 'Still With You')
('지민', '5088만', 'Like Crazy', 'FACE')
('정국, 방탄소년단', None, 'Dreamers [Music from the FIFA World Cup Qatar 2022 Official Soundtrack] (Feat. FIFA Sound)', 'Dreamers [Music from the FIFA World Cup Qatar 2022 Official Soundtrack]')
('DK(디셈버)', '2.3만', '심(心)', '심(心)')
('세븐틴 (SEVENTEEN)', None, '손오공', 'SEVENTEEN 10th Mini Album ‘FML"')
('The Kid LAROI, Justin Bieber', None, 'STAY', 'Stay')
('이무진', '26.7만', '잠깐 시간 될까', '잠깐 시간 될까')
('지아', '203만', '사랑..그게 뭔데', '사랑..그게 뭔데')
('김호중', '10.3만', '그중에 그대를 만나', '삼남매가 용감하게 OST Part.1')
('EXO', '1074만', 'Cream Soda', 'EXIST - The 7th Album')
('윤하 (YOUNHA)', '30.2만', '사건의 지평선', 'YOUNHA 6th Album Repackage "END THEORY : Final Edition"')
('우디 (Woody)', None, '사막에서 꽃을 피우듯', '사막에서 꽃을 피우듯')
('aespa', '30.2만', 'Spicy', 'MY WORLD - The 3rd Mini Album')
('aespa', '30.2만', 'Thirsty', 'MY WORLD - The 3rd Mini Album')
('던 (DAWN)', None, '빛이 나는 너에게', '빛이 나는 너에게')
('FIFTY FIFTY', '84.9만', 'Cupid', 'The Beginning: Cupid')
('경서', None, '첫 키스에 내 심장은 120BPM', 'ONGOING')
```

2. 가져온 데이터 데이터프레임에 넣어보기
``` python
import pymysql
import pandas as pd

# DB
db = pymysql.connect(host="localhost", port=3306, user="root", password="jen401018&", db="sba")
cursor = db.cursor()

sql = """
select a.name, a.follower, b.title, b.album
from singer a, song b
where a.id = b.singer_id;
"""

# 가수명, 팔로워수, 노래 제목, 앨범 명
cursor.execute(sql)
rows = cursor.fetchall()
# 데이터프레임에 넣기
df = pd.DataFrame(rows)
df.columns = ["name", "followers", "title", "album"]

db.close()
df
```
|name|followers|title|album|
|---|---|---|---|
|0|허각|8.4만|물론|물론|
|1|Agust D|4731만|사람 Pt.2 (feat. 아이유)|D-DAY|
|2|Paul Blanco|11.2만|Summer (Feat. BE’O (비오))|Summer|
|3|부석순 (SEVENTEEN)|None|파이팅 해야지 (Feat. 이영지)|부석순 1st Single Album "SECOND WIND"|
|4|임한별|14.5만|사랑하지 않아서 그랬어|사랑하지 않아서 그랬어|
|...|...|...|...|...|
|95|aespa|30.2만|Spicy|MY WORLD - The 3rd Mini Album|
|96|aespa|30.2만|Thirsty|MY WORLD - The 3rd Mini Album|
|97|던 (DAWN)|None|빛이 나는 너에게|빛이 나는 너에게|
|98|FIFTY FIFTY|84.9만|Cupid|The Beginning: Cupid|
|99|경서|None|첫 키스에 내 심장은 120BPM|ONGOING|


3. 가수별로 top 100에 있는 곡의 수를 출력
``` python
import pymysql
import pandas as pd

# DB
db = pymysql.connect(host="localhost", port=3306, user="root", password="jen401018&", db="sba")
cursor = db.cursor()

sql = """
select a.name, a.follower, b.title, b.album
from singer a, song b
where a.id = b.singer_id;
"""

# 가수명, 팔로워수, 노래 제목, 앨범 명
cursor.execute(sql)
rows = cursor.fetchall()
# 데이터프레임에 넣기
df = pd.DataFrame(rows)
df.columns = ["name", "followers", "title", "album"]

# 가수별로(groupby) top 100에 있는 제목(title)의 수(count)를 출력
df_2 = df.loc[:, ["name", "title"]].groupby("name").count()

db.close()
df_2
```


4. 앨범별로 제목의 수를 내림차순으로 정렬해서 출력하고 엑셀로 저장하기
``` python
import pymysql
import pandas as pd

# DB
db = pymysql.connect(host="localhost", port=3306, user="root", password="jen401018&", db="sba")
cursor = db.cursor()

sql = """
select a.name, a.follower, b.title, b.album
from singer a, song b
where a.id = b.singer_id;
"""

# 가수명, 팔로워수, 노래 제목, 앨범 명
cursor.execute(sql)
rows = cursor.fetchall()
# 데이터프레임에 넣기
df = pd.DataFrame(rows)
df.columns = ["name", "followers", "title", "album"]

# 가수별로(groupby) top 100에 있는 제목(title)의 수(count)를 출력
df_2 = df.loc[:, ["name", "title"]].groupby("name").count()

# 앨범별로 제목의 수를 내림차순으로 정렬해서 출력
df_3 = df.loc[:, ["album", "title"]].groupby("album").count().sort_values("title", ascending=False)
df_3.to_csv("result.csv")

db.close()
```


#### 참고
``` python
import numpy as np

np.zeros([5, 4]) #  0으로 채우기
# np.ones 1로 채우기
# 할당 표현식
#[1, 2, 3, 4, 5, ...100]
a = []
for i in range(100):
    a.append(i)

a = [i for i in range(100)]
print(a)
```