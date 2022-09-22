#### Django 프로젝트 생성 및 실행하기

* asgi.py

  * Asynchronous Server Gateway Interface
  * Django 애플리케이션이 비동기식 웹 서버 와 연결 및 소통하는 것을 도움
  * 추후 배포시 사용하며 지금은 수정하지 않음

* setting.py

  * Django 프로젝트 설정을 관리

* urls.py

  * 사이트의 url과 적절한 views의 연결을 지정

* wigs.py

  * Web server Gateway Interface
  * Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
  * 추후 배포 시 사용하며 지금은 수정하지 않음

* manage.py

  * Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

    ``` terminal
    # manage.py Usage 
    $ python manage.py <command> [options]
    ```

<br>

#### Django Application

* 애플리케이션 생성

  ``` terminal
  $ python manage.py startapp articles
  ```

<br>

위의 명령어를 가상환경이 실행된 터미널에서 실행 완료시 articles 폴더가 생성되며, 폴더 안에는 아래와 같은 파일이 생성됨.

 * admin.py
   * 관리자용 페이지를 설정 하는 곳
 * apps.py
   * 앱의 정보가 작성된 곳
   * 별도로 추가 코드를 작성하지 않음
 * **views.py**
   * view 함수들이 정의 되는 곳
   * MTV 패턴의 V에 해당

<br>

## settings.py

* 프로젝트에서 앱을 사용하기 위해서는 반드시 settings.py 안의 INTALLED_APPS 리스트에 반드시 추가해야 함

* INSTALLED_APPS

  ``` python
  # Application definition
  
  INSTALLED_APPS = [
    	'articles', # 생성한 articles를 추가함
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

  <br>

* 생성한 앱을 삭제하고 싶은 경우 위의 settings.py 에 INSTALLED_APPS 내에 추가한 항목을 삭제하고, `$ python manage.py startapp [폴더명] ` 명령어로 생성된 폴더를 삭제

<br>

#### 요청과 응답

* URL -> VIEW -> TEMPLATE 순의 순서로 코드를 작성해보고 데이터의 흐름을 이해하기

<br>

#### URLs

``` python
from django.contrib import admin
from django.urls import path
from articles import views # articles 앱에 있는 views를 가져옴

urlpatterns = [
    path('admin/', admin.site.urls),
  	path('index/', views.index), # 마지막 요소에도 콤마를 붙혀야함(장고 한정)
  	path('welcome/<>/', welcome.index),
]
```

* articles 앱(폴더) 내에 views를 import 하고 urlpatterns 리스트 내에 작성할 페이지를 path 함수 내에 작성 

#### Views

``` python
from django.shortcuts import render
import random

# Create your views here.
def index(request):
  # 환영하는 메인 페이지를 보여준다.

  names = ['최준혁', '홍길동', '장길산', '김영철', '나진수']
  name = random.choice(names)
  
  context = {
    'name' : name,
    'img' : 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
    }
  
  return render(request, 'index.html', context) # 끝은 항상 render()를 리턴

```

* views.py 내에 페이지를 정의하고 인자를 넣어서 render에 인자, 페이지와 함께 반환

#### Templates

* 실제 내용을 보여주는데 사용되는 파일
* articles 폴더 내에 templates 폴더를 생성 후 파일을 만들어 작성

``` python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>welcome</title>
</head>
  <h1>{{ name }}님. 환영합니다 :)</h1>
  <img src="https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg" alt=""> 
</body>
</html>
```

