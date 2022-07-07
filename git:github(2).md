# git(2) - 원격저장소(emote Repository)



## 원격저장소(Remote Repository)

네트워크를 활용한 저장소

git(1)에서는 로컬저장소와 로컬저장소에서 사용되는 명령어를 사용했다.



## 기본 흐름

1. 원격 저장소를 만들고
2. 로컬 저장소의 commit을 push하여 원격저장소로 보낸다.
3. 원격 저장소의 버전을 로컬 저장소로 가져온다(pull)



 ## 원격 저장소 생성

1. New Repository 클릭

![스크린샷 2022-07-06 오전 11.31.18](git:github(2).assets/스크린샷 2022-07-06 오전 11.31.18.png)



2. 저장소 설정

   ![스크린샷 2022-07-06 오전 11.47.12](git:github(2).assets/스크린샷 2022-07-06 오전 11.47.12.png)

* Repository name 저장소 이름
* Description 저장소에 대한 설명 
* public / private 공개 설정 여부

설정 후 Create Repository 클릭



3. 생성 화면

![스크린샷 2022-07-06 오전 11.50.16](git:github(2).assets/스크린샷 2022-07-06 오전 11.50.16.png)

* https://github.com/kimbap918/dukbokki.git

  여기서 kimbap918은 깃허브 유저 이름, dukbokki.git은 저장소 이름이다.

  

4. 로컬저장소의 버전을 원격 저장소로 보내주기

   ![스크린샷 2022-07-06 오전 11.55.16](git:github(2).assets/스크린샷 2022-07-06 오전 11.55.16.png)

``` bash
$ git remote add origin https://github.com/kimbap918/dukbokki.git
```



5. 로컬 저장소의 commit을 push하기

   ``` bash
   $ git push -u origin main
   ```

* push 하기 전, 반드시 commit이 되어있어야한다.



## 명령어

1. push

   ``` bash
   $ git push <원격저장소이름> <브랜치이름>
   $ git push origin main
   ```

   * 원격 저장소로 로컬 저장소 변경 사항(commit)을 올림(push)
   * 로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라간다.

2. pull 

   ``` bash
   $ git pull <원격저장소이름> <브랜치이름>
   $ git pull origin main
   ```

   * 원격 저장소로 부터 변경된 내역을 받아와서 이력을 병합하는것

     

3. clone

   ``` bash
   $ git clone <원격저장소주소>
   $ git clone https://github.com/kimbap918/dukbokki.git
   ```

   * 원격 저장소를 복제하여 가져오는것

   

4. remote

   ``` bash
   $ git remote -v
   ```

   * 원격 저장소 정보를 확인

   ``` bash
   $ git remote add <원격저장소> <url>
   ```

   * 원격 저장소 추가(일반적으로 origin)

   ``` bash
   $ git remote rm <원격저장소>
   ```

   * 원격저장소 삭제

   

