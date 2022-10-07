# Django CRUD 

> Django : 파이썬 기반 웹 프레임워크 

## 1. 가상환경 및 Django 설치

> 가상환경 : 프로젝트별 별도 패키지 관리

### 1. 가상환경 생성 및 실행

* 가상환경 폴더를 `.gitignore`로 설정을 해둔다.

```bash
$ python -m venv venv
$ source venv/bin/activate
(venv) $
```

### 2. Django 설치 및 기록

```terminal
$ pip install django==3.2.13
$ pip install django-bootstrap5 # 부트스트랩 5 설치시
$ pip freeze > requirements.txt
```

### 3. Django 프로젝트 생성

```bash
$ django-admin startproject pjt .
```

## 2. articles app 

> Django : 주요 기능 단위의 App 구조, App 별로 MTV를 구조를 가지는 모습 + `urls.py` 

### 1. app 생성 및 실행

```bash
$ python manage.py startapp app_name
$ python manage.py runserver
```

### 2. app 등록

* `settings.py` 파일의 `INSTALLED_APPS`에 추가

```python
INSTALLED_APPS = [
    'articles',
  	'django_bootstrap5', # 부트스트랩 사용시
    ...
]
```

## 3. Model 정의 (DB 설계)

### 1. 클래스 정의

```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 2. 마이그레이션 파일 생성

* app 폴더 내의 `migrations` 폴더에 생성된 파일 확인

```bash
$ python manage.py makemigrations
```

### 3. DB 반영(`migrate`)

```bash
$ python manage.py migrate
```

## 4. urls.py 설정

> app 단위의 URL 관리

```python
# pjt/urls.py
urlpatterns = [
    ...
    path('articles/', include('articles.urls')),
]
```

```python
# articles/urls.py
from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
  # http://127.0.0.1:8000/articles/
  path('', views.index, name='index'),
  ...
]
```

* 활용 : `articles:index` => `/articles/`

* Template에서 활용 예시
```django
{% url 'articles:index' %}
```

* View에서 활용 예시

```python
redirect('articles:index')
```

* settings.py  TEMPLATES에 추가

````python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "pjt" / "templates"], # DIRS에 경로 등록
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```
````

## 5. CRUD 기능 구현

### 0. ModelForm 선언

> 선언된 모델에 따른 필드 구성 (1) Form 생성 (2) 유효성 검사

```python
# 애플리케이션 폴더에 forms.py 생성하기
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content']
```

### 1. 게시글 생성

> 사용자에게 HTML Form 제공, 입력받은 데이터를 처리 (ModelForm 로직으로 변경)

#### 1. HTML Form 제공

> GET http://127.0.0.1:8000/articles/create/

##### (1) urls.py 

``` python
from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
]
```
##### (2) views.py

```python
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def create(request):
    # forms.py에서 선언한 ArticleForm
    article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context=context)
```

##### (3) articles/create.html

* HTML Form 태그 활용시 핵심

  * 어떤 필드를 구성할 것인지 (`name`, `value`)

  * 어디로 보낼 것인지 (`action`, `method`)

``` html
<h1>글쓰기</h1>
<!-- 제출을 POST 방식으로 -->
<form action="" method="POST">
  {% csrf_token %}
  {{ article_form.as_p }}
  <input type="submit" value="글쓰기">
</form>
```

#### 2. 입력받은 데이터 처리

> POST http://127.0.0.1:8000/articles/create/

> 게시글 DB에 생성하고 index 페이지로 redirect

##### (1) urls.py

``` python
from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
]
```

##### (2) views.py

* GET 요청 처리 흐름

* POST 요청 처리 흐름 (주의! invalid)

```python
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
```

### 2. 게시글 목록

> DB에서 게시글을 가져와서, template에 전달

##### (1) urls.py

``` python
from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
]
```

##### (2) views.py

``` python
# 요청 정보를 받아서..
def index(request):
    # 게시글을 가져와서..
    articles = Article.objects.order_by('-pk')
    # Template에 전달한다. 
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)
```

##### (3) index.html

