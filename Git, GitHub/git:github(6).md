# git 참고 - pull request



## 목적

A뿐만 아니라 B도 로컬 저장소에 브랜치를 생성해서 같은 원격 저장소에 푸시하는 경우에 충돌이 일어날 수 있기때문에 pull request를 통해 원격 저장소에 요청하고 원격 저장소에서 merge 하는것



## 사용 방법



### 1. Fork

- 가져오고자 하는 저장소를 자신의 저장소로 Fork한다.

![](https://i.imgur.com/xOCqqI8.png)



### 2. 내 컴퓨터의 로컬저장소에 원격저장소를 추가(clone)

- Fork로 생성한 저장소에서 `clone or download` 버튼을 누르고 표시되는 URL을 복사한다. 

```bash
$ git clone {복사한 URL}

/Users/mac - (main) > cd Desktop # Desktop으로 이동 후 폴더 생성
$ git clone https://github.com/kimbap918/pull_folder.git
```

![](https://i.imgur.com/gMlNnPE.png)

``` bash
mac/Desktop - (main) > cd pull_folder # 폴더 생성 후 생성된 폴더 내로 이동
Desktop/pull_folder - (master) > 
```



### 3. branch 생성

* 내 컴퓨터의 clone된  저장소(origin)에서 코드를 수정하거나 추가하는 작업은 branch를 만들어서 진행한다.

```bash
$ git branch {branch name}
$ git branch example

Desktop/pull_folder - (master) > git branch example
```



* 생성 후 이동

```bash
$ git checkout {branch name}
$ git checkout example

Desktop/pull_folder - (master) > git checkout example
Switched to branch 'example'
Desktop/pull_folder - (example) > # master -> example로 branch가 이동됨
```



* 생성된 폴더의 모습

![스크린샷 2022-07-07 오후 7.56.49](git:github(6).assets/스크린샷 2022-07-07 오후 7.56.49.png)



### 4. 수정 작업 후 add, commit, push

* 작업물을 추가

![](https://i.imgur.com/nJekzbi.png)

``` bash
Desktop/pull_folder - (example) > git add .
Desktop/pull_folder - (example) > git commit -m "request"
Desktop/pull_folder - (example) > git push origin example
```

* 작업이 완료되면 Github Repository(origin)에 add, commit, push한다.

* push할때 develop 브랜치의 수정내역을 origin으로 푸시한다.

  

### 5. pull Request 생성

- push 완료후 자신의 github 저장소에서 `Compare & pull request`버튼이 활성화 되어있는걸 확인할 수 있다.
- 버튼을 선택해 Pull Request를 생성한다.

![](https://i.imgur.com/5jDeKx1.png)



* 내용을 작성 후 pull request 를 생성

![](https://i.imgur.com/57ienZg.png)



### 6. Merge Pull Request

- PR을 받은 관리자는 코드 변경내역을 환인하고 Merge여부를 결정하게 된다.

  

### 7. Merge 이후 동기화 및 branch 삭제

- Merge가 완료되면 로컬 코드와 원본의 코드를 병합하고 최신의 상태를 유지하게 위해 동기화한다.
- upstream 확인

```bash
$ git remote -v  
```

- upstream 추가

```bash
$ git remote add upstream
$ git fetch upstream
$ git merge upstream/master
$ git branch -d example
```

- 위 명령어를 통해 동기화하고, 브랜치를 삭제한다.