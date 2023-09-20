# 영화 리뷰 채널 프로젝트

- 요구 사항

  ### 모델 Model

  - 모델 이름 : User

    Django **AbstractUser** 모델을 상속 받고, 필드를 직접 정의하세요.

  - 모델 이름 : Review

    모델의 필드를 직접 정의하세요.

  - 모델 이름 : Comment

    모델의 필드를 직접 정의하세요.

  ### **폼 Form**

  회원 가입

  - Django 내장 회원 가입 폼 UserCreationForm을 상속 받아서 CustomUserCreationForm 생성
  - 출력할 필드를 직접 정의합니다.

  로그인

  - Django 내장 로그인 폼 AuthenticationForm 활용

  ### 기능 View

  **리뷰 reviews**

  데이터 목록 조회

  - `GET` http://127.0.0.1:8000/reviews/

  데이터 정보 조회

  - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/

  데이터 생성

  - `POST` http://127.0.0.1:8000/reviews/create/
  - 로그인한 유저만 데이터 생성이 가능합니다.

  데이터 수정

  - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
  - 해당 리뷰 작성자만 수정할 수 있습니다.

  데이터 삭제

  - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/delete/
  - 해당 리뷰 작성자만 삭제할 수 있습니다.

  리뷰 좋아요 / 좋아요 취소

  - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/like/
  - 로그인한 유저만 좋아요 기능을 사용할 수 있습니다.

  **댓글 comments**

  리뷰의 댓글 목록 조회

  - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/
  - 해당 게시글의 댓글 목록 조회

  댓글 생성

  - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/comments/create/
  - 로그인한 유저만 댓글 생성이 가능합니다.

  댓글 삭제

  - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/comments/[int:comment_pk](int:comment_pk)/delete/
  - 해당 댓글 작성자만 삭제할 수 있습니다.

  **회원 관리 accounts**

  회원 가입

  - `POST` http://127.0.0.1:8000/accounts/signup/

  회원 목록 조회

  - `GET` http://127.0.0.1:8000/accounts/

  회원 정보 조회

  - `GET` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/

  로그인

  - `POST` http://127.0.0.1:8000/accounts/login/

  로그아웃

  - `POST` http://127.0.0.1:8000/accounts/logout/

  팔로우

  - `POST` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/follow/
  - 로그인한 유저만 팔로우 기능을 사용할 수 있습니다.
  - 자기 자신은 팔로우 할 수 없습니다.

  ### 화면 Template

  **네비게이션바, Bootstrap <nav>**

  - 서비스 로고
  - 리뷰 목록 페이지 이동 버튼
  - 리뷰 작성 페이지 이동 버튼
  - 로그인 상태에 따라 다른 화면을 출력합니다.
    1. 로그인 상태
       - 로그인한 사용자의 username
       - 로그아웃 버튼
    2. 비 로그인 상태
       - 로그인 페이지 이동 버튼
       - 회원 가입 페이지 이동 버튼

  **메인 페이지**

  - `GET` http://127.0.0.1:8000/
  - 자유 디자인

  **목록 페이지**

  - `GET` http://127.0.0.1:8000/reviews/

  **리뷰 정보 페이지**

  - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/
  - 해당 리뷰 정보 출력
  - 댓글 작성 폼
  - 해당 리뷰에 작성된 댓글 목록
    - 각 댓글에는 삭제 버튼이 있습니다. 단, 댓글 작성자만 삭제를 할 수 있습니다.
  - 좋아요 버튼
    - 해당 리뷰의 좋아요 개수를 함께 출력합니다.
    - 로그인한 유저는 리뷰에 좋아요를 남길 수 있습니다.

  **리뷰 작성 페이지**

  - `GET` http://127.0.0.1:8000/reviews/create/
  - 리뷰 작성 폼

  **리뷰 수정 페이지**

  - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
  - 리뷰 수정 폼

  회원 가입 페이지

  - `GET` http://127.0.0.1:8000/accounts/signup/
  - 회원 가입 폼

  회원 조회 페이지(프로필 페이지)

  - `GET` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/
  - 회원이 작성한 게시글 목록 출력

  로그인 페이지

  - `GET` http://127.0.0.1:8000/accounts/login/
  - 로그인 폼
  - 회원 가입 페이지 이동 버튼

  팔로우 버튼

  - 로그인한 유저는 해당 유저를 팔로우 할 수 있습니다.
  - 단, 자기 자신은 팔로우 할 수 없습니다.

------

## 사전 설정

1. 원격 저장소 생성

2. 콜라보레이터 초대

   **초대자**

   * 레포지토리의 settings -> Access의 Collaborators -> Manage access -> Add people  -> 초대할 대상 아이디 입력

   **초대받은 대상**

   * github계정 생성때 사용한 이메일로 가서 view invitation 클릭
   * github창 열리면 Accept invitation클릭
   * 초대받은 후 fork하지말고 clone 할것

3. 바탕화면에 프로젝트 폴더 생성 & 로컬 저장소 깃 초기화

4. 로컬 저장소 .gitignore 생성

   * https://www.toptal.com/developers/gitignore/

<br>

## 1. 개발환경 설정

#### 1. 가상환경 생성 및 실행

* 가상환경 폴더를 .gitignore로 설정 해둘것

``` terminal
> python -m venv venv
> source venv(가상환경폴더 이름)/bin/activate
```

<br>

#### 2. Django 설치 및 기록

``` terminal
> pip install django==3.2.13 # Django LTS 버전
> pip install django-bootstrap5 # 부트스트랩 사용
> pip install Pillow # 이미지 업로드 시 이미지를 관리하기 위해서 설치
> pip install pilkit 
> pip install django-imagekit
> pip freeze > requirements.txt # requirements에 설치한것들을 기록
```

<br>

#### 3. Django 프로젝트 생성

``` terminal
> django-admin startproject pjt(프로젝트 폴더 명) . # .은 현재 경로에 생성한다는 의미
```

<br>

#### 4. Django 실행 확인

``` terminal
> python manage.py runserver
```

<br>

## 2. 애플리케이션 폴더 생성

#### 1. app 생성 및 실행

``` python
> python manage.py startapp accounts(앱 이름)
> python manage.py startapp reviews(앱 이름)
```

