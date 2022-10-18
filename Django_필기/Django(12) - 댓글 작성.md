## A one-to-many relationship

#### RDB(관계형 데이터베이스)

* 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
*  RDB의 모든 테이블에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만드는 데 사용할 수 있음

<br>

#### RDB에서의 관계

* 1:1 : 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
  * 사용자의 프로필 페이지등의 관계
* 1:N : 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
  * 기준 테이블에 따라(1:N, One-to-many relationships)이라고도 한다.
  * 사용자의 글 / 댓글등의 관계 
* M:N : 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
  * 양쪽 모두에게서 1:N 관계를 가진다

<br>

#### Foreign Key

특징

* 키를 사용하여 부모 테이블의 유일한 값을 참조(참조 무결성)
  * 참조 무결성 : 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
    * 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 해당 테이블의 기본 키 값으로 존재
* 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함

<br>

#### 1:N 관계로 게시판과 게시글 표현하기

모델 관계 설정

* 게시판의 게시글과 1:N 관계를 나타낼 수 있는 댓글 구현
* 1:N 관계에서 댓글을 담당할 Article 모델은 1, Comment 모델은 N이 될 것
  * 게시글은 댓글을 0개 이상 가진다. 
    * 게시글(1)은 여러 개의 댓글(N)을 가진다.
    * 게시글(1)은 댓글을 가지지 않을 수도 있다.
  * 댓글은 반드시 하나의 게시글에 속한다.

<br>

#### Django Relationship fields 종류

* OneToOneField()
* ForeignKey()
  * one-to-many
* ManyToManyField()

<br>

#### ForeignKey(to, on_delete, **options)

* A one-to-many relationship을 담당하는 django의 모델 필드 클래스
* Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
* 2개의 필수 위치 인자가 필요
  * 참조하는 model class
  * on_delete 옵션

<br>

#### ForeignKey arguments - on_delete

* 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할지를 정의
* 데이터 무결성을 위해서 매우 중요한 설정
* on_delete 옵션 값
  * CASCADE: 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
  * PROTECT, SET_NULL, SET_DEFAULT 등 여러 옵션 값들이 존재

<br>

#### Comment 모델 정의

* 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계 없이 필드의 마지막에 작성됨
* ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장

#### models.py

``` python
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # integer가 저장되지만 integerField를 안쓰는이유?
    # 참조 대상은(직접 참조) comment.article
    # 역참조는 article.comment_set 하려고
    # A라고 하는 모델에 B모델의 FK를 정의했을때 B모델은 A모델을 어떻게 쓸까? -> b.a_set
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

<br>

#### admin.py

``` python
from django.contrib import admin
from .models import Article, Comment

# Register your models here.
# https://docs.djangoproject.com/en/3.2/intro/tutorial07/
class ArticleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'created_at', 'updated_at')
# Comment 추가
class CommentAdmin(admin.Model):
    list_display = ('content', 'created_at', 'article')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
```

<br>

#### shell plus

``` terminal
$ python manage.py shell_plus


Article.objects.all()
Article.objects.create(title='제목1', content='내용1')
article = Article.objects.create(title='제목1', content='내용1')
# 게시글 13번에 내용이 111인 댓글을 작성하는 코드?
comment = Comment.objects.create(content='111', article=article)
comment.article # 결과가 뭘까?
# <Article: Article object (13)>
comment.article_id # 결과는?
# 13
comment = Comment.objects.create(contnet='111', article_id=13)
# 13번 게시글의 모든 댓글을 알고자 한다면 어떻게 해야할까?
Comment.objects.filter(article_id=13)
article.comment_set.all()
# 같은 결과가 나옴
```

<br>

#### 게시글 상세페이지에서 댓글들을 출력

#### views.py

``` python
def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        'article': article,
        'comment': article.comment_set.all(),
    }
    return render(request, 'articles/detail.html', context)
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
  # 댓글 출력
  <h4 class="my-3">댓글</h4>
  {% for comment in article.comment_set.all %}
    <p>{{ comment.content }}</p>
    <hr>
  {% endfor %}
{% endblock %}
```

<br>

#### 게시글 상세페이지에서 댓글 입력창 만들기

#### forms.py

``` python
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'image_thumbnail']
# commentForm 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
```

#### views.py

``` python
def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # template에 객체 전달
    context = {
        'article': article,
        'comments': article.comment_set.all(),
      	# comment_form 추가
        'comment_form': comment_form
    }
    return render(request, 'articles/detail.html', context)
