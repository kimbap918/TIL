# 영화 리뷰 채널 프로젝트

## 요구사항

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야합니다.

- **CRUD** 구현

- **Staticfiles** 활용 정적 파일(이미지, CSS, JS) 다루기

- Django **Auth** 활용 회원 관리 구현

- Media 활용 동적 파일 다루기

- 모델간

   

  1 : N 관계

   

  매핑 코드 작성 및 활용

  - 유저 - 리뷰
  - 리뷰 - 댓글
  - 유저 - 댓글

## 토픽

### 깃 저장소 생성

branch master

1. 원격 저장소 생성

2. 콜라보레이터 초대

3. 로컬 저장소 깃 초기화

4. 로컬 저장소 .gitignore 생성 & 작성

   [gitignore.io](https://www.toptal.com/developers/gitignore/)

------

### 개발환경 설정

branch setup-env

1. Django 프로젝트 생성

2. 가상환경 생성 & 실행

3. 필요한 패키지 설치

4. 패키지 목록 저장

   ```bash
   pip freeze > requirements.txt
   ```

5. Django 프로젝트 생성

   ```bash
   django-admin startproject config .
   ```

------

### 회원 가입

branch account/signup

앱 App 생성

- 앱 이름 : accounts

모델 Model 작성

- 모델 이름 : User
- Django AbstractUser 모델 상속

폼 Form 작성

- Django 내장폼 UserCreationForm을 상속받은 CustomUserCreationForm 작성

기능 View

- `POST` accounts/signup/
- CustomUserCreationForm 활용

화면 Template

- `GET` accounts/signup/
- 회원가입 폼

------

### 로그인

branch accounts/login

기능 View

- `POST` accounts/signup/
- 내장 폼 AuthenticationForm 활용

화면 Template

- `GET` accounts/signup/
- 로그인 폼
- 회원가입 페이지 이동 버튼

------

### 로그아웃

branch accounts/logout

기능 View

- `POST` account/logout

------

### 리뷰 작성

branch reviews/create

앱 App 생성

앱 이름 : reviews

모델 Model 생성

모델 이름 : Review

- 모델 필드

  | 이름       | 역할          | 필드     | 속성              |
  | ---------- | ------------- | -------- | ----------------- |
  | user       | 리뷰 작성자   |          |                   |
  | title      | 리뷰 제목     |          |                   |
  | content    | 리뷰 내용     |          |                   |
  | movie_name | 영화 이름     |          |                   |
  | grade      | 영화 평점     |          |                   |
  | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
  | updated_at | 리뷰 수정시간 | DateTime | auto_now = True   |

기능 View

- `POST` reviews/create/

화면 Template

- `GET` reviews/create/
- 리뷰 작성 폼

------

### 리뷰 목록 조회

branch reviews/index

**기능 View**

- `GET` reviews/

**화면 Template**

- `GET` reviews/

------

### 리뷰 정보 조회

branch reviews/detail

**기능 View**

- `GET` reviews/[int:review_pk](int:review_pk)/

**화면 Template**

- `GET` reviews/[int:review_pk](int:review_pk)/
- 리뷰 수정 / 삭제 버튼
  - 수정 / 삭제 버튼은 해당 리뷰 작성자에게만 출력합니다.
- 댓글 작성 폼
  - 댓글 작성 폼은 로그인 사용자에게만 출력합니다.
- 댓글 목록

------

### 리뷰 정보 수정

branch reviews/update

**기능 View**

- `POST` reviews/[int:review_pk](int:review_pk)/update/
- 데이터를 생성한 사용자만 수정할 수 있습니다.

**화면 Template**

- `GET` reviews/[int:review_pk](int:review_pk)/update/
- 리뷰 수정 폼

------

### 리뷰 삭제

branch reviews/delete

**기능 View**

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/delete/
- 데이터를 생성한 사용자만 삭제할 수 있습니다.

------

### 댓글 작성

branch comments/create

reviews 앱에 구현

모델 Model 생성

모델 이름 : Comment

- 모델 필드

  | 이름    | 역할        | 필드 | 속성 |
  | ------- | ----------- | ---- | ---- |
  | review  | 참조 리뷰   |      |      |
  | user    | 댓글 작성자 |      |      |
  | content | 댓글 내용   |      |      |

기능 View

- `POST` reviews/[int:review_pk](int:review_pk)/comments/
- 로그인한 사용자만 댓글을 생성할 수 있습니다.

화면 Template

- `GET` reviews/[int:review_pk](int:review_pk)/
- 리뷰 정보 조회 페이지 하단에 댓글 작성 폼 출력

------

### 댓글 목록 조회

branch comments/index

기능 View

- `GET` reviwes/[int:review_pk](int:review_pk)/

화면 Template

- `GET` reviews/[int:review_pk](int:review_pk)/
- 리뷰 정보 조회 페이지 하단에 댓글 목록 출력

------

### 댓글 삭제

branch comments/delete

기능 View

- `POST` reviews/[int:review_pk](int:review_pk)/comments/[int:comment_pk](int:comment_pk)/delete/
- 데이터를 생성한 사용자만 삭제할 수 있습니다.

화면 Template

- `GET` reviews/[int:review_pk](int:review_pk)/
- 각 댓글에 리뷰 삭제 버튼 추가
  - 삭제 버튼은 해당 댓글 작성자에게만 출력합니다.

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

# Abstract User를 상속받아서 사용
class User(AbstractUser):
  pass
```

<br>

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
        <a href="{% url 'movie:index' %}"><img class="nav-logo mx-1" src="https://user-images.githubusercontent.com/66688033/193211411-15f19a4c-d81f-409c-955a-ec224c8671be.png"/></a>
      </div>
      <button class="navbar-toggler mx-3" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <!-- 두 항목을 오른쪽으로 밀기 .me-auto -->
        <!-- .navbar-nav으로 full-height와 보다 가벼운 네비게이션(드롭다운을 위한 지원 포함)을 실현. -->
        <ul class="navbar-nav mb-2 mx-3 mb-lg-0 ms-lg-4 align-items-end">
          <li class="nav-item">
            <a class="nav-link active" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Community</a>
          </li>
          <li class="nav-item">
            <a class='nav-link' href="#" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@mdo">Login</a>
          </li>
        </ul>
      </div>

      <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <form>
                <div class="mb-3">
                  <label for="email-address" class="col-form-label">Email address</label>
                  <input type="text" class="form-control" id="email-address">
                  <p class="text-black-50">We'll never share your email with anyone else.</p>
                </div>
                <div class="mb-3">
                  <label for="password" class="col-form-label">Password</label>
                  <input type="text" class="form-control" id="password">
                </div>
                <div class="form-check mb-3">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
                  <label class="form-check-label" for="defaultCheck1">
                    Check me out
                  </label>
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button type="button" class="btn btn-primary">Submit</button>
            </div>
          </div>
        </div>
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
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "review_pjt" / "templates"], # DIRS에 경로 등록
        "APP_DIRS": True,
				...
    }
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
from django.contrib.auth import login as auth_login # login이 겹치므로 auth_login으로 이름을 바꿔준다

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # ModelForm의 save 메서드의 리턴값은 해당 모델의 인스턴스다!
            auth_login(request, user) # 로그인
            return redirect('articles:index')
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
from django.db import models
from django.conf import settings

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30) # 리뷰 제목
    content = models.TextField(null=False) # 리뷰 내용
    movie_name = models.CharField(max_length=30) # 영화 이름
    grade = models.DecimalField(max_digits=2, decimal_places=1) # 영화 평점
    created_at = models.DateTimeField(auto_now_add=True) # 리뷰 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 리뷰 수정시간
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
        fields = ['title', 'movie_name', 'content', 'grade']
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
  <style>
    a {
      text-decoration: none;
      color: inherit;
    }
  </style>
{% endblock %}

{% block body %}
  <!-- 게시판 영역 -->
  <section class="mx-5">
    <!-- 게시판 제목 -->
    <div class="text-center my-5 mx-5">
      <a href="{% url 'reviews:community' %}">
        <h1>Community</h1>
      </a>
    </div>
    <!-- 게시판 내용 -->
    <div class="row">
      <!-- 테이블 헤더 -->
      <div class="col-lg-3 col-md-12 px-5 mb-3">
        <ul class="list-group">
          <li class="list-group-item">
            <a class="text-decoration-none" href="#">Boxoffice</a>
          </li>
          <li class="list-group-item">
            <a class="text-decoration-none" href="#">Movies</a>
          </li>
          <li class="list-group-item">
            <a class="text-decoration-none" href="#">Genres</a>
          </li>
          <li class="list-group-item">
            <a class="text-decoration-none" href="#">Actors</a>
          </li>
        </ul>
      </div>
      <div class="col-lg-9 col-md-12 px-5 mb-3">
        <!-- 테이블 영역 -->
        <table class="table">
          <!-- 테이블 헤드 -->
          <thead class="table-light">
            <tr>
              <th scope="col">순번</th>
              <th scope="col">리뷰 제목</th>
              <th scope="col">영화 이름</th>
            </tr>
          </thead>
          <!-- 테이블 바디 -->
          <tbody class="table-group-divider">
            {% for review in reviews %}
              <tr>
                <th>{{ review.pk }}</th>
                <th>
                  <a href="#">{{ review.title }}</a>
                  {% comment %} {% url 'movie:review_detail' review.pk %} {% endcomment %}
                </th> 
                <th>{{ review.movie_name }}</th>
              </tr>
            {% endfor %}
          </tbody>
        </table>
        <div class="col-12">
          <form action="{% url 'reviews:create' %}">
            <button class="btn btn-outline-primary">리뷰작성</button>
          </form>
        </div>
      </div>
    </div>
  </section>
  <nav class="mt-2 mb-2" aria-label="Page navigation example">
    <ul class="pagination justify-content-center">
      <li class="page-item">
        <a class="page-link" href="#">Previous</a>
      </li>
      <li class="page-item">
        <a class="page-link" href="#">1</a>
      </li>
      <li class="page-item">
        <a class="page-link" href="#">2</a>
      </li>
      <li class="page-item">
        <a class="page-link" href="#">3</a>
      </li>
      <li class="page-item">
        <a class="page-link" href="#">Next</a>
      </li>
    </ul>
  </nav>

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
  review = Review.objects.get(pk=pk)
  context = {
    'review': review
    }
  return render(request, 'reviews/detail.html', context)
```

<br>

#### 3. reviews > detail.html

``` html
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block body %}
  <form class="container mt-3">
    <h1>{{ review.title }}</h1>
    <span>작성시간 :
      {{ review.created_at }}
      | 수정시간 :
      {{ review.updated_at }}</span>
    <div class="mb-3 mt-3">
      <label for="reviewContent" class="form-label">내용</label>
      <textarea name='content' class="form-control" id="reviewContent" rows="3" disabled="disabled" readonly="readonly">{{ review.content }}</textarea>
    </div>
    <div class="mb-3">
      <label for="moviename" class="form-label">영화 제목</label>
      <textarea name='content' class="form-control" id="moviename" rows="3" disabled="disabled" readonly="readonly">{{ review.movie_name }}</textarea>
    </div>
    <div class="mb-3">
      <label for="reviewgrade" class="form-label">평점</label>
      <textarea name='content' class="form-control" id="reviewgrade" rows="3" disabled="disabled" readonly="readonly">{{ review.grade }}</textarea>
    </div>
    <!-- 로그인 한 해당유저만 수정 및 삭제 가능하게 변경 -->
    {% if request.user == review.user %}
    <div>
    <a class="btn btn-outline-primary my-3" href="#">수정하기</a>
    <a class="btn btn-outline-danger my-3" href="#">삭제하기</a>
    {% comment %} {% url 'reviews:update' review.pk %} {% endcomment %}
    </div>
    {% endif %}
  </form>
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
        return render(request, 'review/create.html', context)
    else:
        # 403 에러메세지를 던진다
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()
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
    Review.objects.get(pk=pk).delete()
    return redirect('reviews:community')
```

<br>

## 14. 댓글 작성

#### 1. Model 정의(DB 설계)

reviews > models.py

``` python
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE) # 참조 리뷰
    content = models.TextField() # 댓글 내용
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, null=True) # 댓글 작성자
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
        fields = ['title', 'movie_name', 'content', 'grade']

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
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment_form.save() # 모델 인스턴스의 save()
    return redirect('reviews:detail', review.pk)
```

<br>

#### 5. reviews > detail.html

``` html
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block body %}
  <div class="container mt-3">
    <h1>{{ review.title }}</h1>
    <span>작성시간 :
      {{ review.created_at }}
      | 수정시간 :
      {{ review.updated_at }}</span>
    <div class="mb-3 mt-3">
      <label for="reviewContent" class="form-label">내용</label>
      <textarea name='content' class="form-control" id="reviewContent" rows="3" disabled="disabled" readonly="readonly">{{ review.content }}</textarea>
    </div>
    <div class="mb-3">
      <label for="moviename" class="form-label">영화 제목</label>
      <textarea name='content' class="form-control" id="moviename" rows="3" disabled="disabled" readonly="readonly">{{ review.movie_name }}</textarea>
    </div>
    <div class="mb-3">
      <label for="reviewgrade" class="form-label">평점</label>
      <textarea name='content' class="form-control" id="reviewgrade" rows="3" disabled="disabled" readonly="readonly">{{ review.grade }}</textarea>
    </div>
    {% if request.user == review.user %}
      <div>
        <a class="btn btn-outline-primary my-3" href="{% url 'reviews:update' review.pk %}">수정하기</a>
        <a class="btn btn-outline-danger my-3" href="{% url 'reviews:delete' review.pk %}">삭제하기</a>
      </div>
    {% endif %}

    <h4 class="my-3">댓글</h4>
    {% if request.user.is_authenticated %}
    <form action="{% url 'reviews:comment_create' review.pk %}" method="POST">
      {% csrf_token %}
      <div class="mb-2">
        <input name='content' class="form-control" id="comment_form" rows="3"></input>
      </div>
      <button type="submit" class="btn btn-outline-primary">추가</button>
    </form>
    {% endif %} 
  </div>
{% endblock %}

```

<br>

## 15. 댓글 목록 출력

#### 1. reviews > views.py 

* 기존 detail 수정

``` python
def detail(request, pk):
  review = Review.objects.get(pk=pk)
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
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block body %}
  <div class="container mt-3">
    <h1>{{ review.title }}</h1>
    <span>작성시간 :
      {{ review.created_at }}
      | 수정시간 :
      {{ review.updated_at }}</span>
    <div class="mb-3 mt-3">
      <label for="reviewContent" class="form-label">내용</label>
      <textarea name='content' class="form-control" id="reviewContent" rows="3" disabled="disabled" readonly="readonly">{{ review.content }}</textarea>
    </div>
    <div class="mb-3">
      <label for="moviename" class="form-label">영화 제목</label>
      <textarea name='content' class="form-control" id="moviename" rows="3" disabled="disabled" readonly="readonly">{{ review.movie_name }}</textarea>
    </div>
    <div class="mb-3">
      <label for="reviewgrade" class="form-label">평점</label>
      <textarea name='content' class="form-control" id="reviewgrade" rows="3" disabled="disabled" readonly="readonly">{{ review.grade }}</textarea>
    </div>
    {% if request.user == review.user %}
      <div>
        <a class="btn btn-outline-primary my-3" href="{% url 'reviews:update' review.pk %}">수정하기</a>
        <a class="btn btn-outline-danger my-3" href="{% url 'reviews:delete' review.pk %}">삭제하기</a>
      </div>
    {% endif %}

    <h4 class="my-3">댓글</h4>
    {% if request.user.is_authenticated %}
    <form action="{% url 'reviews:comment_create' review.pk %}" method="POST">
      {% csrf_token %}
      <div class="mb-2">
        <input name='content' class="form-control" id="comment_form" rows="3"></input>
      </div>
      <button type="submit" class="btn btn-outline-primary">추가</button>
    </form>
    {% endif %} 
    <hr>
    <p>총 {{ comment.count }}개의 댓글이 있습니다.</p>
    {% for comment in review.comment_set.all %}
      <p>{{ comment.user.username }} | {{ comment.content }}</p>
      <form action="#" method="POST">
        {% comment %} {% url 'reviews:comment_delete' article.pk comment.pk %} {% endcomment %}
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
      <hr>
      {% empty %}
      <p>댓글이 없어요 ㅠ_ㅠ</p>
    {% endfor %}
  </div>
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
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block body %}
  <div class="container mt-3">
    <h1>{{ review.title }}</h1>
    <span>작성시간 :
      {{ review.created_at }}
      | 수정시간 :
      {{ review.updated_at }}</span>
    <div class="mb-3 mt-3">
      <label for="reviewContent" class="form-label">내용</label>
      <textarea name='content' class="form-control" id="reviewContent" rows="3" disabled="disabled" readonly="readonly">{{ review.content }}</textarea>
    </div>
    <div class="mb-3">
      <label for="moviename" class="form-label">영화 제목</label>
      <textarea name='content' class="form-control" id="moviename" rows="3" disabled="disabled" readonly="readonly">{{ review.movie_name }}</textarea>
    </div>
    <div class="mb-3">
      <label for="reviewgrade" class="form-label">평점</label>
      <textarea name='content' class="form-control" id="reviewgrade" rows="3" disabled="disabled" readonly="readonly">{{ review.grade }}</textarea>
    </div>
    {% if request.user == review.user %}
      <div>
        <a class="btn btn-outline-primary my-3" href="{% url 'reviews:update' review.pk %}">수정하기</a>
        <a class="btn btn-outline-danger my-3" href="{% url 'reviews:delete' review.pk %}">삭제하기</a>
      </div>
    {% endif %}

    <h4 class="my-3">댓글</h4>
    {% if request.user.is_authenticated %}
      <form action="{% url 'reviews:comment_create' review.pk %}" method="POST">
        {% csrf_token %}
        <div class="mb-2">
          <input name='content' class="form-control" id="comment_form" rows="3"></input>
        </div>
        <button type="submit" class="btn btn-outline-primary">추가</button>
      </form>
    {% endif %}
    <hr>
    <p>총
      {{ comment.count }}개의 댓글이 있습니다.</p>
    {% for comment in review.comment_set.all %}
      <p>{{ comment.user.username }}
        |
        {{ comment.content }}</p>
      <form action="{% url 'reviews:comment_delete' review.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
      <hr>
      {% empty %}
      <p>댓글이 없어요 ㅠ_ㅠ</p>
    {% endfor %}
  </div>
{% endblock %}
```