<br>

#### 2. app 등록

* setting.py 파일의 INSTALLED_APPS에 추가

``` python
INSTALLED_APPS = [
    'accounts',
  	'reviews',
    'django_bootstrap5', # 부트스트랩 사용시 추가해야함
		...
]
```

<br>

## 3. Model 정의(DB설계)

#### 1. 클래스 정의

#### accounts > models.py

``` python
# Django에서는 User모델을 기본적으로 제공한다.
# Django는 새 프로젝트를 시작하는 경우 비록 기본 User모델이 충분 하더라도 커스텀 모델을 성정하는 것을 강력하게 권장한다. 
# -> 커스텀 User모델은 기본 User 모델과 동일하게 작동 하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    @property
    def full_name(self):
        return f'{self.last_name}{self.first_name}'
```

<br>

#### reviews > models.py

``` python
from email.policy import default
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail
from django.db import models
from django.conf import settings

# 1. 모델 설계 (DB 스키마 설계)
class Review(models.Model):
    title = models.CharField(max_length=20)
    moviename = models.CharField(max_length=20, null=False)
    content = models.TextField(null=False)
    grade = models.FloatField(null=False, default=0)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Review, on_delete=models.CASCADE)
    # user는 settings.AUTH_USER_MODEL에 정의된 accounts앱에 user 클래스
    # 역참조해서 사용 : user.comment_set.all()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, null=True)
```



#### 2. settings.py 설정 추가

``` python
AUTH_USER_MODEL = 'accounts.User'
```

<br>

#### 3. 마이그레이션 파일 생성

* app 폴더 내의 `migrations` 폴더에 생성된 파일 확인

```bash
> python manage.py makemigrations
```

<br>

#### 4. DB 반영(`migrate`)

```bash
> python manage.py migrate
```

<br>

## 4. form.py 설정

app 폴더에 forms.py 파일 생성

``` python
from django.contrib.auth.forms import UserCreationForm # UserCreationForm을 상속받아서 CustomUserCreationForm 생성
from django.contrib.auth import get_user_model 

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', )
```

<br>

## 5. urls.py, templates 설정

> app 단위의 URL관리를 하기 위한 설정

#### 1. pjt 폴더 > urls.py

``` python
from django.contrib import admin
from django.urls import path, include # include 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('reviews/', include('reviews.urls')),
]

```

<br>

#### 2. accounts(app 폴더) > urls.py 생성

``` python
from django.urls import path 
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
]
```

<br>

#### 2-1 reviews(app 폴더) > urls.py 생성

``` python
from django.urls import path 
from . import views

app_name = 'reviews'

urlpatterns = [
  path('', views.index, name='index'),
]
```

<br>

#### 3. templates 폴더 생성

#### pjt 폴더 > templates 폴더 생성 > base.html 생성

* 모든 페이지에 적용되는 베이스 페이지

``` html
{% load django_bootstrap5 %}
{% load static %}

<!DOCTYPE html>
<html lang="ko">

  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BobMovie</title>
    <style>
      @font-face {
        font-family: "NetflixSans";
        src: url("fonts/NetflixSans-Regular.woff2") format("woff2");
        font-weight: normal;
        font-style: normal;
      }

      * {
        font-family: 'NetflixSans';
      }

      .nav-logo {
        width: 5rem;
        object-fit: cover;
      }

      a {
        text-decoration: none;
        color: inherit;
      }
    </style>
    {% bootstrap_css %}
    {% block css %}
      <link rel="stylesheet" href="{% static 'css/movie.css' %}">
    {% endblock css %}

  </head>

  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="nav mx-1">
        <a href="{% url 'reviews:index' %}"><img class="nav-logo mx-1" src="https://user-images.githubusercontent.com/66688033/193211411-15f19a4c-d81f-409c-955a-ec224c8671be.png"/></a>
      </div>
      <button class="navbar-toggler mx-3" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <!-- 두 항목을 오른쪽으로 밀기 .me-auto -->
        <!-- .navbar-nav으로 full-height와 보다 가벼운 네비게이션(드롭다운을 위한 지원 포함)을 실현. -->
        <ul class="navbar-nav mb-2 mx-3 mb-lg-0 ms-lg-4 align-items-end">
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'reviews:index' %}">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Community</a>
          </li>
          {% if request.user.is_authenticated %} 
            <li class="nav-item">
              <a class="nav-link" href="{% url 'accounts:logout' %}">Logout</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" style="color:white;" href="#">{{ request.user }}님, 환영합니다.</a>
              {% comment %} {% url 'movie:detail' user.pk %} {% endcomment %}
            </li>
          {% else %}
            <li class="nav-item">
              <a class="nav-link" href="{% url 'accounts:signup' %}">Join</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'accounts:login' %}">Login</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" style="color:white;">로그인 해주세요</a>
            </li> 
          {% endif %}
        </ul>
      </div>
    </nav>
    {% block body %}{% endblock body %}
    <footer class="py-3 bg-dark col-12 position-fixed bottom-0">
      <div class="container px-4 px-lg-5">
        <p class="m-0 text-center text-white">Web Bootstrap PROJ. by 최준혁</p>
      </div>
    </footer>
    {% bootstrap_javascript %}
  </body>

</html>
```

<br>

#### 4. accounts(앱 폴더) > templates 폴더 생성 > accounts 폴더 생성

accounts > signup.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
<h1>회원가입</h1>
<form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% bootstrap_button button_type="submit" content="OK" %}
</form>

