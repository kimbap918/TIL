## Django

#### Framework = Frame(뼈대) + work(일하다)

* 서비스 개발에 필요한 기능들을 미리 구현해서 모아놓은 것

<br>

#### 클라이언트와 서버

* 오늘날 우리가 사용하는 대부분의 웹 서비스는 클라이언트-서버 구조를 기반으로 동작
* 클라이언트에서 요청을 하면 서버에서 요청을 받고 응답을 하는 구조로 상호작용함
* 이 중에서 Django는 서버를 구현하는 웹 프레임워크 

<br>

#### 클라이언트

* 웹 사용자의 인터넷에 연결된 장치
* Chrome 또는 Firefox 와 같은 웹 브라우저
* 서비스를 요청하는 주체

<br>

#### 서버

* 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
* 클라이언트가 웹 페이지에 접근하려고 할 때 클라이언트 서버로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 포시됨
* 요청에 대해 서비스를 응답하는 주체

<br>

## Web browser와 Web page

#### 동적 웹 페이지

* Dynamic Web page
* 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
* 웹 페이지의 내용을 바꿔주는 주체 == 서버
  * 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌
  * 사용자의 요청을 받아서 적절한 응답을 만들어주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임워크가 Django

<br>

#### 파이썬 가상환경 설정(MAC)

[pyenv] 설치하기

``` terminal
$ brew install pyenv
$ echo 'eval' "$(pyenv init -)"' >> ~/.bash_profile'
```

<br>

파이썬 설치

``` terminal
$ pyenv install -list
$ pyenv install 3.x.x
$ pyenv versions 
```

<br>

[virtualenv] 설치

``` terminal
$ brew install pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
```

<br>

#### 가상 환경 생성하기

가상 환경 생성 명령

``` terminal
$ pyenv virtualenv [파이썬 버전] [가상 환경 이름]
$ pyenv virtualenv 3.x.x venv
```

<br>

가상 환경 생성 확인

``` terminal
$ pyenv versions
```

<br>

가상 환경 실행 명령

``` terminal
$ pyenv activate [가상 환경 이름]
$ pyenv activate venv
$ source server-venv/bin/activate
```

<br>

가상 환경 해제 명령

``` terminal
$ pyenv deactivate
```

<br>

#### 장고(django) 설치 및 환경 설정

가상환경 실행

``` terminal
$ pyenv activate [가상 환경 이름]
```

<br>

가상 환경 실행 후 django를 설치할 폴더를 생성하고 cd 명령을 통해 폴더로 이동

``` terminal
$ mkdir [폴더명]
$ cd [폴더명]
```

<br>

django 설치 전 pip upgrade

``` terminal
$ python3 -m pip install --upgrade pip
```

<br>

django 설치

``` terminal
$ pip install django
$ pip3 install django
```

<br>

설치 확인

``` terminal
$ python -m django --version
$ python3 -m django --version
```

<br>

프로젝트 생성

``` terminal
$ django-admin startproject [생성할 폴더명]
```

<br>

생성한 폴더로 이동 후서버 실행

``` terminal
$ python3 manage.py runserver
$ python manage.py runserver
```

 <br>

터미널 아래에 나와있는 주소를 웹페이지에서 실행