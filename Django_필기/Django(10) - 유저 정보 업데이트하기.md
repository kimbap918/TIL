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

(참고)출력되는 이름 한국 순서대로 바꾸기

#### models.py

``` python
class User(AbstractUSer):
  @property
  def full_name(self):
    return f'{self.last_name}{self.first_name}'
```

<br>

