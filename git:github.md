# git(1) - git에 대해



## git의 목적?

git은 분산버전관리시스템으로 코드의 버전을 관리하는 도구다.

컴퓨터 파일의 변경사항을 추적하고 여러 사용자들 간에 해당 파일들의 작업을 조율하는 목적으로 사용한다.

분산버전관리시스템(DVCS)은 원격저장소를 통해 협업하고 모든 히스토리를 사용자들이 공유하는 시스템이다.



## 기본 흐름

git은 나무와 비슷한것 같다. 하나의 작업(master)에서 독립적으로 어떤 작업을 진행하기 위해 갈래를 생성하는것을 브랜치(branch)라고 부르며, git 에 관리되는 소스들을 조금 더 쉽게 활용하기 위한 GUI 툴의 이름은 sourcetree다.

git의 로컬 저장소는 크게 3가지로 나눠져있는데, 

1. working directory 작업(수정)한 파일을 

2. INDEX(staging area)에 모아(add),

3. 버전으로 남긴다(commit).



## 명령어

1. git init - 저장소 만들기

   ``` bash
   $ git init
   ```

   * git 저장소를 처음 생성하는것(초기화). 초기화를 시키면 해당 디렉토리를 git 저장소로 등록해준다.

     

2. git add 파일명 

   ``` bash
   $ git add .
   ```

   * working directory 상의 변경 내용을 staging area에 추가하기 위해 사용하는 명령어.

   * 폴더 내의 파일 전체를 add하려면 `.`을 입력하면 된다.

     

3. git commit -m '커밋메시지'

   ``` bash
   $ git commit -m 'commit입니다.'
   ```

   * stage에 등록된 상태의 파일들을 커밋을 통해 버전으로 기록하는 명령어.
   * 커밋 메시지는 변경 사항을 알 수 있도록 명확하게 작성하는것이 좋다.
   * 

4. git log, git log -1, git log --oneline, git log -1 oneline

   ``` bash
   $ git log
   $ git log -1
   $ git log --oneline
   $ git log -1 --oneline
   ```

   * 저장소의 커밋 히스토리를 조회하게 해준다.

   * 특별한 옵션 없이 git log 명령을 실행하면 저장소의 커밋 히스토리를 시간순으로 나타낸다.

   * -1 은 최근 한 개의 결과만 보여주는 옵션이다.

   * oneline은 결과값을 한 줄로 나타내는 옵션이다.

     

5. git status - 현재 상태 확인

   ``` bash
   $ git status
   ```
   
   * 파일들의 상태를 확인할 수 있다.
   
   * 작업 디렉토리(working directory)와 스테이징 영역(staging area)의 상태를 확인하기 위해 사용한다.
   
     
   
     
   
     ## 예시
   
   * a.txt 파일을 만든 직후
   
     ``` bash
     $ git status
     On branch master
     
     # 트래킹이 되고 있지 않은 파일?
     # => working directory
     # => 한번도 git으로 관리되고 있지 않은 파일!
     Untracked files:
     (use "git add <file>..." to include in what will be committed)
      a.txt
      
     # 커밋할 것은 없어
     # 하지만 트래킹되지 않은 파일은 존재한다.
     # git add 사용해서 트래킹해
     nothing added to commit but untracked files present (use "git add" to track)
     ```
   
   * b.txt 파일을 만들고 add한 이후

     ``` bash
     $ git stagus
     On branch master
     Changes to be Committed:
     (use "git restore --staged <file>..." to unstage)
     new file: b.txt
     
     Untracked files:
     	(use "git add <file>..." to include in what will be committed)
     	 a.txt
     ```
   
   * a.txt 파일과 b.txt 파일을 모두 add한 이후 커밋까지
   
     ``` bach
     $ git status
     On branch master
     
     nothing to commit, working tree clean
     ```
   
     