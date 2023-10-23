
1. SeSAC의 소개글, 교육과정을 크롤링, 이외에도 새싹 후기 데이터등을 크롤링
``` python
# 새싹 소개글
import requests
import bs4
import re

def get_data(url):
    response = requests.get(url)
    data = response.text
    return data

def get_intro(url):
    # 소개글 가져오기
    data_intro = get_data(url)
    # BeautifulSoup 객체 생성
    soup = bs4.BeautifulSoup(data_intro, "html.parser")
    # 원하는 부분만 추출
    text = soup.find("div", class_="ssac_intro").text
    # 불필요한 정보 제거
    text = re.sub(r"<[^>]*>", "", text)
    text = text.split("\n")

    # 내용을 따로 담기
    contents = []
    for line in text:
        if line != "":
            contents.append(line.rstrip("\r\t").replace("\t", " "))

    # 저장
    with open("새싹_소개글.txt", "w") as f:
        for content in contents:
            f.write(content + "\n")

def main():
    # 소개글 가져오기
    get_intro("http://ssac.seoul.kr/common/menu/html/900006001001/detail.do;jsessionid=F0E2081B0601681A90555BA0F28ACFD1")

if __name__ == "__main__":
    main()
```


``` python
# 교육과정
import requests
from bs4 import BeautifulSoup

url = "http://ssac.seoul.kr/course/active/offline001/list.do"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# edu_on_li 클래스를 가진 ul 태그에서 정보를 가져옴
course_infos = []
for lis in soup.find_all("ul", class_="edu_on_li"):
    # `lis` 변수를 `li` 태그를 포함하는 리스트로 변환
    lis = lis.find_all("li")
    for li_tag in lis:
        # div class="ct on" 태그에서 정보를 가져옴
        inner_tag = li_tag.find("div", class_="inner")

        # `inner_tag` 변수가 `None` 객체인지 확인
        if inner_tag is not None:
            # `inner_tag` 변수가 `None` 객체가 아니면 학습대상, 신청기간, 교육기간, 과정목표를 추출.
            target_info = inner_tag.find("ul", class_="info").text.replace("\n", "")
            course_name = inner_tag.find("p", class_="title").text

            # 딕셔너리를 리스트에 추가
            course_infos.append([course_name, target_info])

print(course_infos)

# 리스트를 txt 파일로 저장
with open("새싹_교육과정.txt", "w") as f:
    for course_info in course_infos:
        f.write("과정명: {}\n학습대상: {}\n".format(course_info[0], course_info[1]))
```


2. KoGPT2와 수집한 후기 데이터를 이용해 주요 문장 생성, GPT를 인컨텍스트러닝하여 가사 생성
``` 
새싹아, 생일 축하해
xx번째 생일을 맞이하여
서울시의 청년들을 위해
SW 개발자로 키워주니

(후렴)
새싹아, 새싹아
항상 푸르게 자라나
청년들의 꿈을 이루게
힘을 주렴

단순한 교육이 아닌
실제 일자리까지 연계해
청년들의 취업 경쟁력을 높이고
SW 산업 발전에 기여해

(후렴)
새싹아, 새싹아
항상 푸르게 자라나
청년들의 꿈을 이루게
힘을 주렴

새싹아, 앞으로도
서울시 청년들의 꿈을 위해
끊임없이 노력하며
더욱 발전해나가길 바라

(후렴)
새싹아, 새싹아
항상 푸르게 자라나
청년들의 꿈을 이루게
힘을 주렴
```
``` 
(Verse 1)
AI 기술을 활용한
새로운 직업군
AI활용 프롬프트 엔지니어
꿈을 이루는 디딤돌이 되네

(Chorus)
새싹, 새싹, 청년들의 꿈을 키워
새싹, 새싹, 미래를 향한 도전을 응원해

(Verse 2)
만 15세 이상 서울시 거주 구직자
누구나 꿈을 이룰 수 있어
새싹과 함께라면

(Chorus)
새싹, 새싹, 청년들의 꿈을 키워
새싹, 새싹, 미래를 향한 도전을 응원해

(Bridge)
120시간의 집중 교육
온라인으로 진행
새싹이 함께하니
꿈은 더 가까워져

(Chorus)
새싹, 새싹, 청년들의 꿈을 키워
새싹, 새싹, 미래를 향한 도전을 응원해
```
``` 
(Verse 1) 
서울시가 운영하는 청년취업사관학교 
AI, 데이터 사이언스, 웹/앱 개발 
다양한 분야의 교육과정을 제공해 
구직자를 위한 꿈의 디딤돌이 되네 

(Chorus) 
새싹, 새싹, 청년들의 꿈을 키워 
새싹, 새싹, 미래를 향한 도전을 응원해 

(Verse 2) 
보도자료를 통해 
새로운 소식을 전해 
청년들의 취업과 일자리 창출 
새싹이 앞장서서 노력해 

(Chorus) 
새싹, 새싹, 청년들의 꿈을 키워 
새싹, 새싹, 미래를 향한 도전을 응원해
```


