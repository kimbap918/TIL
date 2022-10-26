## 회원 정보 수정

* url : path('accounts/`<int:pk>`/update', views.update, name='update')

  1번 유저 수정, 2번 유저 수정, 3번 유저 수정으로 할 필요 없이 그냥 로그인한 유저의 정보를 수정해보자 

#### url.py

``` python
urlpatterns = [
  # url은 path('update/', views.update, name='update') 단, 로그인한 유저에 대해서만
  path('update/', views.update, name='update'),
]
```

<br>

#### views.py

``` python
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm


# 로그인이 필요한 상황에서 사용
# request.user로 유저 객체를 쓰는 view함수에서는 무조건 쓰는게 좋다.
@login_required
def update(request):
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('accounts:detail')
  else:
		form = CustomUserChangeForm(instance=request.user)
  context = {
    'form': form
  }
  return render(request, 'accounts/update.html', context)
```

<br>

#### forms.py

``` python
from django.contrib.auth imoport get_user_model
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = get_user_model()
    fields = ('first_name', 'last_name', 'email') # 3가지만 수정할수 있도록
    # '__all__'
```

<br>

#### update.html

``` python
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
  <h1>수정하기</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% bootstrap_button button_type="submit" content="OK" %}
  </form>
{% endblock %}
```

<br>

여기까지 하면 NoReverseMatch 오류 발생

NoReverseMatch : url을 변수화해놓은 것을 path로 변환하는 과정에서 매치되지 않았다

=> pk 값을 넣어준다.

#### views.py

``` python
from django.contrib.auth.decorators import login_required

# 로그인이 필요한 상황에서 사용
# request.user로 유저 객체를 쓰는 view함수에서는 무조건 쓰는게 좋다.
@login_required
def update(request):
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      # pk 넣어주기
      return redirect('accounts:detail', request.user.pk)
  else:
		form = CustomUserChangeForm(instance=request.user)
  context = {
    'form': form
  }
  return render(request, 'accounts/update.html', context)
```

<br>

#### 수정 관련 참고

#### 출력되는 이름 한국 순서대로 바꾸기

#### models.py

``` python
class User(AbstractUSer):
  @property
  def full_name(self):
    return f'{self.last_name}{self.first_name}'
```

<br>



#### 비밀번호 변경 페이지 작성

#### accounts/urls.py

``` python
app_name = 'accounts'
urlpatterns = [
  ...,
  path('password/', views.change_password, name='change_password')
]
```

<br>

#### accounts/views.py

``` python
def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    # form = PasswordChangeForm(user=request.user, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('accounts:index')
  else:
		form = PasswordChangeForm(request.user)
  context = {
    'form': form
  }
  return render(request, 'accounts/change_password.html', context)
```

<br>

#### accounts/change_password.html

``` python
{% extends 'base.html' %}
{% block content %}
<h1>비밀번호 변경</h1>
<form action="{% url 'accounts:change_password' %}" method="POST">
{% csrf_token %}
{{ form.as_p }}
<input type="submit">
</form>
{% endblock content %}
```

<br>

#### 회원가입 이후 로그인

#### accounts/views.py

* 회원가입 후 곧바로 로그인 진행

``` python
def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect('articles:index')
  else:
    form = CustomUserCreationForm()
  context = {'form': form,}
  return render(request, 'accounts/signup.html', context)
```

<br>

#### 탈퇴하면서 해당 유저의 세션 정보도 함께 지우고 싶을 경우

#### accounts/views.py

``` python
def delete(request):
  request.user.delete()
  auth_logout(request)
```

<br>

#### 암호 변경 시 세션 무효화 방지하기

* 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어버려 로그인 상태가 유지되지 못함
* 비밀번호는 잘 변경되었으나 비밀번호가 변경 되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문
* update_session_auth_hash(request, user)
  * 현재 요청과 새 session data가 파생 될 업데이트 된 사용자 객체를 가져오고, session data를 적절하게 업데이트해줌
  * 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 session을 업데이트

``` python
from django.contrib.auth import update_session_auth_hash

def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    # form = PasswordChangeForm(user=request.user, data=request.POST)
    if form.is_valid():
      form.save()
      update_session_auth_hash(request, form.user)
      return redirect('accounts:index')
  else:
		form = PasswordChangeForm(request.user)
  context = {
    'form': form
  }
  return render(request, 'accounts/change_password.html', context)
```

<br>

