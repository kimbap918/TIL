## 게시글에 작성자 나타내기

#### models.py

``` python
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail
from imagekit.models import ImageSpecField
from django.db import models
from django.conf import settings

# Create your models here.
'''
게시판 기능 
- 제목(20글자이내)
- 내용(긴 글)
- 글 작성시간/수정시간(자동으로 기록, 날짜/시간)
'''
# 1. 모델 설계 (DB 스키마 설계)
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(400, 300)],
                                format='JPEG',
                                options={'quality': 80})
    image_thumbnail = ProcessedImageField(
	                                      upload_to = 'images/', 	blank=True,# settings.py 원본 ImageField 명
	                                      processors = [Thumbnail(100, 100)], # 처리할 작업목록
		                                  format = 'JPEG',		   # 최종 저장 포맷
		                                  options = {'quality': 60}) # 저장 옵션
    # 모델에 user 추가
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, null=True)
```

<br>

#### terminal

``` terminal
$ python manage.py makemigrations
$ python manage.py migrate

# 실행결과
# You are trying to add a non-nullable field 'user' to article without a default; we can't do that (the database needs something to populate existing rows).
# Please select a fix:
# 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
# 2) Quit, and let me add a default in models.py

# -> 기존 정보에 새로운 속성이 추가되어서 변경 이전에 존재하던 행들을 어떻게 처리할것인지 물어보는것
# 기본값을 넣던지, null=True를 하던지.
```

<br>

#### articles > views.py

``` python
@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
          	# 댓글 저장과 같이바로 저장하지 않고 
            # 객체를 주면 내가 필요한 값을 넣고 저장함
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
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

#### articles > detail.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}


{% block body %}
  <h1>{{ article.pk }}번 게시글</h1>
  <p>{{ article.created_at|date:"SHORT_DATETIME_FORMAT" }}
    |
    {{ article.updated_at|date:"y-m-d D" }}</p>
	<!-- 작성자 이름 출력되도록 추가 -->
  <p>작성자: {{ article.user }}</p>
  <p>{{ article.content }}
  </p>
	...
```

#### articles > index.html

``` html

  <div class="row">
    {% for article in articles %}
      <div class="col-4">
        <div class="card">
          {% if article.image_thumbnail %}
            <img src="{{ article.image_thumbnail.url }}" class="card-img-top" alt="...">
          {% else %}
            <img src="https://dummyimage.com/1200x960/000000/c4c4c4" class="card-img-top">
          {% endif %}
          <div class="card-body">
            <h5 class="card-title">{{ article.title }}</h5>
            <!-- 작성 유저명이 나오도록 변경 -->
            <p class="text-muted">{{ article.user.username }}</p>
            <a href="{% url 'articles:detail' article.pk %}" class="btn btn-outline-primary my-3">복습하기</a>
          </div>
        </div>
      </div>
```

<br>

## 게시글에 작성자 이름 클릭 시 프로필로 이동

#### articles > detail.html 

``` python
{% block body %}
  <h1>{{ article.title }}</h1>
  <h2>{{ article.pk }}번 게시글</h2>
  <h3><a href="{% url 'accounts:detail' article.user.pk %}">{{ article.user.username }}</a></h3>
  <p>{{ article.created_at|date:"SHORT_DATETIME_FORMAT" }}
    |
    {{ article.updated_at|date:"y-m-d D" }}</p>
  <p>작성자: {{ article.user }}</p>
  <p>{{ article.content }}
  </p>
  ...
```

<br>

## 사용자가 아닌 다른 유저의 글 수정 막기

#### articles > views.py

``` python
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:

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
    else:
        # (1) 403 에러메세지를 던진다
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()
        # (2) flash message 활용
        # messages.warning(request, '작성자만 수정할 수 있습니다.')
        # return redirect('articles:detail', article.pk)

```

<br>

#### front 에서 막기 

#### articles > detail.html

``` python
  {% if request.user == article.user %}
  <div>
  <a class="btn btn-primary my-3" href="{% url 'articles:update' article.pk %}">수정하기</a>
  <a class="btn btn-danger my-3" href="{% url 'articles:delete' article.pk %}">삭제하기</a>
  </div>
  {% endif %}
```

<br>

## 댓글에 작성자 이름이 뜨게하기

#### articles > models.py

``` python
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # user는 settings.AUTH_USER_MODEL에 정의된 accounts앱에 user 클래스
    # 역참조해서 사용 : user.comment_set.all()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, null=True)
```

<br>

#### articles > views.py

``` python
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        # comment.user 추가
        comment.user = request.user
        comment_form.save() # 모델 인스턴스의 save()
    return redirect('articles:detail', article.pk)

```

<br>

#### articles > detail.html

``` html
  <h4 class="my-3">댓글</h4>
  {% if request.user.is_authenticated %}
  <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form comment_form layout='inline' %}
    {% bootstrap_button button_type="submit" content="OK" %}
    {% comment %}  {% endcomment %}
  </form>
  {% endif %}  
	<hr>
  <p>총 {{ comments.count }}개의 댓글이 있습니다.</p>
  {% for comment in comments %}
		<!-- 댓글에 작성자 이름이 뜨게끔 -->
    <p>{{ comment.user.username }} | {{ comment.content }}</p>
    <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
    <hr>
...
```

<br>

## 프로필에 자신이 작성한 글 표시하기

#### accounts > detail.html

``` html
{% extends 'base.html' %}

{% block body %}
  <h1>{{ user.username }}님의 프로필</h1>
  <p>{{ user.email }}
    |
    {{ user.full_name }}
  </p>
  {% for article in user.articles_set.all %}
		<!-- 작성자의 게시글을 클릭하면 해당 게시글로 감 -->
		{{ forloop.counter }}
    <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
    <p>{{ article.title }}</p>
  {% endfor %}

{% endblock body %}
```

<br>

## 프로필에 자신이 작성한 댓글 표시하기 + 몇개의 글을 썼는지 추가

``` html
{% extends 'base.html' %}

{% block body %}
  <h1>{{ user.username }}님의 프로필</h1>
  <p>{{ user.email }}
    |
    {{ user.full_name }}
  </p>
  <div class="col-6">
    <h3>작성한 글</h3>
    <p class="text-muted">{{ user.article_set.count }}개를 작성하였습니다.</p>
    {% for article in user.article_set.all %}
      <p>
        {{ forloop.counter }}
        <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
      </p>
    </div>
  {% endfor %}

  <div class="col-6">
    <h3>작성한 댓글</h3>
    <p class="text-muted">{{ user.comment_set.count }}개를 작성하였습니다.</p>
    {% for comment in user.comment_set.all %}
      <p>
        {{ forloop.counter }}
        <a href="{% url 'articles:detail' comment.article.pk %}">{{ comment.content }}</a>
      </p>
    </div>
  {% endfor %}

{% endblock body %}
```

<br>
