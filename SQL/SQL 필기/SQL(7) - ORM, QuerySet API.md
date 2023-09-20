## QuerySet API

* **gt** : greater than

  ``` python
  Entry.objects.filter(id__gt=4)
  
  ## 아래의 코드와 같은 역할이다.
  SELECT ... WHERE id > 4;
  ```

  <br>

* **gte** : greater than equal

  ``` python
  Entry.objects.filter(id__gte=4)
  
  ## 아래의 코드와 같은 역할이다.
  SELECT ... WHERE id >= 4;
  ```

  <br>

* **lt, lte** : less than, less than equal

  ``` python
  Entry.objects.filter(id__lt=4)
  Entry.objects.filter(id__lte=4)
  
  ## 아래의 코드와 같은 역할이다.
  SELECT ... WHERE id < 4;
  SELECT ... WHERE id <= 4;
  ```

  <br>

* **in**

  ``` python
  Entry.objects.filter(id__in=[1, 3, 4])
  Entry.objects.filter(headline__in='abc')
  
  SELECT ... WHERE id IN (1, 3, 4);
  SELECT ... WHERE headline IN('abc');
  ```

  <br>

* **startwith**

  ``` python
  Entry.objects.filter(headline__startwith='Lennon')
  
  SELECT ... WHERE headline LIKE 'Lennon%';
  ```

  <br>

* **istartswith** : case-insensitive

  ``` python
  Entry.objects.filter(headline__istartswith='Lennon')
  
  SELECT ... WHERE headline LIKE 'Lennon%';
  SELECT ... WHERE headline ILIKE 'Lennon%';
  ```

  <br>

* **endswith**

  ``` python
  Entry.objects.filter(headline__endswith='Lennon')
  Entry.objects.filter(headline__iendswith='Lennon')
  
  SELECT ... WHERE headline LIKE '%Lennon';
  SELECT ... WHERE headline ILIKE '%Lennon';
  ```

  <br>

* **contains**

  ``` python
  Entry.objects.filter(headline__contains='Lennon')
  Entry.objects.filter(headline__iicontains='Lennon')
  
  SELECT ... WHERE headline LIKE '%Lennon%';
  SELECT ... WHERE headline ILIKE '%Lennon%';
  ```

  <br>

* **range**

  ``` python
  import datetime
  start_date = datetime.date(2005, 1, 1)
  end_date = datetime.date(2005, 3, 31)
  Entry.objects.filter(pub_date__range=(start_date, end_date))
  
  SELECT ... WHERE pub_date
  BETWEEN '2005-01-01' and '2005-03-31'
  ```

  <br>

* **복합 활용**

  ``` python
  inner_qs = Blog.objects.filter(name__contains='Cheddar')
  entries = Entry.objects.filter(blog__in=inner_qs)
  
  SELECT ...
  WHERE blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%Cheddar%');
  ```

  <br>

* **활용**

  ``` python
  # limit
  Entry.objects.all()[0]
  
  SELECT ... LIMIT 1;
  
  # 오름차순, 내림차순
  Entry.objects.order_by('id')
  Entry.objects.order_by('-id')
  
  SELECT ...
  ORDER BY id;
  
  SELECT ...
  ORDER BY id DESC;
  ```

  <br>

## ORM

``` python
# models.py
class Genre(models.Model):
  name = models.CharField(max_length=30)
  
class Artist(models.Model):
  name = models.CharField(max_length=30)
  
# Genre는 Album을 0~여러개 가진다. / Album은 하나의 Genre를 가짐
# 예) 트로트 -> 네박자, ...
# Artist는 Album을 0~여러개 가진다. / Album은 한명의 Artist를 가진다.
# 예) BTS -> Butter
class Album(models.Model):
  name = models.CharField(max_length=30)
  genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
  artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
  
# 1:N 관계에서의 Create  
# 객체
# Class 정의를 genre로 했기 때문
album = Album()
album.name = '꽃'
album.genre = 1 # 오류가 발생함
# ValueError : Cannot assign "1" : "Album.genre" must be a "Genre" instance
# 그럼 어떻게?
genre = Genre.objects.get(id=1)
album.genre = genre
artist = Artist.objects.get(id=1)
album.artist = artist
album.save()

# 값
# 테이블에 실제 필드는 _id가 붙어있기 때문
album = Album()
album.genre_id = 1
album.artist_id = 1
album.name = '미아'
album.save()

# N => 1 (참조)

# 앨범의 id가 1인 것의
album.objects.get(id=1) # 앨범 객체
# 장르의 이름은..?
album.genre # 장르 객체
# <Genre: Genre object(1)>
album.genre.name
# '발라드'

# 1 => N (역참조)
# 클래스이름_set
# id가 1인 장르의 모든 앨범은?
g1 = Genre.objects.get(1)
g1.album_set_all()
```

<br>

* models.ForeignKey 필드

  * 2개의 필수 위치 인자

    * Model class : 참조하는 모델

    * on_delete :  외래 키가 참조하는 객체가 삭제되었을 때 처리 방식
      * **CASCADE** : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
      * PROTECT : 삭제되지 않음
      * SET_NULL : NULL 설정
      * SET_DEFAULT : 기본 값 설정

* Foreign Key(외래키)

  * 키를 사용하여 부모 테이블의 유일한 값을 참조(참조 무결성)
    * 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
  * 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

  ``` python
  class Album(models.Model):
    name = models.CharField(max_length=30)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    
  # [주의] 외래키를 사용하면 db에 생성 시 genre 가 아닌 genre_id로 생성되므로 genre_id = ... 로 변수를 만들면 genre_id_id 가 됨(...)
  ```

<br>

* 참조와 역참조

  ``` python
  class Album(models.Model):
    name = models.CharField(max_length=30)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    
  # 1. 참조
  album = Album.objects.get(1) 
  album.artist # artist의 객체(인스턴스)
  album.genre # genre의 객체(인스턴스)
  
  # 2. 역참조
  # 역참조에는 클래스이름_set 을 붙이는 규칙이 있다.
  genre = Genre.objects.get(1)
  genre.album_set_all() # album의 인스턴스가 담긴 쿼리셋
  ```

  <br>

* Create

  ```python
  artist = Artist.objects.get(1)
  genre = Genre.objects.get(1)
  
  album = Album()
  album.name = '앨범1'
  album.artist = artist
  album.genre = genre
  album.save()
  ```

  