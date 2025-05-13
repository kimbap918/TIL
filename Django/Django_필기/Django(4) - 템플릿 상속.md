practicies : ping pong 기능 (form 활동 데이터 전송)이 있는 앱

-> practices/urls.py

articles : 방명록 기능이 있는 앱

-> articles/urls.py

## Template inheritance

#### 추가 템플릿 경로 추가하기

* base.html의 위치를 앱 안의 template 디렉토리가 아닌 프로젝트 최상단의 templates 디렉토리 안에 위치하고 싶다면?

* 기본 template 경로가 아닌 경로를 추가하기 위해 다음과 같은 코드를 작성

  <br>

  #### day3 프로젝트 폴더

  * articles, practices 폴더가 있는 최상단에 templates 폴더 생성 후 기존에 있던 base.html 파일을 집어넣는다.

  ![](https://i.imgur.com/MXE81WL.png)

  <br>

  #### day3pjt/settings.py

  ``` python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
        	# 이곳을 변경함, BASE_DIR에 templates라는 하위 폴더를 집어넣겠다는 뜻
          'DIRS': [BASE_DIR / 'templates',],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

  <br>

## Django URLs

* Dispatcher(운행 관리원)로서의 URL 이해하기
* 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작함

## App URL mapping

* 앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법을 이해하기

* 두번째 app인 pages를 생성 및 등록 하고 진행

* app의 view 함수가 많아지면서 사용하는 path() 또한 많아지고, app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트의 유지보수에 좋지 않음

  <br>

  #### day3pjt/urls.py

  ``` python
  from django.contrib import admin
  from django.urls import path
  from practices import views as practices_views
  from articles import views as articles_views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('index/', practices_views.index),
      path('ping/', practices_views.ping),
      path('pong/', practices_views.pong),
      path('is-odd-even/<int:_number>', practices_views.is_odd_even),
      path('calculate/<int:_number1>/<int:_number2>', practices_views.calculate),
      path('random_life/', practices_views.random_life),
      path('priv_life/', practices_views.priv_life),
      path('rorem/', practices_views.rorem),
      path('ipsum/', practices_views.ipsum),
      path('', articles_views.index),
  
  ]
  ```

  <br>

  #### practices

  * 세분화할 앱 폴더 내에 urls.py 파일을 생성 

  ![](https://i.imgur.com/qVRJVDd.png)

  <br>

  #### practices/urls.py

  * 해당 앱에 필요한 url을 작성, from import에 .은 현재 경로를 의미함

    ``` python
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('index/', views.index),
        path('ping/', views.ping),
        path('pong/', views.pong),
        path('is-odd-even/<int:_number>', views.is_odd_even),
        path('calculate/<int:_number1>/<int:_number2>', views.calculate),
        path('random_life/', views.random_life),
        path('priv_life/', views.priv_life),
        path('rorem/', views.rorem),
        path('ipsum/', views.ipsum),
    ]
    ```

    <br>

  #### day3pjt/urls.py(메인 urls.py)

  * 메인 urls.py에 include로 서브 url을 작성함

  * include되는 앱의 url.py에 urlpatterns가 작성되어 있지 않다면 에러가 발생 예를 들어, pages 앱의 urlpatterns가 빈 리스트라도 작성되어 있어야 함

    ``` python
    from django.contrib import admin
    # django.urls 안에 include 작성
    from django.urls import path, include
    
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        # 서브 URL들에 대한 설정을 '포함' 하게 만드는것
        path('articles/', include('articles.urls')),
        path('practices/', include('practices.urls')),
    
    ]
    ```

    <br>

## 방명록 - 게시판 내용 저장하기

#### articles/models.py

``` python
from django.db import models

# Create your models here.
class Article(models.Model):
    content = models.TextField()
```

<br>

#### terminal

``` terminal
$ python manage.py makemigrations
$ python manage.py migrate

# 실행결과
(day3-venv) server/day3 - (main) > python manage.py makemigrations 
Migrations for 'articles':
  articles/migrations/0001_initial.py
    - Create model Article
(day3-venv) server/day3 - (main) > python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying articles.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(day3-venv) server/day3 - (main) > 
```



#### articles/views.py

``` python
from django.shortcuts import render
from .models import Article

guestbook = []

# Create your views here.
def index(request):
    # DB에서 가져오기
    guestbook = Article.objects.all()
    return render(request, 'articles/index.html', {'guestbook': guestbook})

def create(request):
    content = request.GET.get('content')
    # DB에 저장
    Article.objects.create(content=content)
    return render(request, 'articles/create.html', {'content': content })
```

<br>

#### articles/template/article/create.html

``` html
{% extends 'base.html' %}
{% block content %}

<body>
  <div>
    <h1>방명록</h1>
  </div>
  <div>
    <h2>글 목록</h2>
    {% for content in guestbook %}
    <p> {{ content.content }}</p>
    {% endfor %}
  </div>
  <div>
    <h2>글 작성</h2>
    <form action="/articles/create">
      <input type="text" name="content">
      <input type="submit">
    </form>
  </div>


</body>

{% endblock %}
```

