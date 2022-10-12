## Django 로그인에 대한 이해

#### HTTP 특징

* 비 연결 지향(connectionlsee)
  * 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
* 무상태(stateless)
  * 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
  * 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적

<br>

#### 어떻게 로그인 상태를 유지할까?

* 우리가 로그인을 하고 웹 사이트를 사용할 때 페이지를 이동해도 로그인 **상태**가 유지됨
* 서버와 클라이언트 간 지속적인 상태 유지를 위해 **쿠키와 세션**이 존재

<br>

## 쿠키

* 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
* 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
  * 브라우저는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
  * 동일한 서버에 재 요청시 저장된 쿠키를 함께 전송
* 쿠키는 서로 다른 요청이 동일한 브라우저로부터 발생한 것인지 판단할 때 주로 사용됨

<br>

#### 사용목적

* 세션관리
  * 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니
* 개인화
  * 사용자 선호, 테마
* 트래킹
  * 사용자 행동을 기록 및 분석

<br>

#### 세션

* 사이트와 특정 브라우저 사이의 상태를 유지시키는 것
* 클라이언트가 서버에 접속하면 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장
  * 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 session id가 저장된 쿠키를 서버에 전달
  * 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직을 처리
* session id는 세션을 구별하기 위해 필요하며, 쿠키에는 session id만 저장

<br>

#### 쿠키의 수명

* Session cookie
  * 현재 세션이 종료되면 삭제됨
  * 브라우저 종료와 함께 삭제됨
* Persistent coocies
  * Expire 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 사라지면 삭제됨

<br>

## Login

- URL : GET /account/login/

- 처리
  * (템플릿) 사용자에게 Form을 제공한다
- URL : POST /accounts/login/
- 처리
  * (로그인) 로직처리
    * 사용자인지 확인하고, django_session 테이블에 저장, 쿠키 주기
  * (성공) 게시글 목록 페이지로 redirect
  * (실패) 로그인 Form

-> Article Create / User Create 로직과 매우 비슷함.

#### urls.py

``` python
urlpatterns = [
 path('login/', views.login, name='login'), 
]
```

<br>

#### views.py

``` python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

@login_required # 이 어노테이션을 함수 위에 사용하면 로그인을 요구한다. 수정하기 등.. 

def login(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      # 이 상태에서는 유효성 검사가 되지 않는다. AuthenticationForm은 modelForm이 아니다
      # form = AuthenticationForm(request.POST)
      form = AuthenticationForm(request.POST)
      if form.is_valid():
        # 세션에 저장
        # login 함수는 request, user 객체를 인자로 받음
        # user 객체는 form에서 인증된 유저 정보를 받을 수 있음
        auth_login(request, form.get_user())
        # 접근 제한 막기
        return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
      'form': form
    }
    return render(request, 'accounts/login.html', context)
 	else:
    form = AuthenticationForm()
  context = {
    'form': form
  }
    return redirect('accounts:login')
```

* 로그인을 위한 built-in-form
  * 로그인 하고자 하는 사용자 정보를 입력 받음(username, password)
  * ModelForm이 아닌 일반 Form을 상속 받고있으며 request를 첫번째 인자로 취함
* login()
  * login(request, user, backend=None)
  * 인증된 사용자를 로그인
    * 유저의 ID를 세션에 저장하여 세션을 기록
  * HttpRequest 객체와 User 객체 필요 
    * 유저 정보는 반드시 인증된 유저 정보여야 함
      * authenticate()함수를 활용한 인증
      * AuthenticationForm을 활용한 is_vaild

<br>

#### login.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
	<h1>글쓰기</h1>
<Form action="" method="POST">
  {% csrf_token %}
  {% bootstrap_form form %}
  {% bootstrap_button button_type="submit" content="OK" %}
</Form>
{% endblock %}
```

<br>

#### base.html

``` python
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  {% bootstrap_css %}
  {% block css %}{% endblock css %}
</head>

<body>
	# 로그인시 상단에 유저 이름이 뜰수 있게함
	<span>{{ request.user }}</span>
  # 유저 로그인 시 로그아웃이 뜰 수 있게 분기
  {% if request.user.is_authenticated %}
  <a href="">로그아웃</a>
	{% else %}  
  <a href="{% url 'accounts:signup' %}">회원가입</a>
  <a href="{% url 'accounts:login' %}">로그인</a>
  {% endif %}

  <div class="container">
  {% block body %}
  {% endblock body %}
  </div>
  {% bootstrap_javascript %}
</body>

</html>
```

* 로그인 로직 작성은 일반적인 ModelForm 기반의 Create 로직과 동일하지만
  * ModelForm이 아닌 Form으로 필수 인자 구성이 다르다
  * DB에 저장하는 것 대신 세션에 유저를 기록하는 함수를 호출한다
    * View 함수와 이름이 동일하여 변경하여 호출
    * 로그인 URL이 '/accounts/login/'에서 변경되는 경우 settings.py LOGIN_URL을 변경하여야 한다.

* get_user()
  * AuthenticationForm의 인스턴스 메서드
  * 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

<br>

## logout

#### urls.py

``` python
urlpatterns = [
 path('login/', views.login, name='login'), 
 path('logout/', views.logout, name='logout'),
]
```

<br>

#### views.py

``` python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def logout(request):
  auth_logout(request)
  return redirect('articles:index')
```

<br>

#### base.html

``` html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  {% bootstrap_css %}
  {% block css %}{% endblock css %}
</head>

<body>
	# 로그인시 상단에 유저 이름이 뜰수 있게함
	<span>{{ request.user }}</span>
  # 유저 로그인 시 로그아웃이 뜰 수 있게 분기
  {% if request.user.is_authenticated %}
  <a href="{% url 'accounts:logut' %">로그아웃</a>
	{% else %}  
  <a href="{% url 'accounts:signup' %}">회원가입</a>
  <a href="{% url 'accounts:login' %}">로그인</a>
  {% endif %}

  <div class="container">
  {% block body %}
  {% endblock body %}
  </div>
  {% bootstrap_javascript %}
</body>

</html>
```

<br>

1. 버튼을 안 만들었는데 URL로 직접 접근할 수 있을때

   -> View(서버)에서 막아두면 된다

2. 인증여부를 직접 조건문 @login_required 데코레이터를 쓸 수 있음

   -> @login_required의 역할은 URL로 로그인페이지로 보내줌

3. if request.method == 'POST':

4. form = AuthenticationForm(request, data=request.POST)

   if form.is_valid():

   ​	auth_login(request, form.get_user())

   ​	return redirect(request.GET.get('next') or 'articles:index')

   redirect를 할 때 URL Get 파라미터로 보내준 값을 쓴다.

   없으면 None or 'articles:index'

   있으면 /articles/1/update/ or 'articles:index'

