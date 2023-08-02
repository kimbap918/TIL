## SeSAC - 파이썬 데이터 처리 프로그래밍 3일차

2023.08.02

<br>

### 공공데이터포털

가입 후 로그인
[공공데이터 포털](https://www.data.go.kr/)
<br>
1. 홈페이지 메뉴에서 데이터 찾기 → 데이터 목록에서 원하는 데이터 검색
![](https://i.imgur.com/sOeiO3B.png)

2. 상세 페이지에서 활용 신청하기
![](https://i.imgur.com/ORfvWWa.png)


3. 마이페이지 → 데이터 활용 → 인증키 발급현황에서 인증키 확인

![](https://i.imgur.com/KQZusL3.png)

<br>

### API
https://ko.wikipedia.org/wiki/API
<br>

### Fake API

[JSONPlaceholder - Free Fake REST API](https://jsonplaceholder.typicode.com/)

![](https://i.imgur.com/wdRcyqV.png)

GET, POST는 대상에 대한 행위이며,
주소에 해당하는 /posts 는 행위의 대상이다.

<br>

### HTTP의 주요 메서드

GET : 서버에게 리소스를 보내달라고 요청

POST : 서버에게 리소스를 보내면서 생성해달라고 요청

PUT : 서버에게 리소스의 업데이트를 하거나 리소스가 없다면 새로운 리소스를 생성해 달라고 요청, 회원정보 수정 등에 사용됨

PATCH : 서버에게 리소스의 업데이트를 요청, 회원정보 수정 등에 사용

DELETE : 서버에게 리소스의 삭제를 요청 

<br>

### HTTP의 상태 코드

[HTTP 상태 코드 - HTTP | MDN](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)

<br>

### 기상청 중기예보 조회서비스 openAPI 정보 사용해보기
https://www.data.go.kr/data/15059468/openapi.do

1. 해당 페이지 아래로 이동해서 샘플 코드 복사

```python
# Python3 샘플 코드 #

import requests

url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidFcst'
params ={'serviceKey' : '서비스키', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'stnId' : '108', 'tmFc' : '201310170600' }

response = requests.get(url, params=params)
print(response.content)
```

2. 마이페이지에서 인코딩 되지 않은 원본 인증키를 복사 후 serviceKey의 값 부분에 붙여넣기

![](https://i.imgur.com/VLzgpee.png)

3. Jupyter에서 샘플 코드를 수정 후 실행

```python
import requests 
from pprint import pprint # pretty print

url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidFcst'
params = {'serviceKey' : '', # 복사한 서비스 키가 들어가야함 
         'pageNo' : '1', 
         'numOfRows' : '10', 
         'dataType' : 'JSON', # JSON으로 변경
         'stnId' : '108', 
         'tmFc' : '202308020600' 
         }

response = requests.get(url, params=params)
data = response.json() # json 형태로 바꾼다.
pprint(data)
```

![](https://i.imgur.com/kjPxdPu.png)

4. json에서 텍스트만 출력해보기

```python
import requests 
from pprint import pprint

url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidFcst'
params = {'serviceKey' : '', # 복사한 서비스 키가 들어가야함 
         'pageNo' : '1', 
         'numOfRows' : '10', 
         'dataType' : 'JSON', 
         'stnId' : '108', 
         'tmFc' : '202308020600' 
         }

response = requests.get(url, params=params)
data = response.json()
for item in data["response"]["body"]["items"]["item"]:
    print(item["wfSv"])
```

```python
○ (강수) 5일(토) 제주도에 비가 오겠습니다.
○ (기온) 이번 예보기간 아침 기온은 23~27도, 낮 기온은 29~35도로 평년(최저기온 22~24도, 최고기온 29~33도)과 비슷하거나 조금 높겠습니다.
○ (해상) 당분간 서해남부해상과 남해상, 제주도해상에서 물결이 1.0~4.0m(제주도해상 5.0m 이상)로 매우 높게 일겠습니다.
○ (주말전망) 5일(토)과 6일(일)은 전국이 구름많겠으나, 제주도는 5일(토) 흐리고 비가 오겠습니다. 아침 기온은 25~27도, 낮 기온은 32~35도가 되겠습니다.

* 이번 예보기간 제6호 태풍(카눈)의 이동경로에 따라 강수구역과 시점이 변경될 가능성이 있으며, 내륙을 중심으로 소나기가 내릴 가능성이 있으니, 앞으로 발표되는 최신 예보를 참고하기 바랍니다.
```
<br>

### Selenium
- 동적 웹을 분석하기 위해 사용하는 도구

```python
!pip3 install selenium webdriver_manager
```

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
# release = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
# version = requests.get(release).text
path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver" # chromedriver 경로
service = Service(executable_path=path)
d = webdriver.Chrome(service=service)
try:
    d.get("https://naver.com")
except Exception as e: # 에러 발생시 실행
    print(e)
finally: # 에러가 나지 않아도 실행
    time.sleep(2)
    d.close()
    d.quit()
```
<br>

### 네이버 뉴스 웹 크롤링 해보기

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # 추가
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
# release = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
# version = requests.get(release).text
path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver" # chromedriver 경로
service = Service(executable_path=path)
d = webdriver.Chrome(service=service)
try:
    d.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105")
    # find_elements 여러개를 가져올때
		elem = d.find_element(By.CSS_SELECTOR, "#_rankingList0")
    print(elem.text)
except Exception as e:
    print(e)
finally:
    time.sleep(2)
    d.close()
    d.quit()
```

```
“세상 물정 너무 몰랐다” 독일 경제가 수렁에 빠진 3가지 …
조선일보
"호텔 뷔페 가자" 외쳤는데…4인가족 80만원에 아빠는 조 …
서울경제
방심위, '김건희 캄보디아 사진' 비판 TBS <김어준의 …
프레시안
해수욕장도 아닌데 '바글바글'…폭염에 인기 폭발한 곳
한국경제
“여장 남자, 딸 속이고 성폭행”…日 '머리 없는 시신' …
전자신문
```

링크가 있는 텍스트를 클릭해서 페이지의 내용을 가져올수도 있다.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # 추가
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
# release = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
# version = requests.get(release).text
path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver" # chromedriver 경로
service = Service(executable_path=path)
d = webdriver.Chrome(service=service)
try:
    d.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105")
    # elem = d.find_element(By.CSS_SELECTOR, "#_rankingList0")
    # titles = elem.find_elements(By.CSS_SELECTOR, ".list_tit")
    # for title in titles:
    #     print(title.text)

    time.sleep(0.5)
    
    section = d.find_element(By.CSS_SELECTOR, ".section_body")
    lis = section.find_elements(By.CSS_SELECTOR, "ul > li")
    for li in lis:
        print(li.text)

    page_area = d.find_element(By.CSS_SELECTOR, "#paging")
    page_2 = page_area.find_element(By.LINK_TEXT, "2") # 링크된 텍스트를 클릭해서 페이지를 넘어갈수도 있다.
    page_2.click()

    time.sleep(2)
    
    section = d.find_element(By.CSS_SELECTOR, ".section_body")
    lis = section.find_elements(By.CSS_SELECTOR, "ul > li")
    for li in lis:
        print(li.text)
        
except Exception as e:
    print(e)
finally:
    time.sleep(2)
    d.close()
    d.quit()
```
<br>

### 반복을 사용한 여러 페이지 크롤링

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # 추가
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver" # chromedriver 경로
service = Service(executable_path=path)
d = webdriver.Chrome(service=service)
try:
    d.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105")
    time.sleep(0.5)
        
    for i in range(2, 7):
        # 수집
        section = d.find_element(By.CSS_SELECTOR, ".section_body")
        lis = section.find_elements(By.CSS_SELECTOR, "ul > li")
        for li in lis:
            print(li.text)

        # 클릭
        page_area = d.find_element(By.CSS_SELECTOR, "#paging")
        page_2 = page_area.find_element(By.LINK_TEXT, str(i)) # 링크된 텍스트를 클릭해서 페이지를 넘어갈수도 있다.
        page_2.click()
    
        time.sleep(1)
            
except Exception as e:
    print(e)
finally:
    time.sleep(2)
    d.close()
    d.quit()
```
<br>

### 실습 - 멜론 차트 Selenium으로 수집하기
* 좋아요(like) 수집하고 콤마(,) 제거 후 int형으로 바꿀것

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
import pymysql
import requests
import time

# 4. DB
db = pymysql.connect(host="localhost", port=3306, user="root", password="jen401018&", db="sba")
cursor = db.cursor()

# 6. Workbook
wb = Workbook()
ws = wb.active

# 1. chromedriver
path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver" # chromedriver 경로
service = Service(executable_path=path)
d = webdriver.Chrome(service=service)

# 데이터 수집
try:
    d.get("https://www.melon.com/chart/index.htm")
    time.sleep(0.5)

	# 2. 수집할 영역 클래스
    area = d.find_element(By.CSS_SELECTOR, ".service_list_song")
    elem = area.find_elements(By.CSS_SELECTOR, "div > table > tbody > tr")

	# 3. 순위, 제목, 가수, 앨범, 변동, 좋아요
    for e in elem:
	    # 수집시 공백을 제거하기 위해 strip() 사용
        rank = e.find_element(By.CSS_SELECTOR, ".rank").text.strip()
        # sql 삽입 시 작은따옴표(') 오류를 해결하기 위해 큰 따옴표로 치환 
        # find_element 는 select_one과 같다.
        # find_elements 는 select와 같다.
        title = e.find_element(By.CSS_SELECTOR, ".ellipsis.rank01 > span > a").text.strip().replace("'", '"')
        singer = e.find_element(By.CSS_SELECTOR, ".ellipsis.rank02 > a").text.strip().replace("'", '"')
        album = e.find_element(By.CSS_SELECTOR, ".ellipsis.rank03 > a").text.strip().replace("'", '"')
        diff = e.find_element(By.CSS_SELECTOR, ".rank_wrap").text.strip().replace("'", '"')
        diff_icon = e.find_element(By.CSS_SELECTOR, ".rank_wrap")
        diff_icon = diff_icon.get_attribute('title')
        # 좋아요를 수집해서 쉼표 제거
        like = e.find_element(By.CSS_SELECTOR, ".cnt").text.strip().replace(",", "")
        
        if "순위 동일" in diff_icon:
            diff = "-"
        elif "단계 상승" in diff_icon:
            diff = "+" + diff
        elif "단계 하락" in diff_icon:
            diff =  "-" + diff
        else:
            diff = "new"

		# 5. SQL 삽입
        sql = f"""
        insert into melon
        values(NULL, {rank}, '{title}', '{singer}', '{album}', {like}, '{diff}')
        """
        cursor.execute(sql)

		# 7. workbook 삽입
        ws.append([rank, title, singer, album, like, diff])

except Exception as e:
    print(e)
    
finally:
    time.sleep(1)
    d.close()
    d.quit()
    # DB 커밋
    db.commit()
    db.close()
    # Excel 저장
    wb.save("melon2.xlsx")
```

<br>

### Selenium을 사용해서 검색하고 값 가져오기
``` python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys # 키보드의 특수키를 전달하기 위해 import
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

# chromedriver
path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver" # chromedriver 경로
service = Service(executable_path=path)
d = webdriver.Chrome(service=service)

try:
    d.get("https://cafe.naver.com/joonggonara")
    elem = d.find_element(By.CSS_SELECTOR, "#topLayerQueryInput")
    elem.send_keys("자전거") # 자전거를 검색창에 입력
    elem.send_keys(Keys.RETURN) # 엔터키(Return)

    time.sleep(2)

except Exception as e:
    print(e)
finally:
    d.close()
    d.quit()
```

<br>

검색 결과를 가져올때 클래스를 가져와도 아무것도 없다고 오류가 뜨기도 한다. 

![](https://i.imgur.com/f1iKvSO.png)
![](https://i.imgur.com/kUloXEV.png)
위의 사진처럼 a 태그의 article 클래스를 가져왔지만 `no such element` 오류가 뜬다.  이  때는 iframe태그가 있는지 확인해보자.

<br>

> iframe  :  Inline Frame, 웹 브라우저 내에 또 다른 프레임, 즉 현재 브라우저에 렌더링되고 있는 문서 안에 또 다른 HTML페이지를 삽입할 수 있도록 하는 기능

![](https://i.imgur.com/tzMGoGb.png)

``` python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys # 키보드의 특수키를 전달하기 위해 import
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

# chromedriver
path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver" # chromedriver 경로
service = Service(executable_path=path)
d = webdriver.Chrome(service=service)

try:
    d.get("https://cafe.naver.com/joonggonara")
    elem = d.find_element(By.CSS_SELECTOR, "#topLayerQueryInput")
    elem.send_keys("자전거") # 자전거를 검색창에 입력
    elem.send_keys(Keys.RETURN) # 엔터키(Return)

	# time.sleep(1)
	# 다른 웹사이트이기 때문에 느리게 로딩될 수 있어서 기다리는 함수

	# iframe
    iframe = d.find_element(By.CSS_SELECTOR, "#cafe_main")
    d.switch_to.frame(iframe) # iframe 안으로 이동 

	# 원본 웹으로 돌아오는 함수
	# d.switch_to.default_content()

	# iframe 안의 .article을 찾는다.
    article = d.find_element(By.CSS_SELECTOR, ".article")
    print(article.text)
    
    time.sleep(2)

except Exception as e:
    print(e)
finally:
    d.close()
    d.quit()
```

<br>

### 실습 - 중고나라 검색(제목, 작성자, 작성일)
* 입력한 값을 검색해서 엑셀에 삽입하기
``` python
# 1~5페이지까지 게시글 제목, 작성자, 작성일 
# 엑셀에 삽입하기

from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time


# 1. chromedriver의 경로
path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver"
service = Service(executable_path=path)
d = webdriver.Chrome(service=service)

# 7. Workbook
wb = Workbook()
ws = wb.active

try:
    # 2. 중고나라 검색창에서 검색
    d.get("https://cafe.naver.com/joonggonara")
    elem = d.find_element(By.CSS_SELECTOR, "#topLayerQueryInput")

	# 3. 입력한 값을 검색
    elem.send_keys(input())
    elem.send_keys(Keys.RETURN)
    
    time.sleep(1)

    # 4. iframe
    iframe = d.find_element(By.CSS_SELECTOR, "#cafe_main") # id가 cafe_main인 태그를 찾아 iframe에 저장
    d.switch_to.frame(iframe) # iframe으로 이동

	# 6. 페이징
    for i in range(1, 6):
        element = d.find_elements(By.CSS_SELECTOR, ".article-board.m-tcol-c > table > tbody > tr")

		# 5. 제목, 작성자, 날짜, 조회수 가져오기
        for e in element:
            title = e.find_element(By.CSS_SELECTOR, ".article").text.strip()
            nick = e.find_element(By.CSS_SELECTOR, ".p-nick").text.strip()
            date = e.find_element(By.CSS_SELECTOR, ".td_date").text.strip()
            view = e.find_element(By.CSS_SELECTOR, ".td_view").text.strip()

            # print("==========================", i)
            # print(title)
            # print(nick)
            # print(date)
            # print(view)
            ws.append([title, nick, date, view])
            
        page_area = d.find_element(By.CSS_SELECTOR, ".prev-next")
        page = page_area.find_element(By.LINK_TEXT, str(i))
        page.click()
        
        time.sleep(1)
    
except Exception as e:
    print(e)
finally:
    time.sleep(1)
    d.close()
    d.quit()
    # 8. 엑셀로 저장하기
    wb.save("jungo.xlsx")
```
