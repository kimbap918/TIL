## 팔로우 기능 구현하기

* 1. A가 B를 친구 요청(팔로잉/팔로우)
  2. B입장에서는 팔로워로 A가 등록됨
* 팔로잉 기능 구현
  * 사용자 프로필 페이지에 들어가 팔로우 상태가 아니면 '팔로우'를 누르면 추가
  * 이미 팔로우 상태면, '팔로우 취소' 버튼을 누르면 삭제(remove)
* 팔로우/취소 요청을 할 때 URL은 어떻게 할까?
  * /accounts/`<int:pk>`/follow/
  * 처리 완료 후에는 프로필 페이지로 redirect
* 셀프 좋아요는 가능하지만 셀프 팔로우는 허용 불가

<br>

#### accounts > urls.py

``` python
from django.urls import path
from . import views
# app_name은 왜 쓸까요?
# 우리는 기본적으로 URL을 모두 변수화해서 쓰고 있음
# Template, View에서 직접 '/accounts/' X 
# app_name과 path 이름으로 

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/follow', views.follow, name='follow'),
]
```

<br>

#### views.py

``` python
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

@require_POST
@login_required
def follow(request, pk):
    # 프로필에 해당하는 유저를 로그인한 유저가 팔로우 할 수 없음
    user = get_object_or_404(get_user_model(), pk=pk)
    # article = get_object_or_404(Article, pk=pk)
    # user = get_user_model().objects.get(pk=pk)
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

#### accounts > detail.html

``` python
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
```

<br>