{% endblock body %}
```

<br>

#### 4-1. reviews(앱 폴더) > templates 폴더 생성 > reviews 폴더 생성

reviews > index.html

``` html
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block body %}
  <!-- carousel -->
  <div id="carouselExampleControls" class="carousel slide bg-dark" data-bs-ride="carousel">
    <!-- inner -->
    <div class="carousel-inner">
      <!-- 1 -->
      <div class="carousel-item active">
        <img src="{% static 'images/carousel4.jpg' %}" class="d-block w-100 opacity-50" alt="...">
        <div class="carousel-caption">
          <h2 class="fw-bold">세계의 영화를 한곳에.</h2>
          <p>모든 영화들이 이곳에 있습니다</p>
        </div>
      </div>
      <!-- 2 -->
      <div class="carousel-item">
        <img src="{% static 'images/carousel3.jpg' %}" class="d-block w-100 opacity-50" alt="...">
        <div class="carousel-caption">
          <h2 class="fw-bold">당신의 취향에 맞는<br>시리즈 추천.</h2>
          <p></p>
        </div>
      </div>
      <!-- 3 -->
      <div class="carousel-item">
        <img src="{% static 'images/carousel1.jpg' %}" class="d-block w-100 opacity-50" alt="...">
        <div class="carousel-caption">
          <h2 class="fw-bold">다양한 영화 리뷰를 하나로.</h2>
          <p>다양한 유저들과 소통하고 평점을 매겨보세요</p>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>

  <!-- 포스터 섹션 -->
  <section class="py-5 px-5">
    <div class="text-center mb-5">
      <h2 class="fw-bold">Boxoffice</h2>
    </div>
    <div class="row row-cols-lg-3 row-cols-md-2 row-cols-sm-1 row-cols-xs-1 gx-4">
      <div class="col mb-5">
        <div class="card h-100">
          <a href="https://www.themoviedb.org/movie/278-the-shawshank-redemption?language=ko"><img class="card-img-top" src="{% static 'images/movie1.jpg' %}" alt="..."/></a>
          <div class="card-body py-4">
            <div class="text-center">
              <h5 class="fw-bold">쇼생크 탈출</h5>
            </div>
            <p class="d-flex justify-content-center mb-0">평점 : 9.88
            </p>
            <div class="d-flex justify-content-center text-warning mb-2">
              <div class="bi-star-fill"></div>
              <div class="bi-star-fill"></div>
              <div class="bi-star-fill"></div>
              <div class="bi-star-fill"></div>
              <div class="bi-star-fill"></div>
            </div>
          </div>
          <div class="card-footer bg-light p-4 pt-0 border-top-0 bg-transparent">
            <div class="text-center">
              <a class="btn btn-outline-dark" href="http://www.cgv.co.kr/ticket/">지금 예매하기</a>
            </div>
          </div>
        </div>
      </div>
      <div class="col mb-5">
        <div class="card h-100">
          <a href="https://www.themoviedb.org/movie/207-dead-poets-society?language=ko"><img class="card-img-top" src="{% static 'images/movie2.jpg' %}" alt="..."/></a>
          <div class="card-body py-4">
            <div class="text-center">
              <h5 class="fw-bold">죽은 시인의 사회</h5>
              <p class="d-flex justify-content-center mb-0">평점 : 9.56
              </p>
              <div class="d-flex justify-content-center text-warning mb-2">
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
              </div>
            </div>
          </div>
          <div class="card-footer bg-light p-4 pt-0 border-top-0 bg-transparent">
            <div class="text-center">
              <a class="btn btn-outline-dark" href="http://www.cgv.co.kr/ticket/">지금 예매하기</a>
            </div>
          </div>
        </div>
      </div>
      <div class="col mb-5">
        <div class="card h-100">
          <a href="https://www.themoviedb.org/movie/49026-the-dark-knight-rises?language=ko"><img class="card-img-top" src="{% static 'images/movie3.jpg' %}" alt="..."/></a>
          <div class="card-body py-4">
            <div class="text-center">
              <h5 class="fw-bold">다크 나이트 라이즈</h5>
              <p class="d-flex justify-content-center mb-0">평점 : 9.56
              </p>
              <div class="d-flex justify-content-center text-warning mb-2">
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
              </div>
            </div>
          </div>
          <div class="card-footer bg-light p-4 pt-0 border-top-0 bg-transparent">
            <div class="text-center">
              <a class="btn btn-outline-dark" href="http://www.cgv.co.kr/ticket/">지금 예매하기</a>
            </div>
          </div>
        </div>
      </div>
      <div class="col mb-5">
        <div class="card h-100">
          <a href="https://www.themoviedb.org/movie/120467-the-grand-budapest-hotel?language=ko"><img class="card-img-top" src="{% static 'images/movie4.jpg' %}" alt="..."/></a>
          <div class="card-body py-4">
            <div class="text-center">
              <h5 class="fw-bold">그랜드 부다페스트 호텔</h5>
              <p class="d-flex justify-content-center mb-0">평점 : 8.71
              </p>
              <div class="d-flex justify-content-center text-warning mb-2">
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-half"></div>
              </div>
            </div>
          </div>
          <div class="card-footer bg-light p-4 pt-0 border-top-0 bg-transparent">
            <div class="text-center">
              <a class="btn btn-outline-dark" href="http://www.cgv.co.kr/ticket/">지금 예매하기</a>
            </div>
          </div>
        </div>
      </div>
      <div class="col mb-5">
        <div class="card h-100">
          <a href="https://www.themoviedb.org/movie/152601-her?language=ko"><img class="card-img-top" src="{% static 'images/movie5.jpg' %}" alt="..."/></a>
          <div class="card-body py-4">
            <div class="text-center">
              <h5 class="fw-bold">그녀</h5>
              <p class="d-flex justify-content-center mb-0">평점 : 8.70
              </p>
              <div class="d-flex justify-content-center text-warning mb-2">
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-half"></div>
              </div>
            </div>
          </div>
          <div class="card-footer bg-light p-4 pt-0 border-top-0 bg-transparent">
            <div class="text-center">
              <a class="btn btn-outline-dark" href="http://www.cgv.co.kr/ticket/">지금 예매하기</a>
            </div>
          </div>
        </div>
      </div>
      <div class="col mb-5">
        <div class="card h-100">
          <a href="https://www.themoviedb.org/movie/316029-the-greatest-showman?language=ko"><img class="card-img-top" src="{% static 'images/movie6.jpg' %}" alt="..."/></a>
          <div class="card-body py-4">
            <div class="text-center">
              <h5 class="fw-bold">위대한 쇼맨</h5>
              <p class="d-flex justify-content-center mb-0">평점 : 9.31
              </p>
              <div class="d-flex justify-content-center text-warning mb-2">
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
              </div>
            </div>
          </div>
          <div class="card-footer bg-light p-4 pt-0 border-top-0 bg-transparent">
            <div class="text-center">
              <a class="btn btn-outline-dark" href="http://www.cgv.co.kr/ticket/">지금 예매하기</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

