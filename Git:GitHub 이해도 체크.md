# Git/Github 이해도 체크업

오늘은 수강중인 교육과정에서 간단한 이해도 점검을 했다.

짧지만 몇 가지 문제가 있으니 보면서 다시 상기시켜도 좋을것같다.



## Q1. Git은 무엇인지 작성해주세요

<details markdown="1">
<summary>확인</summary>

분산버전관리시스템(DVCS)

</details>

<details markdown="1">
<summary>접기/펼치기</summary>


분산버전관리시스템(DVCS)

</details>



## Q2. Staging Area(임시공간)의 의미를 작성해주세요.

<details markdown="1">
<summary>접기/펼치기</summary>


Commit을 하기위해 `$ git add` 명령어로 추가한 파일들이 모여있는 공간

</details>



## Q3. 작업이 완료 되었을 때, 버전을 기록하는 과정을 명령어로 작성하고, 커밋이 가지는 의미가 무엇인지 작성해주세요.

<details markdown="1">
<summary>접기/펼치기</summary>


``` bash
$ git add {파일명}
$ git status # 난 이걸 빠트렸다. add 후에 꼭 확인하는 습관을 가지자.
$ git commit -m "메시지 내용"
$ git push {원격저장소이름} {브랜치이름}
```

commit은 `$ git add` 로 모여있는 파일들에 대한 확정을 짓고 버전을 기록하는것이다.

</details>



## Q4. .gitignore를 활용하는 이유를 작성해주세요.

<details markdown="1">
<summary>접기/펼치기</summary>


git은 생성된 모든 하위 디렉토리의 파일을 추적하는데, .gitignore를 사용함으로서 원하지 않는 파일을 git에서 제외할 수 있기 때문이다.

</details>



## Q5. 커밋 내역을 확인하는 명령어는 `$ git ___ `이다.

<details markdown="1">
<summary>접기/펼치기</summary>


log

</details>



## Q6. 원격저장소를 제공하는 서비스는 Github 밖에 없다.

<details markdown="1">
<summary>접기/펼치기</summary>

X

</details>



## Q7. 아래의 이미지 오류의 원인과 해결방안을 작성하세요.

![스크린샷 2022-07-08 오후 6.29.01](/Users/mac/Library/Application Support/typora-user-images/스크린샷 2022-07-08 오후 6.29.01.png)

<details markdown="1">
<summary>접기/펼치기</summary>


github의 원격저장소에 내 로컬조정소에는 없는 파일이 있는 상태에서 push를 하는 경우 생기는 오류이다.

hint: 의 조언과 같이 git pull로 로컬저장소를 업데이트 한 후 push한다.

</details>



## Q8. 원격저장소 https://github.com/kimbap918/TIL.git 를 복제하기 위한 명령어를 작성해주세요.

<details markdown="1">
<summary>접기/펼치기</summary>



`$ git clone https://github.com/kimbap918/TIL.git`

</details>



## Q8-1 해당 명령어를 바탕화면에서 입력했을 때 저장소는?

1. 바로 바탕화면에서 활용 가능하다.
2. 바탕화면에 TIL 폴더가 생성되어 있다.

<details markdown="1">
<summary>접기/펼치기</summary>



2

</details>



## Q9. 브랜치를 사용하는 목적은 무엇인지 작성해주세요.

<details markdown="1">
  <summary>접기/펼치기</summary>



개발자 여러명이 협업으로 동일한 소스코드를 기반으로 해서 서로 다른 작업을 할 때에, 각각 서로 다른 버전의 소스코드가 여러가지로 나오게되는데 이러한 경우에 개발자들이 동시에 다양한 작업을 할 수 있게 해준다.

</details>



## Q10. merge conflict가 발생하였을 때 해야하는 일을 작성해주세요.

<details markdown="1">
<summary>접기/펼치기</summary>



1. 충돌한 내역을 확인하고
2. 충돌한 부분을 직접 수정하고
3. commit한다.

</details>



## Q11. GitHub에서 1) Shared Repository와 2) Fork & Pull Request의 차이점을 작성해주세요.

<details markdown="1">
<summary>접기/펼치기</summary>



권한의 차이. Shared Repository와는 다르게 Fork & Pull Request는 마음대로 수정, 삭제가 불가능하다. 그래서 원격 저장소를 Fork 한 후에 로컬 저장소로 가져와 clone하고 branch를 생성 한 뒤에 작업을 끝마치면 Pull Request를 하여 Fork한 원작자의 승인을 받으면 병합이 된다.

</details>

