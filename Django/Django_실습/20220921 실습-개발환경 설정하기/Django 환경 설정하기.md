## MAC에서 가상환경 생성 및 실행

1. pyenv 설치 및 python 설치

   * pyenv 설치하기 

   * pyenv는 여러 파이썬 버전을 쉽게 바꾸어 쓸 수 있게 도와준다.

     ``` terminal
     $ brew install pyenv
     $ echo 'eval "$(pyenv init -)"' >> /.bash_profile
     ```

     <br>

2. python 설치하기

   ``` terminal
   $ pyenv install -list
   ```

   <img src="Django 환경 설정하기.assets/pyenv.png" alt="pyenv" style="zoom:50%;" />

   <br>

3. python 설치 및 설치 후 버전 확인하기

   ``` terminal
   $ pyenv install 3.x.x
   $ pyenv versions 
   ```

   <br>

4. 실제 환경에서 사용할 버전 선택하기

   ``` terminal
   $ pyenv shell 3.x.x
   ```

   <br>

5. virtualenv 설치

   * 가상 환경을 생성하고 사용할 수 있도록 해줌

     ``` terminal
     $ brew install pyenv-virtualenv
     $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
     ```

   <br>

6. 가상 환경 생성하기

   ``` terminal
   $ pyenv virtualenv [파이썬 버전] [가상 환경 이름]
   $ pyenv virtualenv 3.x.x venv
   ```

   <br>

7. 가상 환경이 생성 되었는지 확인을 한다.

   ``` terminal
   $ pyenv versions
   ```

   ![version](Django 환경 설정하기.assets/version-3743298.png)

   <br>

8. 가상 환경 실행 명령

   ``` terminal
   $ pyenv activate [가상 환경 이름]
   $ pyenv activate venv
   ```

   <br>

9. 가상 환경 해제 명령

   ``` terminal
   $ pyenv deactive
   ```

   <br>

## MAC 장고(Django) 설치 및 환경설정

1. 가상환경 실행

   ``` terminal
   $ pyenv activate [가상 환경 이름]
   ```

   <br>

2. 가상 환경 실행 후 django를 설치할 폴더를 생성하고 cd 명령을 통해 폴더로 이동

   ``` terminal
   $ mkdir [폴더명]
   $ cd [폴더명]
   ```

   <br>

3. django 설치 전 pip upgrade

   ``` terminal
   $ python3 -m pip install --upgrade pip
   ```

   <br>

4. django 설치

   ``` terminal
   $ pip install django
   $ pip3 install django
   ```

   <br>

5. 설치 확인

   ``` terminal
   $ python -m django --version
   $ python3 -m django --version
   ```

   <br>

6. 프로젝트 생성

   ``` terminal
   $ django-admin startproject [생성할 폴더명]
   ```

   <br>

7. 생성한 폴더로 이동 후서버 실행

   ``` terminal
   $ python3 manage.py runserver
   $ python manage.py runserver
   ```

   ![runserver](Django 환경 설정하기.assets/runserver-3743317.png)

   <br>

터미널 아래에 나와있는 주소를 웹페이지에서 실행

![page](Django 환경 설정하기.assets/page-3743327.png)