{% endblock %}
```

<br>

#### 5. settings.py  TEMPLATES에 추가

````python
import os

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "review_pjt" / "templates"], # DIRS에 경로 등록
        "APP_DIRS": True,
				...
    }
      ]

# Media files (user uploaded filed)

MEDIA_ROOT = BASE_DIR / 'images'
MEDIA_URL = '/media/'

# 정적 파일 관리
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'config', 'static') # 추가
]

````

<br>

## 6. 회원가입

#### 1. accounts > urls.py

``` python
urlpatterns = [
  path('signup/', views.signup, name='signup'),
]
```

<br>

#### 2. views.py

``` python
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 폼이 유효하면
            user = form.sava()
            auth_login(request, user)
            return redirect('reviews:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

<br>

#### 3. accounts > signup.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
  <h1>회원가입</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% bootstrap_button button_type="submit" content="OK" %}
    {% comment %}  {% endcomment %}
  </form>
{% endblock body %}
```

<br>

## 7. 로그인

#### 1. accounts > urls.py

``` python
from django.urls import path 
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
]
```

<br>

#### 2. views.py 

``` python
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        # AuthenticationForm은 ModelForm이 아님!
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'reviews:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)
```

<br>

#### 3. accounts > login.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
  <h1>로그인</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% bootstrap_button button_type="submit" content="OK" %}
    {% comment %}  {% endcomment %}
  </form>
{% endblock body %}
```

<br>

## 8. 로그아웃

#### 1. accounts > urls.py

``` python
from django.urls import path 
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
]
```

<br>

#### 2. views.py

``` python
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

def logout(request):
    auth_logout(request)
    messages.warning(request, '로그아웃 하였습니다.')
    return redirect('reviews:index')
```

<br>

## 9. 리뷰 작성 

#### 1. Model 정의(DB설계)

reviews > models.py 

``` python
from email.policy import default
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail
from django.db import models
from django.conf import settings

# 1. 모델 설계 (DB 스키마 설계)
class Review(models.Model):
    title = models.CharField(max_length=20)
    moviename = models.CharField(max_length=20, null=False)
    content = models.TextField(null=False)
    grade = models.FloatField(null=False, default=0)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")
```

<br>

#### 2. terminal

``` terminal
> python manage.py makemigrations
> python manage.py migrate
```

<br>

#### 3. reviews > forms.py 생성

``` python
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'movie_name', 'content', 'grade', 'image', 'image_thumbnail']
```

<br>

#### 4. reviews > urls.py

``` python
from django.urls import path 
from . import views

app_name = 'reviews'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
]
```

<br>

#### 5. views.py

``` python
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm

@login_required
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('reviews:index') # 목록 조회기능 구현 후 변경
    else: 
        review_form = ReviewForm()
    context = {
        'review_form': review_form
    }
    return render(request, 'reviews/create.html', context=context)
```

<br>

#### 6. reviews > create.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}

<div class="container mt-3">
{% if request.resolver_match.url_name == 'create' %}
  <h1> 글쓰기 </h1>
  {% else %}
  <h1> 수정하기 </h1>
  {% endif %}

  <form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {% bootstrap_form review_form %}
    {% bootstrap_button button_type="submit" content="OK" %}
    {% comment %}  {% endcomment %}
  </form>
</div>
{% endblock %}
```

<br>

## 10. 리뷰 목록 조회

#### 1. reviews > urls.py

``` python
from django.urls import path 
from . import views

app_name = 'reviews'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('community/', views.community, name='community'),
]
```

<br>

#### 2. views.py

``` python
def community(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/community.html', context)
```

<br>

#### 3. reviews > community.html

``` html
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block body %}
<div class="container mt-3">
  <h1>게시판</h1>
  <div class="row">
    {% for review in reviews %}
      <div class="col-4">
        <div class="card">
          {% if article.image_thumbnail %}
            <img src="{{ review.image_thumbnail.url }}" class="card-img-top" alt="...">
          {% else %}
            <img src="https://dummyimage.com/1200x960/000000/c4c4c4" class="card-img-top">
          {% endif %}
          <div class="card-body">
            <h5 class="card-title">{{ review.title }}</h5>
            <p class="text-muted">{{ review.user.username }}</p>
            <a href="#" class="btn btn-outline-primary my-3">상세보기</a>
            {% comment %} {% url 'reviews:detail' review.pk %} {% endcomment %}
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
  {% if request.user.is_authenticated %}
  <a class="btn btn-outline-primary my-3 float-right" href="{% url 'reviews:create' %}">글 쓰기</a>
{% endif %}
</div>
{% endblock %}
```

<br>

## 11. 리뷰 세부 정보 조회

#### 1. reviews > urls.py

``` python
from django.urls import path 
from . import views

app_name = 'reviews'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('community/', views.community, name='community'),
  path('detail/<int:pk>', views.detail, name='detail'),
]
```

<br>

#### 2. views.py

``` python
def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review': review
    }
    return render(request, 'reviews/detail.html', context)
