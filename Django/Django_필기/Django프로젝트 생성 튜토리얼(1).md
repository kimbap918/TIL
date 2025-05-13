
# Django 프로젝트 파일 구조와 역할

이 문서는 일반적인 Django 프로젝트의 주요 파일 및 폴더 구조와 그 각각의 역할을 설명합니다.

## 1. `manage.py`
- **역할**: Django 프로젝트의 진입점이자 명령어 인터페이스.
- 프로젝트 시작, 마이그레이션 적용, 관리자 계정 생성 등 다양한 명령을 처리할 수 있습니다.
- 이 파일은 jango가 프로젝트를 시작할 때 자동으로 생성하는 파일로, 프로젝트를 진행하면서 수정할 일은 거의 없습니다.
- 주요 명령어:
  - `runserver`: 개발 서버를 시작합니다.
  - `migrate`: 데이터베이스 마이그레이션을 적용합니다.
  - `createsuperuser`: 관리자 계정을 생성합니다.

---

## 2. 프로젝트 폴더 (예: `p2p/`)
이 폴더에는 프로젝트 설정 파일, URL 라우팅 파일, WSGI/ASGI 파일 등이 포함되어 있습니다.

### `__init__.py`
- **역할**: 이 폴더가 Python 패키지로 인식되게 하는 역할을 합니다. 보통은 빈 파일이지만 필요 시 초기화 코드를 넣을 수 있습니다.

### `settings.py`
- **역할**: Django 프로젝트의 설정 파일로, 전체 프로젝트 설정을 관리합니다.

- 주요 설정:
  - `INSTALLED_APPS`: 프로젝트에 설치된 앱 목록, Django 프로젝트에서 사용되는 모든 앱을 등록하는 곳입니다. 새로운 기능(앱)을 추가할때, 해당 앱이 프로젝트에 인식되도록 반드시 INSTALLED_APPS에 등록해야 합니다.
  
    ``` python
    INSTALLED_APPS = [
        # 기본 Django 앱들
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
         
      	# 외부 패키지
        'rest_framework',  # Django REST Framework
      
        # 내가 만든 새로운 앱
        'articles',
    ]
    ```
  
  - `DATABASES`: 데이터베이스 설정 (기본은 SQLite, 다른 데이터베이스로 변경 가능).
  
    ``` python
    # 프로젝트가 여러 데이터베이스를 사용하는 경우 이곳에 여러 데이터베이스 설정을 추가할 수 있습니다.
    DATABASES = {
        "default": { 
            "ENGINE": "django.db.backends.sqlite3", # Django가 사용할 데이터베이스의 종류를 지정합니다. 
          	# django.db.backends.sqlite3: SQLite 데이터베이스를 사용.
    				# django.db.backends.postgresql: PostgreSQL 데이터베이스를 사용.
    				# django.db.backends.mysql: MySQL 데이터베이스를 사용.
    				# django.db.backends.oracle: Oracle 데이터베이스를 사용.
            "NAME": BASE_DIR / "db.sqlite3", 
          	# 사용할 데이터베이스 파일이나 데이터베이스 이름을 지정
          	# BASE_DIR / "db.sqlite3"는 SQLite 데이터베이스 파일이 BASE_DIR (프로젝트의 기본 디렉토리) 내의 db.sqlite3라는 이름의 파일로 저장된다는 뜻입니다.
          
        }
    }
    ```
  
    ```python
    # 다른 데이터베이스 설정의 예시
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "mydatabase",
            "USER": "mydatabaseuser",
            "PASSWORD": "mypassword",
            "HOST": "localhost",  # 데이터베이스 서버 주소
            "PORT": "5432",  # 데이터베이스 포트
        }
    }
    
    ```
  
  - `TEMPLATES`:  Django 프로젝트에서 템플릿 엔진의 설정을 정의하는 부분. 템플릿 파일의 경로와 처리 방법, 추가적으로 사용할 수 있는 옵션들을 설정합니다.
  
    ``` python
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates", # 어떤 템플릿 엔진을 사용할지 결정하는 설정
          	#  "django.template.backends.django.DjangoTemplates"는 Django의 기본 템플릿 엔진을 의미
            "DIRS": [BASE_DIR / "templates"], # 템플릿 파일들이 저장된 디렉토리 경로를 정의하는 리스트
          	# 위 설정은 Django 프로젝트의 기본 디렉토리 아래에 templates/ 폴더가 위치해 있으며, 그 폴더에서 템플릿 파일을 찾는다는 의미
          	# BASE_DIR은 프로젝트의 루트 디렉토리
            "APP_DIRS": True, # 각 앱(app)의 templates/ 디렉토리에서 템플릿을 자동으로 찾을지 여부
            "OPTIONS": { # 템플릿 렌더링 시 자동으로 템플릿에 전달되는 변수나 데이터를 처리하는 함수(또는 모듈)들의 목록
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
  
  - `STATIC_URL`, `STATICFILES_DIRS`: **`STATIC_URL`** 설정은 **정적 파일(static files)**을 제공할 때 사용되는 **URL 경로**를 지정하는 부분입니다. 정적 파일은 CSS, JavaScript, 이미지 파일 등과 같이 서버에서 별도로 처리할 필요 없이 그대로 클라이언트(브라우저)로 전송되는 파일들입니다
  
    ``` python
    STATIC_URL = '/static/'
    
    STATICFILES_DIRS = [
        BASE_DIR / "static",  # 프로젝트 루트 디렉토리의 static 폴더
    ]
    ```
  
  - `MIDDLEWARE`: 요청과 응답을 처리하는 미들웨어 설정. 미들웨어는 요청(Request)이 뷰(View)로 전달되기 전에, 또는 응답(Response)이 클라이언트로 전달되기 전에 특정 작업을 수행할 수 있도록 합니다. 이를 통해 보안, 세션 관리, 인증, 메시지 처리 등의 기능을 추가할 수 있습니다.
  
    ``` python
    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware", # 보안강화
        "django.contrib.sessions.middleware.SessionMiddleware", # 세션관리
        "django.middleware.common.CommonMiddleware", # 일반적인 웹 개발 작업 처리
        "django.middleware.csrf.CsrfViewMiddleware", # CSRF(Cross-Site Request Forgery) 공격을 방어하는 미들웨어
        "django.contrib.auth.middleware.AuthenticationMiddleware", # 사용자 로그인 여부 관리
        "django.contrib.messages.middleware.MessageMiddleware", # Django의 메시지 프레임워크를 활성화하는 미들웨어
        "django.middleware.clickjacking.XFrameOptionsMiddleware", # Clickjacking 공격을 방지하기 위한 미들웨어
    ]
    
    ```
  
    

### `urls.py`
- **역할**: 프로젝트의 URL 경로를 정의하며, 각 경로가 어떤 뷰(View)를 호출할지 결정합니다. 모든 Django 프로젝트는 `urls.py` 파일에 이 리스트를 정의해야 합니다.

- 예시:
  ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path("admin/", admin.site.urls), # Django의 Admin 페이지에 대한 경로를 정의하고 있습니다.
  ]
  
  ```

