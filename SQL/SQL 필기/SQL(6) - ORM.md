## ORM

Object-Relational-Mapping

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술

파이썬에서는 SQLAlchemy, peewee 등 라이브러리가 있으며 Django 프레임워크에서는 내장 Django ORM을 활용

<br>

"객체(object)로 DB를 조작한다"

``` python
genre.objects.all()

= SELECT * FROM Genre;
```

<br>

* 모델 설계 및 반영

  * (1) 클래스를 생성하여 내가 원하는 DB의 구조를 만든다.

    ``` python
    from django.db import models
    
    # Genre 클래스를 만드는데, 
    # models.Model 내부 클래스를 상속받는 이유?
    # 미리 만들어진 기능들을 활용하고 싶어서!
    class Genre(models.Model):
      name = models.CharField(max_length=30)
    ```

    <br>

  * (2) 클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일을 생성한다(자동)

    ``` terminal
    # 터미널
    $ python manage.py makemigrations # 터미널에서 마이그레이션 파일 생성
    # 결과
    # Migrations for 'db':
    # db/migrations/0001_initial.py
    # - Create model Genre
    ```

    ``` python
    # db/migrations/0001_initial.py 위치에 아래와 같이 파일이 자동 생성됨
    # Generated by Django 4.0.6 0n 2022-08-24 10:53
    from django.db import models
    
    class Migration(migrations.Migration):
      initial = True
      
      dependencies = [
      ]
      
      operations = [
        migrations.CreateModel(
        	name.'Genre',
          fiends =[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name ='ID')),
            ('name', models.CharField(max_length=30)),
          ], 
        ),
      ]
    ```

    <br>

  * (3) DB에 migrate한다.

    ``` terminal
    # 터미널
    # DB에 반영
    $ python manage.py migrate
    
    # Operations to perform:
    #		Apply all migrations: db
    # Running migrations:
    #		Applying db.0001_initial... OK
    ```

    Migration(마이그레이션)

    * Model에 생긴 변화를 DB에 반영하기 위한 방법
    * 마이그레이션 파일을 만들어 DB스키마를 반영한다.
      * 명령어
        * makemigration : 마이그레이션 파일 생성
        * migrate : 마이그레이션을 DB에 반영

    <br>

    ``` terminal
    # 터미널
    $ python manage.py shell_plus # 이 명령어를 통해서 접속
    
    # class Person:
    #		pass
    
    # iu 라고 하는 변수의 이름을 가진 Person 클래스의 인스턴스를 만드는 코드?
    # iu = Person()
    
    # iu의 name 속성으로 아이유라고 하는 코드는?
    # iu.name = '아이유'
    
    # 이것을 터미널에서 똑같이 사용가능하다!
    
    # 생성 방법 1
    In [1]: Genre.objects.crete(name='트로트')
    Out[1]: <Genre: Genre object (1)>
    
    
    # 생성 방법 2
    In[1] : genre = Genre()
    In[2] : genre.name = '인디밴드'
    In[3] : genre.name
    Out[3] : '인디밴드'
    
    # 저장 전 genre 객체 확인
    In[4] : genre
    Out[4] : <Grenre: Genre object (None)>
    
    # 저장하기
    In[5] : genre.save() 
    
    # 저장 후 genre 
    In[6] : genre
    Out[6] : <Grenre: Genre object (1)>
    
    # Genre에 저장된 모든 값 확인
    In[7] : Grenre.objects.all()
    In[7] : <QuerySet [<Genre: Genre object (1)>]>
    
    # 타입 확인
    In[8] : type(Genre.objects.all())
    Out[8] : django.db.models.query.QuerySet
    
    # Genre에 저장된 0번째 값의 이름 확인
    In[9] : Genre.objects.all()[0].name
    Out[9] : '인디밴드'
    
    # 조회시 for문 사용
    In[10] : for genre in genres:
    						print(genre.name)
    # 인디밴드
    
    # 반드시 하나. 없거나, 많으면 오류를 띄움
    # PK를 가져올때 사용
    In[11] : Genre.objects.get(id=1)
    Out[11] : <Genre: Genre object (1)>
    
    # 무조건 결과가 QuerySet(일종의 리스트)을 가져옴
    In[12] Genre.objects.filter(id=1)
    Out[12] : <QuerySet [<Genre: Genre object (1)>]>
    
    
    # 수정과 삭제 모두 반드시 가져온 뒤 수정/삭제가 가능함
    # 인디밴드를 인디음악으로 변경(수정)
    genre = Genre.objects.get(id=1)
    In[13] : genre.name = '인디음악'
    In[14] : genre.save() # 반드시 save해야 반영됨
    
    # 삭제
    genre = Genre.objects.get(id=1)
    genre.delete()
    # 이 방법도 가능
    Genre.objects.get(id=1).delete()
    
    ```

<br>

* Artist 모델 생성

``` python
class Artist(models.Model):
  name = models.CharField(max_length=30)
  debut = models.DateField()
```

* 마이그레이션!

``` terminal
$ python manage.py makemigrations
$ python manage.py migrate
```

<br>

[예시]

``` python
# 1. Artist 생성
import datetime
artist = Artist()
artist.name = '아이브'
# 2021년 12월 1일 
artist.debut = datetime.date(2021, 12, 1)
artist.save()
```

<br>

#### 요약

1. ORM은 객체를 조작해서 데이터베이스를 관리한다.
2. 데이터베이스를 관리할때 모델링을 하는 파트, 테이블을 조작하는 파트가 있다
3. 모델링을 할땐 class를 만들고, 테이블을 조작할땐 Migration
4. CRUD Operation은 객체를 조작하면서 한다.