```

<br>

#### 3. reviews > detail.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}


{% block body %}
<div class="container mt-3 mb-3">
  <h1>{{ review.title }}</h1>
  <hr>
  <span>{{ review.pk }}번 게시글</span><br>
  <span>작성자: <a href="#">{{ review.user.username }}</a></span><br>
  <span>작성일자: {{ review.created_at|date:"SHORT_DATETIME_FORMAT" }} | 수정일자: {{ review.updated_at|date:"y-m-d D" }}</span><br>
  {% if request.user.is_authenticated %}
    {% if request.user in review.like_users.all %}
      <i id="like-btn"  data-article-id="{{ review.pk }}" class="bi bi-heart-fill"></i>
    {% else %}
      <i id="like-btn" data-article-id="{{ review.pk }}" class="bi bi-heart"></i>
    {% endif %}
  {% endif %}
  <span id="like-count">{{ review.like_users.count }}</span>
  <div class="mb-3 mt-3">
    <label for="reviewContent" class="form-label">내용</label><br>
    {% if review.image %}
    <img class="mb-2" src="{{ review.image.url }}" alt="{{ review.image }}" width="400" height="300">
    {% endif %}  
    <textarea name='content' class="form-control" id="reviewContent" rows="3" readonly="readonly">{{ review.content }}
    </textarea>
  </div>

  {% if request.user == review.user %}
  <div>
  <a class="btn btn-outline-primary my-3" href="#">수정하기</a>
  <a class="btn btn-outline-danger my-3" href="#">삭제하기</a>
  </div>
  {% endif %}
  <h4 class="my-3">댓글</h4>
  {% if request.user.is_authenticated %}
  <form id="comment-form" data-article-id="{{ article.pk }}">
    {% csrf_token %}
    {% comment %} {% bootstrap_form comment_form layout='inline' %}
    {% bootstrap_button button_type="submit" content="OK" %} {% endcomment %}
    {% comment %}  {% endcomment %}
  </form>
  {% endif %}
  <hr>
  <p>총 {{ comments.count }}개의 댓글이 있습니다.</p>
  <div id="comments">
    {% for comment in comments %}
      <p>{{ comment.user.username }} | {{ comment.content }}</p>
      <form action="#" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
      <hr>
      {% empty %}
      <p>댓글이 없어요 ㅠ_ㅠ</p>
    {% endfor %}
  </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  // (1) 좋아요 버튼
  const likeBtn = document.querySelector('#like-btn')
  // (2) 좋아요 버튼을 클릭하면, 함수 실행
  likeBtn.addEventListener('click', function(event){
    // 서버로 비동기 요청을 하고싶음
    console.log(event.target.dataset)
    axios({
      method: 'get',
      url: `/articles/${event.target.dataset.articleId}/like/`
    })
    .then(response => {
      console.log(response)
      console.log(response.data)
      if (response.data.isLiked === true ) {
        event.target.classList.add('bi-heart-fill')
        event.target.classList.remove('bi-heart')
      } else {
        event.target.classList.add('bi-heart')
        event.target.classList.remove('bi-heart-fill')       
      }
      const likeCount = document.querySelector('#like-count')
      likeCount.innerText = response.data.likeCount
    })
  })
</script>
<script>
  // 1. form을 작성
  const commentForm = document.querySelector('#comment-form')
  // 2. 제출하면, 함수 실행
  // csrf
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  commentForm.addEventListener('submit', function(event) {
    event.preventDefault();
    axios({
      method: 'post',
      url: `/articles/${event.target.dataset.articleId}/comments/`,
      headers: { "X-CSRFToken": csrftoken },
      data: new FormData(commentForm) // 폼에 있는 정보를 data로 넘겨줄 수 있도록 변환
    })
    .then(response => {
      console.log(response.data)
      const comments = document.querySelector('#comments')
      const p = document.createElement('p')
      p.innerText = `${response.data.userName} | ${response.data.content}`
      const hr = document.createElement('hr')
      comments.append(p, hr)
      //comments.insertAdjacentHTML('beforeend', ' 
      //<p> ${response.data.userName} | ${response.data.content}</p>
      //<hr>
      //')
      commentForm.reset()
    })
  })
</script>
{% endblock %}
```

<br>

## 12. 리뷰 정보 수정

#### 1. reviews > urls.py

``` python
from django.urls import path 
from . import views

app_name = 'reviews'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('community/', views.community, name='community'),
  path('detail/<int:pk>', views.detail, name='detail'),
  path('update/<int:pk>', views.update, name='update'),
]
```

<br>

#### 2. views.py

``` python
@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:

        if request.method == 'POST':
            # POST : input 값 가져와서, 검증하고, DB에 저장
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
                review_form.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('reviews:detail', review.pk)
            # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
        else:
            # GET : Form을 제공
            review_form = ReviewForm(instance=review)
        context = {
            'review_form': review_form
        }
        return render(request, 'reviews/create.html', context)
```

<br>

#### 3. reviews > create.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
<div class="container mt-3">
{% if request.resolver_match.url_name == 'create' %}
  <h1> 글쓰기 </h1>
  {% else %}
  <h1> 수정하기 </h1>
  {% endif %}

  <form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {% bootstrap_form review_form %}
    {% bootstrap_button button_type="submit" content="OK" %}
    {% comment %}  {% endcomment %}
  </form>
</div>
{% endblock %}
```

<br>

## 13. 리뷰 삭제

#### 1. reviews > urls.py

``` python
from django.urls import path 
from . import views

app_name = 'reviews'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('community/', views.community, name='community'),
  path('detail/<int:pk>', views.detail, name='detail'),
  path('update/<int:pk>', views.update, name='update'),
  path('delete/<int:pk>', views.delete, name='delete'),
]
```

<br>

#### 2. views.py

``` python
def delete(request, pk):
    get_object_or_404(Review, pk=pk).delete()
    return redirect('reviews:community')
```

<br>

## 14. 댓글 작성

#### 1. Model 정의(DB 설계)

reviews > models.py

``` python
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Review, on_delete=models.CASCADE)
    # user는 settings.AUTH_USER_MODEL에 정의된 accounts앱에 user 클래스
    # 역참조해서 사용 : user.comment_set.all()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
```

<br>

#### terminal

``` terminal
> python manage.py makemigrations
> python manage.py migrate
```

<br>

#### 2. reviews > forms.py

``` python
from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'moviename', 'content', 'grade', 'image', 'image_thumbnail']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
```

<br>

#### 3. reviews > urls.py

``` python
from django.urls import path 
from . import views

app_name = 'reviews'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('community/', views.community, name='community'),
  path('detail/<int:pk>', views.detail, name='detail'),
  path('update/<int:pk>', views.update, name='update'),
  path('delete/<int:pk>', views.delete, name='delete'),
  path('comments/<int:pk>', views.comment_create, name='comment_create'),
]
```

<br>

#### 4. views.py

``` python
from .forms import ReviewForm, CommentForm