3. 이외에도 팀원들이 수집한 정보를 기반으로 가사를 생성하여 취합, 적절한 가사를 작사
``` 
(Instrumental Intro) 

(Verse 1)

넌 우리의 희망, 새싹이란 이름
3주년 너의 생일, 특별한 순간
서울의 빛나는 청년들의 꿈, 이곳에서
우리 모두 멋지게 성장하리라 믿어

머리 위에 떠오르는 별처럼
빛나는 미래로 가득 차서
열정과 열망, 우리 함께
하늘 높이 날아가자, 함께

(Verse 2) 

넌 우리의 꿈, 새싹이란 이름
3주년을 맞은 너의 특별한 날 
서울의 빛나는 청년들의 희망, 이곳에서 
우리 함께 더 나아가길 믿어

(Chorus 1)

새싹아
항상 푸르게 자라나
청년들의 꿈을 이루게
힘을 줘

(Chorus 2)

새싹아
항상 푸르게 자라나
청춘들의 꿈을 이뤄갈
힘을 줘



(Verse 3)

Education and jobs, hand in hand we'll stride
교육과 취업, 손에 손을 잡고 우린 나아가

Into the world of Software, doors open wide
소프트웨어의 세계로, 문이 넓게 열려 있어

Illuminating young dreams with a hopeful glow
젊은 꿈들을 희망의 빛으로 비추며

Together we'll walk the path where our hopes flow
우리 함께 희망이 흐르는 길을 걸어갈 거야

(Pre-outro)

Challenges and passions fuel our way
도전과 열정이 우리의 길을 이끌어

Onward on the journey, no end in our sight
우리의 여정은 계속돼, 끝이 보이지 않아

(Outro)

Shaping Seoul's future, hand in hand we'll create
서울의 미래를, 우리 손에 손을 잡고 만들어 갈 거야

Embarking on the journey to our dreams, so bright
밝게 빛나는 우리 꿈을 향한 여정을 떠나게 될 거야.

(Instrumental Outro)
```

4. 작곡된 가사를 사용하여 멜로디 생성(suno AI)하고 편집(PowerDirector 365)
![](SOURCE_SeSAC%203rd%20Anniversary%20Song.mp3)


5. 완성된 곡의 앨범 커버 편집, 가사 정보 삽입 및 동영상 제작
![](새싹_3주년_노래.mp4)

#### 시행착오
* 처음에 멜론 차트를 기반으로 가사 트렌드를 수집하고 분석해서 문장을 생성했으나, 차트에 한이 많았는지 생일축하가 아닌 생이별 노래같은 가사가 생성되었다.
* KoGPT2가 생성한 가사가 매끄럽지 않아서 가사의 이해가 힘들었다.
* 작곡된 멜로디를 매끄럽게 연결하는 과정이 stable diffusion만큼이나 많이 걸렸다. 부르는 가수 자체가 달라지거나, 음악의 플롯이 이전과 너무 맞지 않거나, 부르는 음이 어색한 경우가 많았다. 

(딴딴딴딴딴)넌 우↗️리↘️의➡️꿈
![](넌~%20우리으꿈~.mp3)
노래 안부르다가, 뒤에가서 급하게부르다가, 부를 시간 없으니까 얼버무려요
![](노래언제불러.mp3)
이런게 정말 많았다.

