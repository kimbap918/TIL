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
# import는 내가 필요할때 가져와서 쓰는 것


# Register your models here.
admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
  	# 아래와 같이 표기하는 방식을 커스텀 할수도 있다.
    list_display = ('title', 'created_at', 'updated_at')
    # class가 많은 이유?
    # 기본 기능을 상속 받아서 커스텀 설정을 하고 이걸 그대로 사용, 나도 사용, Django도 사용
    # 현재는 view를 function으로 정의하고 있지만 view까지도 class로 정의하는 것이 있다.
    # fields = ['title']

admin.site.register(Article, ArticleAdmin)
```

<br>

#### Static files

* 웹 서버는 특정 위치(URL)에 있는 자원(resource)을 요청받아서 제공하는 응답을 처리하는 것을 기본 동작으로 한다.
* 즉, 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공

settings.py

``` python
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

STATIC_URL = '/static/'
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



