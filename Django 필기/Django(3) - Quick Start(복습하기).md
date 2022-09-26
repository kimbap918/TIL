#### Variable routing

* URL 주소를 변수로 사용하는 것을 의미
* URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음 
* 즉, 변수 갑셍 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음
* 사용자로 부터 변경되는 URL을 입력받아서 처리하는 방식

<br>

#### Sending and Retrieving form data

* 데이터를 보내고 가져오기
* HTML  form element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기
* 웹은 기본적으로 클라이언트-서버 아키텍처를 사용
* 클라이언트 측에서 HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법
* 이를 통해 사용자는 HTTP 요청에서 전달할 정보를 제공할 수 있다.

<br>

#### HTML `<form>` element

* 데이터가 전송되는 방법을 정의
* 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당

<br>

주소(누구에게) => https://search.naver.com

주문서(무엇을) => /search.naver

?query=아이유

https://search.naver.com/search.naver?

=> form의 action에 정의한 내용

query=아이유 

=> input으로 정의한 데이터

https://search.naver.com/search.naver?query=아이유

``` html
  <h1>Naver</h1>
  <form action="https://search.naver.com/search.naver">
    Naver 검색어: <input type="text" name="query">
     <input type="submit">
  </form>
```

<br>

#### Django Quick start

#### terminal

``` terminal
# 1. 프로젝트를 시작할 경로 이동
/Users/mac - (main) > cd desktop
mac/desktop - (main) > cd server
# 2. 폴더 생성
desktop/server - (main) > mkdir day3
desktop/server - (main) > ls
day3		example		ohjumae		server-venv
# 3. 생성한 폴더로 경로 이동
desktop/server - (main) > cd day3
server/day3 - (main) > ls
# 4. python -m venv [가상환경 이름]으로 가상환경 생성
server/day3 - (main) > python -m venv day3-venv
# 5. 가상환경 실행 
server/day3 - (main) > source day3-venv/bin/activate
(day3-venv) server/day3 - (main) > 
(day3-venv) server/day3 - (main) > pip list
Package    Version
---------- -------
pip        22.0.4
setuptools 58.1.0
WARNING: You are using pip version 22.0.4; however, version 22.2.2 is available.
You should consider upgrading via the 
# (선택 사항) python -m pip install --upgrade pip 명령어로 pip 업그레이드
'/Users/mac/Desktop/server/day3/day3-venv/bin/python -m pip install --upgrade pip' command.
(day3-venv) server/day3 - (main) > 
# 6. Django LTS버전 설치 
(day3-venv) server/day3 - (main) > pip install django==3.2.13
# 7. Django 프로젝트 폴더 생성 
(day3-venv) server/day3 - (main) > django-admin startproject day3pjt .
# 8. 애플리케이션 생성
(day3-venv) server/day3 - (main) > python manage.py startapp practices

```

<br>

#### settings

``` python
# settings.py
# Application definition

INSTALLED_APPS = [
    'practices',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

<br>

#### urls

``` python
# urls.py 
from django.contrib import admin
from django.urls import path
# import
from practices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
```

<br>

#### views

``` python
# views.py
from django.shortcuts import render

# Create your views here.

def index(request):
  	# 인자와 HTML파일을 담아 render에 리턴
    return render(request, 'index.html')
```

<br>

#### 템플릿 페이지 생성

practices 폴더 내에 templates 폴더를 생성 후 index.html 생성

``` html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>검색 모음</h1>
  <h2>Google</h2>
  <form action="https://www.google.com/search">
    <input type="text" name="q">
    <input type="submit">
  </form>
</body>
</html>
```

<br>

#### 서버 실행하기

``` terminal
# 서버 실행
(day3-venv) server/day3 - (main) > python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 26, 2022 - 01:38:02
Django version 3.2.13, using settings 'day3pjt.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

<br>

## 실습 해보기 - 핑퐁 페이지

/ping : form 태그 및 input 태그를 통해 사용자의 입력을 받아 pong이라는 페이지에 전달해 주는 기능 만들기

/pong : /ping으로부터 전달받은 데이터를 활용하여, ooo님 환영합니다. 페이지를 출력

#### ping 페이지 만들기

#### urls

``` python
from django.contrib import admin
from django.urls import path
from practices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index.urls),
  	# path에 ping 생성
    path('ping/', views.ping),
]
```

<br>

#### views

``` python
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ping(request):
    return render(request, 'ping.html')
```

<br>

#### templates 폴더 내 ping.html 생성

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Ping</h1>
  <!-- 아무것도 적지 않으면 method 는 자동으로 기본값을 GET으로 넣어줌. 
GET 방식은 어떤 데이터를 가져오기 위해서 보내는 데이터를 의미 -->
  <form action="/pong" method="GET">
    이름을 입력해주세요 : <input type="text" name="ball">
    <input type="submit">
  </form>
</body>
</html>
```

<br>

#### pong 페이지 만들기

#### urls

``` python
from django.contrib import admin
from django.urls import path
from practices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index.urls),
    path('ping/', views.ping),
    path('pong/', views.pong)
]
```

<br>

#### views

``` python
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ping(request):
    return render(request, 'ping.html')


def pong(request):
    # print(request)
    # print(dir(request))
    # print(request.Get.get('ball'))
    name = request.GET.get('ball')
    context = {
        'name' : name,
    }
    return render(request, 'pong.html', context)
  	# 위의 name과 context를 지우고 아래 코드로 1줄 처리 가능
  	# return render(request, 'pong.html', {'name': request.GET.get('ball')}) 
```

<br>

#### templates 폴더 내  pong.html

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Pong</h1>
  <p>{{ name }}님, 환영합니다.</p>
</body>
</html>
```

<br>

## 템플릿 상속

* 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
* **반드시 템플릿 최상단에 작성되어야 함(2개 이상 사용할 수 없음)**
* 하위 템플릿에서 재지장 할 수 있는 블록을 정의

<br>

#### base.html 생성

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <!-- CSS only -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  <!-- JavaScript Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
</head>
<body>
  {% block content %}
  {% endlblock content %}
</body>
</html>
```

<br>

index 템플릿에서 base템플릿을 상속받음

``` html
<!-- 최상단에 작성 -->
{% extends 'base.html %}

{% block content %}
<h1>검색 모음</h1>
<h2>Google</h2>
<form action="https://www.google.com/search">
  <input type="text" name="q">
  <input type="submit">
</form>
{% endblock %}
```

공통된 부분을 제외하고 block 과 endblock 사이에 개별적인 내용을 넣으면 템플릿 상속이 가능함

<br>

