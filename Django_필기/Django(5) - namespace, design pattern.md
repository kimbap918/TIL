## Namespace

#### Namespace의 필요성  

* 변수화를 해서 코드의 재사용성을 증가시키고,  코드들의 변경을 최소화 시킨다.

#### urls.py

``` python
from django.urls import path
from . import views

urlpatterns = [
  	# index에 name='index'를 추가
    path('', views.index, name='index'),
    path('create', views.create),
]
```

<br>

#### articles/index.html

``` html
{% extends 'base.html' %}

{% block content %}
<h1>작성 완료</h1>
<p>작성 내용: {{ content }}</p>
<!-- 방명록의 링크를 변수화 하여 작성 -->
<a href="{% url 'index' %}">방명록으로 돌아가기</a>
{% endblock %}
```

<br>

## URL namespace

* URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있음

* app_name attribute를 작성해 URL namespace를 작성

  #### articles/urls.py

  ``` python
  from django.urls import path
  from . import views
  # app_name을 작성해서 url의 이름을 만들어줌
  app_name = 'articles'
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('create', views.create, name='create'),
  ]
  ```

  <br>

  #### articles/create.html

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
      <!-- app_name을 지정한 이후에는 url 태그에서 반드시 app_name:url_name 형태로만 사용해야한다 -->
      <form action="{% url 'articles:create' %}">
        <input type="text" name="content">
        <input type="submit">
      </form>
    </div>
  </body>
  
  {% endblock %}
  ```

  <br>

#### (참고)DRY 원칙

* Don't Repeat Yourself의 약어
* "소스 코드에서 동일한 코드를 반복하지 말자" 라는 의미
* 동일한 코드가 반복되는것은 잠재적 버그 위협을 증가시키고 반복되는 코드를 변경할 때 모든 반복되는 코드를 찾아서 수정해야함
* 프로젝트 규모가 커질수록 애플리케이션의 유지 보수 비용이 커짐

<br>

## Design Pattern

* 각기 다른 기능을 가진 다양한 응용 소프트웨어를 개발할 때 공통적인 설계 문제가 존재하며, 이를 처리하는 해결책 사이에도 공통점이 있다는것을 발견
* 이러한 유사점을 패턴이라고 함
* 소프트웨어 또한 자주 사용되는 구조와 해결책이 있음

#### Django의 디자인 패턴 - MTV(MVC)

* Model - View - Controller 의 준말
* 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론
* Model : 데이터와 관련된 로직을 관리
  * 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
* View : 레이아웃과 화면을 처리
* Template(Controller) : 명령을 model과 view 부분으로 연결
  * 클라이언트의 요청에 대해 처리를 분기하는 역할
  * 데이터가 필요하다 -> model에 접근해 데이터를 가져옴
  * 가져온 데이터 -> template로 보내 화면을 구성
  * 구성된 화면을 응답으로 만들어 클라이언트에게 반환

* Django는 MVC 패턴을 기반으로 한 MTV 패턴을 사용함

* 두 패턴은 서로 크게 다른 점은 없으며, 일부 역할에 대해 부르는 이름이 다름

  | MVC        | MTV      |
  | ---------- | -------- |
  | Model      | Model    |
  | View       | Templete |
  | Controller | View     |

<br>