```

#### detail.html

``` html
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
  <h4 class="my-3">댓글</h4>
  <form action="">
    {% bootstrap_form comment_form %}
    {% bootstrap_button button_type="submit" content="OK" %}
    {% comment %}  {% endcomment %}
  </form>
  <hr>
  {% for comment in comments %}
    <p>{{ comment.content }}</p>
    <hr>
    {% empty %}
    <p>댓글이 없어요 ㅠ_ㅠ</p>
  {% endfor %}
{% endblock %}
```

<br>

#### 

#### urls.py

``` python
from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
  path('<int:pk>/update/', views.update, name='update'),
  path('<int:pk>/delete/', views.delete, name='delete'),
  # comment_create 생성
  path('<int:pk>/comments/', views.comment_create, name='comment_create'),
]
```

<br>

#### views.py

``` python
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST) # CommentForm의 인스턴스(모델폼)
    if comment_form.is_valid(): # comment_form : 어떤 클래스의 인스턴스
      	# 직접 DB에 save하지 않고 객체를 주면 
        # 내가 필요한 값을 직접 넣고 
        # save함
        comment = comment_form.save(commit=False) # comment : 어떤 클래스의 인스턴스
        comment.article = article # 모델폼의 save메서드는 리턴값이 그 모델의 인스턴스
        comment_form.save()
    return redirect('articles:detail', article.pk)
```

<br>

#### detail.html

``` html
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
  <h4 class="my-3">댓글</h4>
  <!-- comment_create 수정 -->
  <form action="{% url 'articles:comment_create' %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form comment_form layout='inline' %}
    {% bootstrap_button button_type="submit" content="OK" %}
    {% comment %}  {% endcomment %}
  </form>
  <hr>
  {% for comment in comments %}
    <p>{{ comment.content }}</p>
    <hr>
    {% empty %}
    <p>댓글이 없어요 ㅠ_ㅠ</p>
  {% endfor %}
{% endblock %}
```

<br>

#### 댓글 삭제

#### urls.py

``` python
from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
  path('<int:pk>/update/', views.update, name='update'),
  path('<int:pk>/delete/', views.delete, name='delete'),
  path('<int:pk>/comments/', views.comment_create, name='comment_create'),
  # 삭제 url 생성
  path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
```

<br>

#### views.py

``` python
from .models import Article, Comment

def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

<br>

#### detail.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}


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
  <div>
  <a class="btn btn-primary my-3" href="{% url 'articles:update' article.pk %}">수정하기</a>
  <a class="btn btn-danger my-3" href="{% url 'articles:delete' article.pk %}">삭제하기</a>
  </div>
  <h4 class="my-3">댓글</h4>
  <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form comment_form layout='inline' %}
    {% bootstrap_button button_type="submit" content="OK" %}
    {% comment %}  {% endcomment %}
  </form>
  <hr>
  {% for comment in comments %}
    <p>{{ comment.content }}</p>
		<!-- delete form 추가 -->
    <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
    <hr>
    {% empty %}
    <p>댓글이 없어요 ㅠ_ㅠ</p>
  {% endfor %}
{% endblock %}
```

<br>

#### 댓글 개수 카운트

``` html
  <p>총 {{ comments.count }}개의 댓글이 있습니다.</p>
```