@login_required
def comment_create(request, pk):
    print(request.POST)
    article = get_object_or_404(Review, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment_form.save() # 모델 인스턴스의 save()
        context = {
            'content': comment.content,
            'userName': comment.user.username
        }
    return JsonResponse(context)
```

<br>

#### 5. reviews > detail.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
  <div class="container mt-3 mb-3">
    <h1>{{ review.title }}</h1>
    <hr>
    <span>{{ review.pk }}번 게시글</span><br>
    <span>작성자:
      <a href="#">{{ review.user.username }}</a>
    </span><br>
    <span>작성일자:
      {{ review.created_at|date:"SHORT_DATETIME_FORMAT" }}
      | 수정일자:
      {{ review.updated_at|date:"y-m-d D" }}</span><br>
    {% if request.user.is_authenticated %}
      {% if request.user in review.like_users.all %}
        <i id="like-btn" data-article-id="{{ review.pk }}" class="bi bi-heart-fill"></i>
      {% else %}
        <i id="like-btn" data-article-id="{{ review.pk }}" class="bi bi-heart"></i>
      {% endif %}
    {% endif %}
    <span id="like-count">{{ review.like_users.count }}</span>
    <div class="mb-3 mt-3">
      <label for="reviewContent" class="form-label">내용</label><br>
      {% if review.image %}
        <img class="mb-2" src="{{ review.image.url }}" alt="{{ review.image }}" width="400" height="300">
      {% endif %}
      <textarea name='content' class="form-control" id="reviewContent" rows="3" readonly="readonly">{{ review.content }}
      </textarea>
    </div>

    {% if request.user == review.user %}
      <div>
        <a class="btn btn-outline-primary my-3" href="{% url 'reviews:update' review.pk %}">수정하기</a>
        <a class="btn btn-outline-danger my-3" href="{% url 'reviews:delete' review.pk %}">삭제하기</a>
      </div>
    {% endif %}
    <hr>
    <!-- 댓글 부분 -->
    <h4 class="my-3">댓글</h4>
    {% if request.user.is_authenticated %}
    <form id="comment-form" data-article-id="{{ review.pk }}" >
      {% csrf_token %}
      <div class="mb-2">
        <input name='content' class="form-control" id="comment_form" rows="3"></input>
      </div>
      {% bootstrap_button button_type="submit" content="OK" %}
      {% comment %}  {% endcomment %}
    </form>
    {% endif %}
    <hr>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 1. form을 작성
    const commentForm = document.querySelector('#comment-form')
    // 2. 제출하면, 함수 실행
    // csrf
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    commentForm.addEventListener('submit', function (event) {
        event.preventDefault();
        axios({
          method: 'post',
          url: `/reviews/comments/${event.target.dataset.articleId}`,
          headers: {
            "X-CSRFToken": csrftoken
          },
          data: new FormData(commentForm) // 폼에 있는 정보를 data로 넘겨줄 수 있도록 변환
        }).then(response => {
          console.log(response.data)
          const comments = document.querySelector('#comments')
          const p = document.createElement('p')
          p.innerText = `${response.data.userName} | ${response.data.content}`
          const hr = document.createElement('hr')
          comments.append(p, hr)
          //comments.insertAdjacentHTML('beforeend', '
          //<p> ${response.data.userName} | ${response.data.content}</p>
          //<hr>
          //')
          commentForm.reset()
        })
      })
  </script>
{% endblock %}
```

<br>

## 15. 댓글 목록 출력

#### 1. reviews > views.py 

* 기존 detail 수정

``` python
def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review': review,
        'comment': review.comment_set.all(),
        }
    return render(request, 'reviews/detail.html', context)
```

<br>

#### 2. reviews > detail.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
  <div class="container mt-3 mb-3">
    <h1>{{ review.title }}</h1>
    <hr>
    <span>{{ review.pk }}번 게시글</span><br>
    <span>작성자:
      <a href="#">{{ review.user.username }}</a>
    </span><br>
    <span>작성일자:
      {{ review.created_at|date:"SHORT_DATETIME_FORMAT" }}
      | 수정일자:
      {{ review.updated_at|date:"y-m-d D" }}</span><br>
    {% if request.user.is_authenticated %}
      {% if request.user in review.like_users.all %}
        <i id="like-btn" data-article-id="{{ review.pk }}" class="bi bi-heart-fill"></i>
      {% else %}
        <i id="like-btn" data-article-id="{{ review.pk }}" class="bi bi-heart"></i>
      {% endif %}
    {% endif %}
    <span id="like-count">{{ review.like_users.count }}</span>
    <div class="mb-3 mt-3">
      <label for="reviewContent" class="form-label">내용</label><br>
      {% if review.image %}
        <img class="mb-2" src="{{ review.image.url }}" alt="{{ review.image }}" width="400" height="300">
      {% endif %}
      <textarea name='content' class="form-control" id="reviewContent" rows="3" readonly="readonly">{{ review.content }}
      </textarea>
    </div>

    {% if request.user == review.user %}
      <div>
        <a class="btn btn-outline-primary my-3" href="{% url 'reviews:update' review.pk %}">수정하기</a>
        <a class="btn btn-outline-danger my-3" href="{% url 'reviews:delete' review.pk %}">삭제하기</a>
      </div>
    {% endif %}
    <hr>
    <!-- 댓글 부분 -->
    <h4 class="my-3">댓글</h4>
    {% if request.user.is_authenticated %}
    <form id="comment-form" data-article-id="{{ review.pk }}" >
      {% csrf_token %}
      <div class="mb-2">
        <input name='content' class="form-control" id="comment_form" rows="3"></input>
      </div>
      {% bootstrap_button button_type="submit" content="OK" %}
      {% comment %}  {% endcomment %}
    </form>
    {% endif %}
    <hr>
    <p>총 {{ comment.count }}개의 댓글이 있습니다.</p>
    <div id="comments">
      {% for comment in comment %}
        <p>{{ comment.user.username }} | {{ comment.content }}</p>
        <form action="#" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
        <hr>
        {% empty %}
        <p>댓글이 없어요 ㅠ_ㅠ</p>
      {% endfor %}
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 1. form을 작성
    const commentForm = document.querySelector('#comment-form')
    // 2. 제출하면, 함수 실행
    // csrf
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    commentForm.addEventListener('submit', function (event) {
        event.preventDefault();
        axios({
          method: 'post',
          url: `/reviews/comments/${event.target.dataset.articleId}`,
          headers: {
            "X-CSRFToken": csrftoken
          },
          data: new FormData(commentForm) // 폼에 있는 정보를 data로 넘겨줄 수 있도록 변환
        }).then(response => {
          console.log(response.data)
          const comments = document.querySelector('#comments')
          const p = document.createElement('p')
          p.innerText = `${response.data.userName} | ${response.data.content}`
          const hr = document.createElement('hr')
          comments.append(p, hr)
          //comments.insertAdjacentHTML('beforeend', '
          //<p> ${response.data.userName} | ${response.data.content}</p>
          //<hr>
          //')
          commentForm.reset()
        })
      })
  </script>
{% endblock %}
```

 <br>

## 16. 댓글 삭제

#### 1. reviews > urls.py

``` python
from django.urls import path 
from . import views

app_name = 'reviews'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('community/', views.community, name='community'),
  path('detail/<int:pk>', views.detail, name='detail'),
  path('update/<int:pk>', views.update, name='update'),
  path('delete/<int:pk>', views.delete, name='delete'),
  path('comments/<int:pk>', views.comment_create, name='comment_create'),
  path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
```

<br>

#### 2. views.py

``` python
def comment_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)
```

<br>

#### 3. reviews > detail.py

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
  <div class="container mt-3 mb-3">
    <h1>{{ review.title }}</h1>
    <hr>
    <span>{{ review.pk }}번 게시글</span><br>
    <span>작성자:
      <a href="#">{{ review.user.username }}</a>
    </span><br>
    <span>작성일자:
      {{ review.created_at|date:"SHORT_DATETIME_FORMAT" }}
      | 수정일자:
      {{ review.updated_at|date:"y-m-d D" }}</span><br>
    {% if request.user.is_authenticated %}
      {% if request.user in review.like_users.all %}
        <i id="like-btn" data-article-id="{{ review.pk }}" class="bi bi-heart-fill"></i>
      {% else %}
        <i id="like-btn" data-article-id="{{ review.pk }}" class="bi bi-heart"></i>
      {% endif %}
    {% endif %}
    <span id="like-count">{{ review.like_users.count }}</span>
    <div class="mb-3 mt-3">
      <label for="reviewContent" class="form-label">내용</label><br>
      {% if review.image %}
        <img class="mb-2" src="{{ review.image.url }}" alt="{{ review.image }}" width="400" height="300">
      {% endif %}
      <textarea name='content' class="form-control" id="reviewContent" rows="3" readonly="readonly">{{ review.content }}
      </textarea>
    </div>

    {% if request.user == review.user %}
      <div>
        <a class="btn btn-outline-primary my-3" href="{% url 'reviews:update' review.pk %}">수정하기</a>
        <a class="btn btn-outline-danger my-3" href="{% url 'reviews:delete' review.pk %}">삭제하기</a>
      </div>
    {% endif %}
    <hr>
    <!-- 댓글 부분 -->
    <h4 class="my-3">댓글</h4>
    {% if request.user.is_authenticated %}
    <form id="comment-form" data-article-id="{{ review.pk }}" >
      {% csrf_token %}
      <div class="mb-2">
        <input name='content' class="form-control" id="comment_form" rows="3"></input>
      </div>
      {% bootstrap_button button_type="submit" content="OK" %}
      {% comment %}  {% endcomment %}
    </form>
    {% endif %}
    <hr>
    <p>총 {{ comment.count }}개의 댓글이 있습니다.</p>
    <div id="comments">
      {% for comment in comment %}
        <p>{{ comment.user.username }} | {{ comment.content }}</p>
        <form action="{% url 'reviews:comment_delete' review.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
        <hr>
        {% empty %}
        <p>댓글이 없어요 ㅠ_ㅠ</p>
      {% endfor %}
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 1. form을 작성
    const commentForm = document.querySelector('#comment-form')
    // 2. 제출하면, 함수 실행
    // csrf
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    commentForm.addEventListener('submit', function (event) {
        event.preventDefault();
        axios({
          method: 'post',
          url: `/reviews/comments/${event.target.dataset.articleId}`,
          headers: {
            "X-CSRFToken": csrftoken
          },
          data: new FormData(commentForm) // 폼에 있는 정보를 data로 넘겨줄 수 있도록 변환
        }).then(response => {
          console.log(response.data)
          const comments = document.querySelector('#comments')
          const p = document.createElement('p')
          p.innerText = `${response.data.userName} | ${response.data.content}`
          const hr = document.createElement('hr')
          comments.append(p, hr)
          //comments.insertAdjacentHTML('beforeend', '
          //<p> ${response.data.userName} | ${response.data.content}</p>
          //<hr>
          //')
          commentForm.reset()
        })
      })
  </script>
{% endblock %}

```

