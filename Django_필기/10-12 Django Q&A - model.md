## Django Q&A

Q. account.User에 만들고 시작하는지? 왜 auth.User를 사용하지 않는지?

* settings.py : AUTH_USER_MODEL
* accounts앱에 abstractUser를 상속받아서 빈 껍데기(pass)

-> Model은 DB조작에 밀접한 관계를 가지고 있다.

모델의 필드가 수정되거나 하는 것들은 마이그레이션 파일 등을 통해서 자동으로 관리되며 

모델 자체가 변화하면 별도의 수작업이 필요하다.

<br>

Q. 그렇다면 왜 AbstractUser를 상속받을까? User를 상속받으면 안되나?

* UserCreationForm의 custom?
  * UserCreationForm => Modelform을 상속 받아서 만들고 있다
  * ModelForm을 정의할 때 가장 중요했던 설정 = 모델, 필드
* get_user_model의 사용 이유?
  * User 모델은 결국 변경이 가능한 친구면서 django+사용자가 쓰는 것
  * 결국에는 변경 가능한 것은 변수화를 통해서 호출하도록 하는게 가장 좋다. -> 범개발영역에서의 핵심
  * url에 name을 붙여두고 함수로 해석해서 사용하는게 좋다
  * redirect('articles:index') -> /articles/
  * 유저 모델 클래스는 어딘가에 있겠지만 이것을 get_user_model() 을 호출해서 사용, 그러면 알아서 AUTH_USER_MODEL에 정의된 클래스를 준다.