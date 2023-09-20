## Django 정리해보기

### Django?

파이썬 기반의 웹 프레임워크

<br>

### Django 서버

사용자가 요청을 하면 django에서 응답을 해준다. 어떻게?

1. URL 요청을 받아서
2. 처리하고 (views.py)
3. 응답을 해준다  (Template)

-> MTV 모델(Model, Template, View)

<br>

## Django CRUD

#### 가상환경 및 Django설치

* 프로젝트별 독립적인 개발 환경을 유지하기 위해

``` terminal
$ python -m venv venv(가상환경 이름) # 가상환경 생성
$ source venv/bin/activate # 가상환경 실행
# (venv) $
$ pip install django==3.2.13 # Django LTS 버전 설치
$ pip freeze > requirements.txt # 기록지 생성
```

<br>

#### Django 프로젝트 생성 및 실행

``` terminal
$ django-admin startproject pjt .(프로젝트명) # Django 프로젝트 생성
$ python manage.py startapp practice(애플리케이션 이름) # 앱 생성
$ python manage.py runserver # 앱 실행 
```

<br>

url을 등록하고, view 함수 생성, template를 만드는 flow

#### urls.py 설정

settings.py

* 생성한 앱 등록(필수), 그 외에 언어 설정도 가능 

``` python
# Application definition

INSTALLED_APPS = [
    'practice', # 앱을 등록한다.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr' # 언어 설정도 가능

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

```

<br>

urls.py

* 다른 url들의 설정을 가져오려면 include를 import해서 사용한다.

``` python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

<br>

``` python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index')
]
```

<br>

#### view 함수 생성

views.py

``` python
from django.shortcuts import render

# 요청 정보를 받아서
def index(request):
		# 페이지를 render
    return render(request, 'articles/index.html')
```

<br>

#### template 생성

index.html

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
	<h1>게시판</h1>
	<a href="{% url 'articles:new' %}">글쓰기</a>
</body>

</html>
```

<br>

## Model 정의

클래스 정의

``` python
from django.db import models

# 1. 모델 설계(DB 스키마 설계)
class Article(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  careated_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
```

<br>

마이그레이션

``` terminal
$ python mange.py makemigrations # 마이그레이션 파일 생성
$ python manage.py migrate # DB에 반영
```

<br>

## CRUD 기능 구현

#### 1. 생성(Create)

* 사용자에게 HTML Form 제공, 입력한 데이터를 처리

urls.py

``` python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('new', views.new, name='new'),
  path('create', views.create, name='create')
]
```

views.py

``` python
from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
		# 페이지를 render
    return render(request, 'articles/index.html')
  
def new(request):
  
  return render(request, 'articles/new.html')

def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')
  Article.objects.create(title=title, content=content)
  return redirect('articles:index')
```

new.html

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
	<h1>글쓰기</h1>
  <form action="{% url 'articles:create' %}">
    <label for="title">제목 : </label>
    <input type="text" name="title" id='title'>
    <label for="title">내용 : </label>
    <textarea name="content" id='content' cols='30' rows=10></textarea>
    <input type="submit" value='글쓰기'>
  </form>
</body>

</html>
```

<br>

#### 2. 읽기(Read)

* 게시글을 가져와서 템플릿에 전달

views.py

``` python
from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
  	# 게시글을 가져와서
  	articles = Article.objects.order_by('-pk')
    # template에 전달한다
    context = {
      'articles' : articles
    }
		# 페이지를 render
    return render(request, 'articles/index.html')
  
def new(request):
  
  return render(request, 'articles/new.html')

def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')
  Article.objects.create(title=title, content=content)
  return redirect('articles:index')
```

<br>

index.html

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
	<h1>게시판</h1>
	<a href="{% url 'articles:new' %}">글쓰기</a>
  {% for article in articles %}
  <h3>{{ article.title}}</h3>
  <p>{{ article.created_at}} | {{ article.updated_at}}</p>
  <hr>
  {% endfor %}
</body>

</html>
```

<br>

#### (번외)Create - POST로 제출하기

new.html

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
	<h1>글쓰기</h1>
  <!-- method를 POST로 변경 -->
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <label for="title">제목 : </label>
    <input type="text" name="title" id='title'>
    <label for="title">내용 : </label>
    <textarea name="content" id='content' cols='30' rows=10></textarea>
    <input type="submit" value='글쓰기'>
  </form>
</body>

</html>
```

<br>

views.py

``` python
from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
  	# 게시글을 가져와서
  	articles = Article.objects.order_by('-pk')
    # template에 전달한다
    context = {
      'articles' : articles
    }
		# 페이지를 render
    return render(request, 'articles/index.html')
  
def new(request):
  
  return render(request, 'articles/new.html')

def create(request):
  title = request.POST.get('title')
  content = request.POST.get('content')
  Article.objects.create(title=title, content=content)
  return redirect('articles:index')