<br>

## 17. 게시글에 좋아요 하기(비동기 처리)

#### reviews > urls.py

``` python
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('community/', views.community, name='community'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('comments/<int:pk>', views.comment_create, name='comment_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('like/<int:pk>', views.like, name='like'),
]
```

<br>

#### views.py

``` python
@login_required
def like(request, pk):
  review = get_object_or_404(Review, pk=pk)
  if request.user in review.like_users.all(): 
    # 좋아요 삭제
    review.like_users.remove(request.user)
    is_liked = False
  else:
    # 좋아요 추가
    review.like_users.add(request.user)
    is_liked = True
  # 상세 페이지로 redirect
  context = {'isLiked': is_liked, 
             'likeCount': review.like_users.count(),
            }
  return JsonResponse(context)
```

<br>

#### reviews > detail.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
  <div class="container mt-3 mb-3">
    <h1>{{ review.title }}</h1>
    <hr>
    <span>{{ review.pk }}번 게시글</span><br>
    <span>작성자:
      <a href="#">{{ review.user.username }}</a>
    </span><br>
    <span>작성일자:
      {{ review.created_at|date:"SHORT_DATETIME_FORMAT" }}
      | 수정일자:
      {{ review.updated_at|date:"y-m-d D" }}</span><br>
    {% if request.user.is_authenticated %}
      {% if request.user in review.like_users.all %}
        <i id="like-btn" data-article-id="{{ review.pk }}" class="bi bi-heart-fill"></i>
      {% else %}
        <i id="like-btn" data-article-id="{{ review.pk }}" class="bi bi-heart"></i>
      {% endif %}
    {% endif %}
    <span id="like-count">{{ review.like_users.count }}</span>
    <div class="mb-3 mt-3">
      <label for="reviewContent" class="form-label">내용</label><br>
      {% if review.image %}
        <img class="mb-2" src="{{ review.image.url }}" alt="{{ review.image }}" width="400" height="300">
      {% endif %}
      <textarea name='content' class="form-control" id="reviewContent" rows="3" readonly="readonly">{{ review.content }}
      </textarea>
    </div>

    {% if request.user == review.user %}
      <div>
        <a class="btn btn-outline-primary my-3" href="{% url 'reviews:update' review.pk %}">수정하기</a>
        <a class="btn btn-outline-danger my-3" href="{% url 'reviews:delete' review.pk %}">삭제하기</a>
      </div>
    {% endif %}
    <hr>
    <!-- 댓글 부분 -->
    <h4 class="my-3">댓글</h4>
    {% if request.user.is_authenticated %}
    <form id="comment-form" data-article-id="{{ review.pk }}" >
      {% csrf_token %}
      <div class="mb-2">
        <input name='content' class="form-control" id="comment_form" rows="3"></input>
      </div>
      {% bootstrap_button button_type="submit" content="OK" %}
      {% comment %}  {% endcomment %}
    </form>
    {% endif %}
    <hr>
    <p>총 {{ comment.count }}개의 댓글이 있습니다.</p>
    <div id="comments">
      {% for comment in comment %}
        <p>{{ comment.user.username }} | {{ comment.content }}</p>
        <form action="{% url 'reviews:comment_delete' review.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
        <hr>
        {% empty %}
        <p>댓글이 없어요 ㅠ_ㅠ</p>
      {% endfor %}
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // (1) 좋아요 버튼
    const likeBtn = document.querySelector('#like-btn')
    // (2) 좋아요 버튼을 클릭하면, 함수 실행
    likeBtn.addEventListener('click', function (event) {
      // 서버로 비동기 요청을 하고싶음
      console.log(event.target.dataset)
      axios({method: 'get', url: `/reviews/like/${event.target.dataset.articleId}`}).then(response => {
        console.log(response)
        console.log(response.data)
        if (response.data.isLiked === true) {
          event
            .target
            .classList
            .add('bi-heart-fill')
          event
            .target
            .classList
            .remove('bi-heart')
        } else {
          event
            .target
            .classList
            .add('bi-heart')
          event
            .target
            .classList
            .remove('bi-heart-fill')
        }
        const likeCount = document.querySelector('#like-count')
        likeCount.innerText = response.data.likeCount
      })
    })
  </script>
  <script>
    // 1. form을 작성
    const commentForm = document.querySelector('#comment-form')
    // 2. 제출하면, 함수 실행
    // csrf
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    commentForm.addEventListener('submit', function (event) {
        event.preventDefault();
        axios({
          method: 'post',
          url: `/reviews/comments/${event.target.dataset.articleId}`,
          headers: {
            "X-CSRFToken": csrftoken
          },
          data: new FormData(commentForm) // 폼에 있는 정보를 data로 넘겨줄 수 있도록 변환
        }).then(response => {
          console.log(response.data)
          const comments = document.querySelector('#comments')
          const p = document.createElement('p')
          p.innerText = `${response.data.userName} | ${response.data.content}`
          const hr = document.createElement('hr')
          comments.append(p, hr)
          //comments.insertAdjacentHTML('beforeend', '
          //<p> ${response.data.userName} | ${response.data.content}</p>
          //<hr>
          //')
          commentForm.reset()
        })
      })
  </script>
{% endblock %}

