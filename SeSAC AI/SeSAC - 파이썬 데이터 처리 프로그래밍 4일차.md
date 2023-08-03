## SeSAC - 파이썬 데이터 처리 프로그래밍 4일차

2023.08.03

<br>

### 네이버 증권 TOP종목 Selenium을 사용해 가져오기

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
import requests
import time

# webdriver 경로 찾기
path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver"
service = Service(executable_path=path)
d = webdriver.Chrome(service=service)

wb = Workbook()
ws = wb.active

try:
    d.get("https://finance.naver.com/")
    elem = d.find_elements(By.CSS_SELECTOR, "#_topItems1 > tr")

    for e in elem:
        name = e.find_element(By.CSS_SELECTOR, "a").text
        tds = e.find_elements(By.CSS_SELECTOR, "td") # tr 안의 td를 담아둔다.
        price = tds[0].text.strip() # 주가
        diff = tds[1].text.replace("\n", "").strip() # 등락
        diff_per = tds[2].text.strip() # 등락율 

        # 상승, 하락 화살표 
        if diff[0] == "상":
            diff ='\u25B2'+diff[2:]
        else:
            diff ='\u25BC'+diff[2:]
    
        ws.append([name, price, diff, diff_per])
        
except Exception as e:
    print(e)
    
finally:
    d.close()
    d.quit()
    wb.save("stock.xlsx")
```


<br>

### 인스타그램 정보 가져오기

- 주의할점

인스타그램은 리액트로 개발되어 클래스가 매우 난잡하게 생성이 되어있다. 예를 들어 인스타그램의 검색 버튼을 확인해보면 이름이 랜덤으로 생성되어있고

![](https://i.imgur.com/oXLOQDL.png)

div가 겹겹으로 감싸져 있는것을 확인할 수 있다.
![](https://i.imgur.com/d3053xv.png)

여기서 인스타그램의 메뉴 아이콘을 쉽게 찾으려면 아래와 같은 접근법이 필요하다.

1. svg는 우리가 사용해야할 태그가 아니다. 하지만 이 태그를 통해 원하는 버튼을 찾을 수 있다.

![](https://i.imgur.com/L3ILxMw.png)


2. 정확한 클래스를 찾기보다 '검색'이라면 검색 버튼을 클릭한다는 생각으로 접근해야한다.

* svg를 클릭해서 태그의 위치를 파악한다.
* svg를 감싸고 있는 div의 가장 마지막 클래스명(여기서는 xvy4d1p)을 사용한다.

![](https://i.imgur.com/WimWsaQ.png)

``` python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains # 추가
import requests
import time

options = webdriver.ChromeOptions()
# window
# options.add_argument("--user-data-dir=C:\\Users\\sopung/\\Desktop\\MyChrome")
# mac
options.add_argument("--user-data-dir=/Users/sopung/Desktop/MyChrome")

# webdriver 경로 찾기
path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver"
service = Service(executable_path=path)
d = webdriver.Chrome(service=service, options=options) # options 추가

try:
    d.get("https://www.instagram.com/")
    # input() input으로 입력받고 홈페이지 로그인, 로그인 정보 저장 후에는 주석처리

    time.sleep(2)

	# 검색 버튼
	# 버튼 클래스의 가장 마지막 값을 가져옴
    buttons = d.find_elements(By.CSS_SELECTOR, ".xvy4d1p")
    # 버튼 리스트의 3번째(0, 1, '2', 3 ...)가 검색버튼 
    search_button = buttons[2] # 키 전달

    # action chain
    ac = ActionChains(d)
    ac.move_to_element(search_button)
    ac.click()
    ac.pause(1)
    ac.perform() # 반드시 perform을 해야한다.

    time.sleep(1)

	# 검색하기
	# 검색창 클래스의 가장 마지막 값을 가져옴 
    elem = d.find_element(By.CSS_SELECTOR, ".x7xwk5j")
    ac.reset_actions()
    ac.move_to_element(elem)
    ac.click()
    ac.send_keys("#파이썬")

    ac.pause(3)
    ac.move_by_offset(0, 100) # x좌표, y좌표
    # ac.context_click(마우스 우클릭) 을 통해 좌표값이 대략 어느정도 움직이는지 확인 가능하다.
    ac.click()
    ac.perform()
    
    # 파이썬 검색어 클릭 후 조회 대기시간
    time.sleep(5)

    # 검색된 포스트가 담긴 리스트
    posts = d.find_elements(By.CSS_SELECTOR, "._aabd")
    for post in posts:
        # 포스트를 클릭
        ac = ActionChains(d)
        ac.click(post)
        ac.pause(0.5)
        ac.perform()

        content = d.find_element(By.CSS_SELECTOR, "._a9zs > ._aade")
        print(content.text)

        ac.reset_actions()
        # 클릭한 포스트를 빠져나가기 위해 esc버튼 클릭 
        ac.send_keys(Keys.ESCAPE)
        ac.pause(0.5)
        ac.perform()
        # break # 게시글을 하나만 클릭하기 위해 break

    time.sleep(5)
    
    
except Exception as e:
    print(e)
    
finally:
    d.close()
    d.quit()