```

<br>

## Django ModelForm

* DB기반의 애플리케이션을 개발하다보면,  HTML Form(UI)은 Django 모델(DB)과 매우 밀접한 관계를 가지게 됨
  * 사용자로부터 값을 받아 DB에 저장하여 활용하기 때문
  * 즉, 모델에 정의한 필드의 구성 및 종류에 따라 HTML Form이 결정됨
* 사용자가 입력한 값이 DB의 데이터 형식과 일치하는지를 확인하는 유효성 검증이 반드시 필요하며 이는 서버 사이드에서 반드시 처리해야함.

forms.py 생성

``` python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
  
  class Meta:
    model = Article
    fields = '__all__'
    # fields = ['title', 'content'] 필요한것만 가져올 수 있음
```

 <br>

views.py

``` python
from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
  	# 게시글을 가져와서
  	articles = Article.objects.order_by('-pk')
    # template에 전달한다
    context = {
      'articles' : articles
    }
		# 페이지를 render
    return render(request, 'articles/index.html')
  
#def new(request):
#  article_form = ArticleForm()
#  context = {
#    'article_form' : article_form
#  }
#  return render(request, 'articles/new.html', context=context)

# new를 제거하고 create에서 전부 처리 가능
def create(request): # 유효성 검사도 가능
  if request.method == 'POST':
  	article_form = ArticleForm(request.POST)
  	if article_form.is_valid():
    	article_form.save()
    	return redirect('articles:index')
  else:
    # 유효하지 않을때
    article_form = ArticleForm()
    context = {
      'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
```

<br>

new.html

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
	<h1>글쓰기</h1>
  <!-- method를 POST로 변경 -->
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <!-- 기존의 form을 대체할 수 있다 -->
    {{ article_form.as_p }}
</body>

</html>
```

<br>

#### 3. read - 상세보기

url.py

``` python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  # path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
]
```

views.py

``` python
from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
  	# 게시글을 가져와서
  	articles = Article.objects.order_by('-pk')
    # template에 전달한다
    context = {
      'articles' : articles
    }
		# 페이지를 render
    return render(request, 'articles/index.html')
  
#def new(request):
#  article_form = ArticleForm()
#  context = {
#    'article_form' : article_form
#  }
#  return render(request, 'articles/new.html', context=context)

# new를 제거하고 create에서 전부 처리 가능
def create(request): # 유효성 검사도 가능
  if request.method == 'POST':
  	article_form = ArticleForm(request.POST)
  	if article_form.is_valid():
    	article_form.save()
    	return redirect('articles:index')
  else:
    # 유효하지 않을때
    article_form = ArticleForm()
    context = {
      'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
  
def detail(request):
  article = Article.onjects.get(pk=pk)
  context = {
    'article' : article
  }
  return render(request, 'articles/detail.html', context)
  
```

detail.html

``` python
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
	<h1>{{ article.pk }}번 게시글</h1>
  <p>{{ article.created_at }} | {{ article.updated_at}}</p>
  <p>{{ article.content }}</p>
  <a href="{% url 'article:update' article.pk %}">수정하기</a>
</body>

</html>
```

<br>

#### 수정하기(Update)

urls.py

``` python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  # path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
  path('<int:pk>/update/', views.update, name='update'),
]
```

<br>

views.py

``` python
from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
  	# 게시글을 가져와서
  	articles = Article.objects.order_by('-pk')
    # template에 전달한다
    context = {
      'articles' : articles
    }
		# 페이지를 render
    return render(request, 'articles/index.html')
  
#def new(request):
#  article_form = ArticleForm()
#  context = {
#    'article_form' : article_form
#  }
#  return render(request, 'articles/new.html', context=context)

# new를 제거하고 create에서 전부 처리 가능
def create(request): # 유효성 검사도 가능
  if request.method == 'POST':
  	article_form = ArticleForm(request.POST)
  	if article_form.is_valid():
    	article_form.save()
    	return redirect('articles:index')
  else:
    # 유효하지 않을때
    article_form = ArticleForm()
  context = {
      'article_form': article_form
  }
 	return render(request, 'articles/new.html', context=context)
 
def detail(request):
  article = Article.onjects.get(pk=pk)
  context = {
    'article' : article
  }
  return render(request, 'articles/detail.html', context)
  
def update(request, pk)
  article = Article.objects.get(pk=pk)
  if request.method == 'POST':
    # POST : input 값 가져와서 검증하고 DB에 저장
    article_form = ArticleForm(request.POST, instance=article) # 특정한 글을 수정하는 것이기 때문에 인스턴스를 반드시 넘겨주어야 함
    if article_form.is_valid():
      # 유효성 검사 통과하면 저장하고 상세보기 페이지로 
      article_form.save()
      return redirect('articles:detail', article.pk)
      
  else:
  	article_form = ArticleForm(instance=article)
  context = {
    'article_form' : article_form
  }
  return render(request, 'artitle/update.html', context)
  
```

<br>

update.html

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
	<h1>글 수정하기</h1>
  <form action="{% url 'articles:update' %}" method="POST"></form>
  {{ article_form.as_p }}
  <input type="submit" value="수정하기">
  </form>
</body>

</html>
```