``` html
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block body %} 
<h1>게시판</h1>
<img src="{% static 'images/apparel.jpeg' %}" alt="">
<!-- urls.py에서 등록한 app_name Template에서 사용하기  -->
<a href="{% url 'articles:create' %}">글 쓰기</a>
{% for article in articles %}
<h3><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></h3>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<hr>
{% endfor %}
{% endblock %}
```

### 3. 상세보기

> 특정한 글을 본다.

> http://127.0.0.1:8000/articles/<int:pk>/

##### (1) urls.py

``` python
from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
]

```

##### (2) views.py

``` python

def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

```

##### (3) detail.html

``` html
{% extends 'base.html' %}

{% block body %} 
<h1>{{ article.pk }}번 게시글</h1>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>{{ article.content }} </p>
{% endblock %}

```

### 4. 삭제하기

> 특정한 글을 삭제한다.

> http://127.0.0.1:8000/articles/<int:pk>/delete/

##### (1) url.py

``` python
from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
  path('<int:pk>/delete/', views.delete, name='delete'),
]

```

##### (2) views.py

``` python
def delete(request, pk):
    # pk에 해당하는 글 삭제
    Article.objects.get(pk=pk).delete()

    return redirect('articles:index')
```

##### (3) detail.html

``` html
{% extends 'base.html' %}

{% block body %} 
<h1>{{ article.pk }}번 게시글</h1>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>{{ article.content }} </p>
<a href="{% url 'articles:delete' article.pk %}">삭제하기</a>
{% endblock %}

```

### 5. 수정하기

> 특정한 글을 수정한다. => 사용자에게 수정할 수 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)

> http://127.0.0.1:8000/articles/<int:pk>/update/

##### (1) urls.py

``` python
from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
  path('<int:pk>/delete/', views.delete, name='delete'),
  path('<int:pk>/update/', views.update, name='update'),

]

```

##### (2) views.py

``` python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # POST : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            article_form.save()
            # urls.py에서 등록한 app_name view에서 활용
            return redirect('articles:detail', article.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)

```

##### (3) detail.html
``` html
{% extends 'base.html' %}

{% block body %}
<h1>{{ article.pk }}번 게시글</h1>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>{{ article.content }} </p>
<a href="{% url 'articles:delete' article.pk %}">수정하기</a>
<a href="{% url 'articles:update' article.pk %}">수정하기</a>
{% endblock %}
```

## Django Admin

``` terminal
$ source venv/bin/activate # 가상환경 실행
$ python manage.py createsuperuser # 슈퍼유저 생성

Username (leave blank to use 'mac'): admin
Email address: fx887722@naver.com
Password: 
Password (again): 
Superuser created successfully.
(server-venv) server/day3 - (main) > 
```

<br>

admin.py

``` python
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title']

admin.site.register(Article, ArticleAdmin)
```

<br>

#### Static files

* 웹 서버는 특정 위치(URL)에 있는 자원(resource)을 요청받아서 제공하는 응답을 처리하는 것을 기본 동작으로 한다.
* 즉, 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공

settings.py

``` python
...
import os

INSTALLED_APPS = [
    'posts',
    'articles',
    'practices',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # 프로젝트 생성시 설정이 되어있음
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/' # 기본으로 설정되어있음.

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'config', 'static') # 추가
]
```

<br>

앱 안에 static 폴더 생성 -> static 폴더 안에 image 폴더 생성 -> 생성한 image 폴더에 이미지 넣기

<br>

HTML 내에서 아래와 같이 {% STATIC_URL 에 설정한 경로  '파일명' %} 사용시 파일 로드 가능

``` html
<img src="{% static 'image/apparel.jpeg' %}">
```

<br>

## Django Bootstrap5

#### settings.py

``` python
INSTALLED_APPS = [
    'articles',
    'django_bootstrap5', # 부트스트랩 추가
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

<br>

#### 사용 예시

``` html
{% load django_bootstrap5 %}

{% bootstrap_css %}

{% bootstrap_javascript %}

{% bootstrap_form article_form %}

{% bootstrap_button button_type="submit" %}
```

## 추천 문서

* [HTTP request & response object](https://docs.djangoproject.com/en/4.1/ref/request-response/)

* [ModelForm](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/)

* [Django view shortcut functions](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/)