```

<br>

### 실습 - 인스타그램 정보 가져와서 엑셀에 저장하기
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook
import requests
import time

# workbook
wb = Workbook()
ws = wb.active

# webdriver options
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/Users/sopung/Desktop/MyChrome")
options.add_argument("--headless")
# 켜지는 윈도우 사이즈 
options.add_argument("--window-size=1920,1080")


# webdriver path
path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver"
service = Service(executable_path=path)
d = webdriver.Chrome(service=service, options=options)

try:
    # 정보를 가져올 페이지
    d.get("https://www.instagram.com/")
    # 페이지가 뜨는지 확인
    # time.sleep(3)

    # 1. 검색 버튼 누르기
    # 버튼을 감싸는 div의 마지막 클래스명을 통해 버튼 요소들을 담는다. 
    buttons = d.find_elements(By.CSS_SELECTOR, ".xvy4d1p")
    # print(len(buttons)) # buttons 리스트의 길이는 10
    # buttons의 3번째 요소(검색버튼)을 search_btn에 저장
    search_btn = buttons[2]

    # action chains, 행동을 수행한 후 리셋 시켜줘야한다.
    ac = ActionChains(d)
    ac.move_to_element(search_btn).click() # search_btn으로 이동 후 클릭
    # ac.click # 버튼을 클릭
    ac.pause(0.5)
    ac.perform() # 클릭을 수행

    time.sleep(0.3)

    # 2. 검색창에서 검색하기
    # 검색창을 감싸는 div의 마지막 클래스명을 통해 검색창 요소를 저장한다.
    elem = d.find_element(By.CSS_SELECTOR, ".x7xwk5j")
    ac.reset_actions() # 행동을 초기화 시켜준다.
    ac.move_to_element(elem).click()
    ac.send_keys("#문래동맛집추천")
    ac.pause(1)
    ac.send_keys(Keys.TAB, Keys.TAB, Keys.ENTER).perform() # 탭 두번, 엔터키

	# 검색이 오래걸리기 때문에 10초를 줌
    time.sleep(10)

	# 3. 포스트 열기
	# 포스트를 감싸는 div의 공통된 클래스명을 통해 게시글 요소들을 저장한다.
    posts = d.find_elements(By.CSS_SELECTOR, "._aabd")    
    # 게시글 요소 리스트를 순회
    for post in posts:
        ac = ActionChains(d) # 초기화
        ac.click(post) # 게시글을 클릭
        ac.pause(0.5)
        ac.perform()

		# 4. 컨텐츠 내용 가져오기
        content = d.find_element(By.CSS_SELECTOR, "._a9zs > ._aade").text
        # 5. 컨텐츠 내용을 workbook에 삽입
        ws.append([content])
        # print(content)

		# 초기화
        ac.reset_actions()
        ac.send_keys(Keys.ESCAPE).perform() # esc버튼 클릭
        ac.pause(0.5)
        
    time.sleep(10)
    
except Exception as e:
    print(e)
finally:
    d.close()
    d.quit()
    # 6. 엑셀로 저장
	wb.save("insta.xlsx")
```

<br>

### 실습 

``` text
1. singer 테이블 만들기
    
    - id(Auto increment)
        
    - name(가수이름)
        
    - follower(팔로우 수)
        
2. song 테이블 만들기
    
    - id(Auto increment)
        
    - singer_id(FK)
        
    - title(제목)
        
    - album(앨범)
        
3. 멜론 TOP 100을 수집
    
    - 멜론 TOP 100에 존재하는 가수들을 singer 테이블에 저장
        
        - top100내의 가수목록을 selenium 등으로 수집해서 singer에 넣기
            
        - 가수의 중복을 없애야한다
            
    
    - 각 가수들의 곡은 song 테이블에 저장
        
    - 단, singer 테이블에 follower는 0으로 저장
        
4. 인스타그램에서 가수명으로 검색한 후 인증마크 달려있는 계정의 follower가져와서 데이터베이스의 follower 값 업데이트
    
5. pandas
```

<br>

1. singer 테이블에 가수 목록 중복제거해서 넣기
``` python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook
import pymysql
import requests
import time

# INSERT INTO 테이블2 (singer_id, song, title)
# SELECT id, '노래명', '제목' -- 
# FROM 테이블1;

# DB
db = pymysql.connect(host="localhost", port=3306, user="root", password="jen401018&", db="sba")
cursor = db.cursor()

# webdriver options
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/Users/sopung/Desktop/MyChrome")

# path
path = "/Users/sopung/Downloads/chromedriver_mac_arm64/chromedriver"
service = Service(executable_path=path)
d = webdriver.Chrome(service=service, options=options)

try:
    # 멜론 차트 top100
    d.get("https://www.melon.com/chart/index.htm")

    # 차트 top100영역
    area = d.find_element(By.CSS_SELECTOR, ".service_list_song")
    elem = area.find_elements(By.CSS_SELECTOR, "tbody > tr")
    singer_list = []

    # 가수 목록
    for e in elem:
        singer_list.append(e.find_element(By.CSS_SELECTOR, ".ellipsis.rank02").text.strip())
        title = e.find_element(By.CSS_SELECTOR, ".ellipsis.rank01").text.strip()
        album = e.find_element(By.CSS_SELECTOR, ".ellipsis.rank03").text.strip()
        # print(album)
        # print(title)
    # 가수 중복 제거
    singer_list = list(set(singer_list))

    # 리스트에서 가수를 SQL로 담아 DB에 삽입
    for singer in singer_list:        
        sql = f"""
            insert into singer
            values(NULL, '{singer}', NULL)
        """
        cursor.execute(sql)
except Exception as e:
    print(e)

finally:
    d.close()
    d.quit()
    db.commit()
    db.close()

```