### `wsgi.py`
- **역할**: WSGI(Web Server Gateway Interface) 설정 파일로, Django 프로젝트를 배포할 때 사용됩니다. WSGI 서버(Gunicorn, uWSGI 등)와 상호작용합니다.
- Django 프로젝트의 배포 과정에서 사용되는 파일로, 일반적으로 **직접 수정할 일이 거의 없습니다**.

### `asgi.py`
- **역할**: ASGI(Asynchronous Server Gateway Interface) 설정 파일로, 비동기 요청(예: 웹소켓)을 처리하는 경우 사용됩니다.
-  **`asgi.py`** 파일 역시 **대부분의 경우 직접 수정할 일이 거의 없습니다**.

---

## 3. 앱 폴더 (예: `app_name/`)
Django 프로젝트는 여러 개의 앱을 포함할 수 있으며, 각각의 앱은 독립적인 기능을 담당합니다.

### `models.py`
- **역할**: 데이터베이스 테이블을 정의하는 곳으로, Django의 ORM을 통해 테이블과 상호작용합니다.
- 예시:
  ```python
  from django.db import models
  
  class Parking(models.Model):
      name = models.CharField(max_length=100)
      location = models.CharField(max_length=200)
      capacity = models.IntegerField()
  ```

### `views.py`
- **역할**: 요청을 처리하고 응답을 반환하는 로직을 작성하는 곳입니다. HTML 페이지 또는 JSON 데이터를 반환할 수 있습니다.
- 예시:
  ```python
  from django.http import HttpResponse
  
  def index(request):
      return HttpResponse("Hello, world!")
  ```

### `urls.py`
- **역할**: 앱 내부에서 사용되는 URL 패턴을 정의합니다. 프로젝트의 `urls.py`에서 이 파일을 포함하여 앱 단위에서의 URL 라우팅을 관리합니다.

### `admin.py`
- **역할**: Django 관리자 인터페이스에서 모델을 관리할 수 있도록 설정하는 파일입니다.
- 예시:
  ```python
  from django.contrib import admin
  from .models import Parking
  
  admin.site.register(Parking)
  ```

### `forms.py` (선택사항)
- **역할**: Django의 `forms` 라이브러리를 사용하여 사용자 입력을 처리하고 검증하는 폼을 정의합니다.

### `migrations/`
- **역할**: 모델의 변경 사항을 추적하고 데이터베이스에 반영하는 마이그레이션 파일들이 저장됩니다.

### `apps.py`
- **역할**: 앱의 설정 정보를 담고 있으며, `INSTALLED_APPS`에 등록될 때 사용됩니다.

---

## 4. 템플릿 및 정적 파일

### `templates/`
- **역할**: HTML 템플릿 파일을 저장하는 폴더로, 뷰에서 렌더링하여 사용자에게 보낼 HTML을 생성합니다.

### `static/`
- **역할**: CSS, JavaScript, 이미지 같은 정적 파일들이 저장되는 폴더입니다.

---

## 5. 기타 파일

### `requirements.txt`
- **역할**: 프로젝트에서 필요한 Python 패키지 목록을 정의한 파일입니다. `pip` 명령어로 패키지를 설치할 때 사용됩니다.
- 예시:
  ```
  Django==4.0
  djangorestframework==3.13
  ```

### `README.md`
- **역할**: 프로젝트의 설명, 설치 방법, 사용법 등을 담고 있는 문서입니다.