```

<br>

## 18. 사용자 팔로우하기

#### accounts > urls.py

``` python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('follow/<int:pk>', views.follow, name='follow'),
]
```

<br>

#### views.py

``` python
@require_POST
@login_required
def follow(request, pk):
    # 프로필에 해당하는 유저를 로그인한 유저가 팔로우 할 수 없음
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user == user:
        messages.warning(request, '스스로 팔로우 할 수 없습니다.')
        return redirect('accounts:detail')
    # 팔로우 상태면, 팔로우 취소를 누르면 삭제
    if request.user in user.followings.all():
        user.followings.remove(request.user)
    else:
        # 팔로우 상태가 아니면, '팔로우'를 누르면 추가
        user.followings.add(request.user)
    return redirect('accounts:detail', pk)
```

<br>

#### detail.html

``` html
{% extends 'base.html' %}

{% block body %}
  <h1>{{ user.username }}님의 프로필</h1>
  <p>{{ user.email }}
    |
    {{ user.full_name }}
  </p>
  팔로우 :
  {{ user.followings.count }}
  | 팔로워 :
  {{ user.follower.count }}
  {% if request.user.is_authenticated %}
    {% if request.user != user %}
      {% if request.user in user.followings.all %}
        <a class="btn btn-outline-secondary" href="{% url 'accounts:follow' user.pk %}">팔로우 취소</a>
      {% else %}
        <a class="btn btn-outline-primary" href="{% url 'accounts:follow' user.pk %}">팔로우</a>
      {% endif %}
    {% endif %}
  {% endif %}
  <div class="col-6">
    <h3>작성한 글</h3>
    <p class="text-muted">{{ user.review_set.count }}개를 작성하였습니다.</p>
    {% for article in user.review_set.all %}
      <p>
        {{ forloop.counter }}
        <a href="{% url 'reviews:detail' article.pk %}">{{ article.title }}</a>
      </p>
    </div>
  {% endfor %}

  <div class="col-6">
    <h3>작성한 댓글</h3>
    <p class="text-muted">{{ user.comment_set.count }}개를 작성하였습니다.</p>
    {% for comment in user.comment_set.all %}
      <p>
        {{ forloop.counter }}
        <a href="{% url 'reviews:detail' comment.article.pk %}">{{ comment.content }}</a>
      </p>
    </div>
  {% endfor %}

{% endblock body %}

```

