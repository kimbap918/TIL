## 이미지 업로드하기

#### 사전 설정

``` python
$ pip install Pillow
$ pip install pilkit
$ pip freeze > requirements.txt
```

* Pillow의 설치 이유 : 이미지를 관리하기 위해서(Python Image Library)

<br>

#### models.py

``` python
# 1. 모델 설계 (DB 스키마 설계)
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 추가
    image = models.ImageField(upload_to='images/', blank=True)
```

<br>

#### forms.py

``` python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # 이미지 필드 추가
        fields = ['title', 'content', 'image']
```

<br>

#### views.py

``` python
def create(request):
    if request.method == 'POST':
        # request.FILES 추가
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context=context)

```

<br>

#### forms.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}

{% if request.resolver_match.url_name == 'create' %}
<h1> 글쓰기 </h1>
{% else %}
<h1> 수정하기 </h1>
{% endif %}

<!-- enctype 추가 -->
<form action="" method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {% bootstrap_form article_form %}
  {% bootstrap_button button_type="submit" content="OK" %}
</form>
{% endblock %}
```

<br>

## 수정화면에서의 이미지 업로드

#### detail.html

``` python
{% extends 'base.html' %}

{% block body %} 
<h1>{{ article.pk }}번 게시글</h1>
<p>{{ article.created_at|date:"SHORT_DATETIME_FORMAT" }} | {{ article.updated_at|date:"y-m-d D" }}</p>
<p>{{ article.content }} </p>
<img src="{{ article.image.url }}" alt="{{ article.image }}">
<a href="{% url 'articles:update' article.pk %}">수정하기</a>
{% endblock %}
```

<br>

#### settings.py

``` python
# Media files (user uploaded filed) 추가

MEDIA_ROOT = BASE_DIR / 'images'
MEDIA_URL = '/media/'
```

<br>

#### urls.py

``` python
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

<br>

## 이미지 Resizing

#### terminal

``` python
$ pip install django-imagekit
```

<br>

#### models.py

``` python
# imagekit import
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ProcessedImageField 추가
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(400, 300)],
                                format='JPEG',
                                options={'quality': 80})
```

<br>

## views.py

``` python
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # POST : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            article_form.save()
            messages.success(request, '글이 수정되었습니다.')
            return redirect('articles:detail', article.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)
```

<br>

#### detail.html

``` python
{% extends 'base.html' %}

{% block body %} 
<h1>{{ article.pk }}번 게시글</h1>
<p>{{ article.created_at|date:"SHORT_DATETIME_FORMAT" }} | {{ article.updated_at|date:"y-m-d D" }}</p>
<p>{{ article.content }} </p>
{% if article.image %}
    <img src="{{ article.image.url }}" alt="{{ article.image }}" width="400" height="300">
{% endif %}
<a href="{% url 'articles:update' article.pk %}">수정하기</a>
{% endblock %}
```

<br>

## 썸네일 업로드하기

#### models.py

``` python
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(400, 300)],
                                format='JPEG',
                                options={'quality': 60})
    image_thumbnail = ProcessedImageField(
	                                 upload_to = 'images/', 	# settings.py 원본 ImageField 명
	                                 processors = [Thumbnail(100, 100)], # 처리할 작업목록
		                             format = 'JPEG',		   # 최종 저장 포맷
		                             options = {'quality': 60}) # 저장 옵션
```

#### forms.py

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # 썸네일 추가
        fields = ['title', 'content', 'image', 'image_thumbnail']
```

<br>

#### index.html

``` html
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block body %}
  <h1>게시판</h1>
  {% if request.user.is_authenticated %}
    <a class="btn btn-primary my-3 float-right" href="{% url 'articles:create' %}">글 쓰기</a>
  {% endif %}

  <div class="row">
    {% for article in articles %}
      <div class="col-4">
        <div class="card">
          # image_thumbnail로 변경
          <img src="{{ article.image_thumbnail.url }}" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">{{ article.title }}</h5>
            <a href="{% url 'articles:detail' article.pk %}" class="btn btn-outline-primary my-3">복습하기</a>
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
{% endblock %}
```

<br>

#### detail.html

``` python
{% extends 'base.html' %}

{% block body %}
  <h1>{{ article.pk }}번 게시글</h1>
  <p>{{ article.created_at|date:"SHORT_DATETIME_FORMAT" }}
    |
    {{ article.updated_at|date:"y-m-d D" }}</p>
  <p>{{ article.content }}
  </p>
  {% if article.image %}
    <img src="{{ article.image.url }}" alt="{{ article.image }}" width="400" height="300">
  {% endif %}
  {% if article.image_thumbnail %}
    <img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}" width="400" height="300">

  {% endif %}
  <a href="{% url 'articles:update' article.pk %}">수정하기</a>
  <a href="{% url 'articles:delete' article.pk %}">삭제하기</a>
{% endblock %}
```

