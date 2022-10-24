## 좋아요 기능 구현하기

#### 예시- 의사와 환자 모델 Django ManyToManyField

#### hospitals/models.py

``` python
class Patient(models.Model):
  # ManyToManyField 작성
  doctors = models.ManyToManyField(Doctor)
  name = models.TextField()
  
  def __str__(self):
    return f'{self.pk}번 환자 {self.name}'
  
# Reservation Class 주석 처리
```

<br>

#### terminal

``` terminal
$ python manage.py makemigrations
$ python manage.py migrate

$ python manage.py shell_plus
```

<br>

#### 의사 1명과 환자 2명 생성

``` python
doctor = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='dane')
```

<br>

#### 예약 생성(환자가 의사에게 예약)

``` python
# patient1이 doctor1에게 예약
patient1.doctors.add(doctor1)

# patient1 - 자신이 예약한 의사목록 확인
patient1.doctors.all()
<QuerySet [<Doctor: 1번 의사 alice>]>

# doctor1 - 자신의 예약된 환자목록 확인
doctor1.patient_set.all()
<QuerySet [<Patient: 1번 환자 carol>]>
```

<br>

#### 예약 생성(의사가 환자를 예약)

#### doctor1이 patient2을 예약

``` python
# doctor1이 patient2을 예약
doctor1.patient_set.add(patient2)

# doctor1 - 자신의 예약 환자목록 확인
doctor1.patient_set.all()
<QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 dane>]>

# patient1, 2 - 자신이 예약한 의사목록 확인
patient1.doctors.all()
<QuerySet [<Doctor: 1번 의사 alice>]>

patient2.doctors.all()
<QuerySet [<Doctor: 1번 의사 alice>]>

```

<br>

#### 예약 취소하기(삭제)

* .remove()로 삭제

``` python
# doctor1이 patient1 진료 예약 취소
doctor1.patient_set.remove(patient1)
doctor1.patient_set.all()
<QuerySet [<Patient: 2번 환자 harry>]>
patient1.doctors.all()
<QuerySet []>

# patient2가 doctor1 진료 예약 취소
patient2.doctors.remove(doctor1)
patient2.doctors.all()
<QuerySet []>
doctor1.patient_set.all()
<QuerySet []>
doctor1.patient_set.all()
<QuerySet []>
```

<br>

#### 'related_name' argument

* target model이 source model을 참조할 때 사용할 manager name
* ForeignKey()의 related_name과 동일

``` python
class Patient(models.Model):
  # ManyToManyField - related_name 작성
  doctors = models.ManyToManyField(Doctor, related_name='patients')
  name = models.TextField()
  
  def __str__(self):
    return f'{self.pk}번 환자 {self.name}'
```

<br>

#### 'through' argument

* through 설정 및 Reservation Class 수정
  * 예약 정보에 증상과 예약일이라는 추가 데이터가 생김

``` python
class Patient(models.Model):
  doctor = models.ManyToManyField(Doctor, through='Reservation')
  name = models.TextField()
  
  def __str__(self):
    return f'{self.pk}번 환자 {self.name}'
  
class Reservation(models.Model):
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  symptom = models.TextField()
  reserved_at = models.DateTimeField(quto_now_add=True)
  
  def __str__(self):
    return f'{self.doctor.pk}번 의사의 {self.patient.name}번 환자'    
```

<br>

#### 정리

* M:N 관계로 맺어진 두 테이블에는 변화가 없음
* Django의 ManyToManyField는 중개 테이블을 자동으로 생성함
* Django의 ManyToManyField는 M:N 관계를 가진 모델 어디에 위치해도 상관 없음
  * 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
* 만약 테이블에서 예약정보들을 더 기록하는 형태가 된다면 중개 모델을 만들어서 through옵션을 만들어야함

<br>

## 좋아요 기능 구현

1. DB 좋아요 기록할 것인지?
   * Article(M) - User(N)
   * Article은 0명 이상의 User에게 좋아요를 받는다.
   * User는 0개 이상의 글에 좋아요를 누를 수 있다.
2. 로직
   * 상세보기 페이지에서 좋아요 링크를 누르면(URL : /articles/`<int:pk>`/like/)
   * 좋아요를 DB에 추가하고(add 메서드) 다시 상세보기 페이지로 redirect

<br>

#### articles > models.py

``` python
# 1. 모델 설계 (DB 스키마 설계)
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
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
    # 이 부분을 추가, 여기서 related_name을 설정하지 않으면 같은 모델을 참조하는 상황에서 문제가 생기기 때문에 역참조설정을 꼭 해줘야한다.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")

```

<br>

#### terminal

``` terminal
$ python manage.py makemigration
$ python manage.py migrate
```

<br>

#### articles > urls.py

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
  path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
  path('<int:pk>/like/', views.like, name='like'),
]
```

<br>

#### views.py

``` python
{% extends 'base.html' %}
{% load django_bootstrap5 %}


{% block body %}
  <h1>{{ article.title }}</h1>
  <h2>{{ article.pk }}번 게시글</h2>
  <h3><a href="{% url 'accounts:detail' article.user.pk %}">{{ article.user.username }}</a></h3>
  <p>{{ article.created_at|date:"SHORT_DATETIME_FORMAT" }}
    |
    {{ article.updated_at|date:"y-m-d D" }}</p>
  {% if request.user in article.like_users.all %}
    <a class="btn btn-secondary" href="{% url 'articles:like' article.pk %}">
      <i class="bi bi-balloon-heart-fill"></i> 좋아요 취소</a>
  {% else %}
    <a class="btn btn-danger" href="{% url 'articles:like' article.pk %}">
      <i class="bi bi-balloon-heart"></i> 좋아요</a>
  {% endif %}
  <span>{{ article.like_users.count }}</span>
  <p>작성자: {{ article.user }}</p>
  <p>{{ article.content }}
  </p>
```

<br>

#### articles > detail.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}


{% block body %}
  <h1>{{ article.title }}</h1>
  <h2>{{ article.pk }}번 게시글</h2>
  <h3><a href="{% url 'accounts:detail' article.user.pk %}">{{ article.user.username }}</a></h3>
  <p>{{ article.created_at|date:"SHORT_DATETIME_FORMAT" }}
    |
    {{ article.updated_at|date:"y-m-d D" }}</p>
  <a href="{% url 'articles:like' article.pk %}">좋아요</a><span>{{ article.like_users.count }}</span>
  <p>작성자: {{ article.user }}</p>
  <p>{{ article.content }}
  </p>
	...
```

