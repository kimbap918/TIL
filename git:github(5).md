# git(5) - merge🤝



## merge?

merge는 branch로 분기된 각 commit을 하나로 다시 합치고싶을 때 사용하는 명령어이다.





## 1. 명령어

1. branch 병합

   * master에 merge가 완료되었으면 branch를 삭제해도 된다.

   ``` bash 
   (master) $ git merge {branch name}
   (master) $ git merge example 
   ```

   

2. merge 취소

   ``` bash
   (master) $ git merge --abort 
   ```



3. 병합하면서 해당 branch는 기록을 남기고 싶을때

   ``` bash
   (master) $ git merge --no-ff
   ```

4. branch 확인

   ``` bash
   $ git branch --merged # 현재 브랜치에 머지가 된 브랜치 확인
   $ git branch --no-merged # 마스터 브런치에서 파생된 브랜치 학인
   ```

   

## 2. branch 병합 시나리오

> branch 관련된 명령어는 간단하다.
>
> 다양한 시나리오 속에서 어떤 상황인지 파악하고 자유롭게 활용할 수 있어야 한다.

### 상황 1. fast-foward

> fast-foward 란 뿌리가 되는 master브랜치에 변화가 주어지지 않은 채 다른 변화가 생긴 브랜치로 머지를 하게 되는 것.
>
>  새로운 커밋이 생성되지 않고 **HEAD**의 위치만 변한 채 머지를 한 대상 브랜치의 마지막 커밋에 master 브랜치가 자리잡게 된다.

### head?

``` bash
d7afaf1 (HEAD -> master) add README # 예시
```

> 내가 이동한 Commit의 정보를 표시, 위 예시는 master에 위치해 있음을 나타낸다.



1. feature/home branch 생성 및 이동

   ```bash
   (master) $ git branch feature/home
   (master) $ git checkout feature/home
   ```

   

2. 작업 완료 후 commit

   ```bash
   (feature/home) $ touch home.txt
   (feature/home) $ git add .
   (feature/home) $ git commit -m 'Add home.txt'
   (feature/home) $ git log --oneline
   b534a34 (HEAD -> feature/home) Complete Home!!!!
   e89616a (master) Init
   ```




3. master 이동

   ```bash
   (feature/home) $ git checkout master
   (master) $ git log --oneline
   ```




4. master에 병합

   ```bash
   (master) $ git merge feature/home 
   Updating e89616a..b534a34
   Fast-forward
    home.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 home.txt
   ```

   


5. 결과 : fast-foward

   ```bash
   (master) $ git log --oneline
   b534a34 (HEAD -> master, feature/home) Complete Home!!!!
   e89616a Init
   ```

   

6. branch 삭제

   ```bash
   (master) $ git branch -d feature/home 
   Deleted branch feature/home (was b534a34).
   ```

   

---

### 상황 2. merge commit

> 서로 다른 이력(commit)을 병합(merge)하는 과정에서 **다른 파일이 수정**되어 있는 상황
>
> git이 auto merging을 진행하고, **commit이 발생된다.**

1. feature/about branch 생성 및 이동

   ```bash
   (master) $ git checkout -b feature/about
   (feature/about) $
   ```

   

2. 작업 완료 후 commit

   ```bash
   (feature/about) $ touch about.txt
   (feature/about) $ git add .
   (feature/about) $ git commit -m 'Add about.txt'
   (feature/about) $ git log --oneline
   5e1f6de (HEAD -> feature/about) 자기소개 페이지 완료!
   b534a34 (master) Complete Home!!!!
   e89616a Init
   ```

   

3. master 이동

   ```bash
   (feature/about) $ git checkout master
   (master) $
   ```

   

4. master에 추가 commit을 발생시킨다.

   * **다른 파일을 수정 혹은 생성할것.**

   ```bash
   (master) $ touch master.txt
   (master) $ git add .
   (master) $ git commit -m 'Add master.txt'
   (master) $ git log --oneline
   98c5528 (HEAD -> master) 마스터 작업....
   b534a34 Complete Home!!!!
   e89616a Init
   ```

   

5. master에 병합

   ```bash
   (master) $ git merge feature/about
   ```

   

6. 결과 -> 자동으로 *merge commit 발생*

   

7. 커밋 및 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   *   582902d (HEAD -> master) Merge branch 'feature/about'
   |\
   | * 5e1f6de (feature/about) 자기소개 페이지 완료!
   * | 98c5528 마스터 작업....
   |/
   * b534a34 Complete Home!!!!
   * e89616a Init
   ```

   

8. branch 삭제

   

   ```bash
   $ git branch -d feature/about 
   Deleted branch feature/about (was 5e1f6de).
   ```

   

---

### 상황 3. merge commit 충돌

> 서로 다른 이력(commit)을 병합(merge)하는 과정에서 **같은 파일의 동일한 부분이 수정**되어 있는 상황
>
> git이 auto merging을 하지 못하고, 충돌 메시지가 뜬다.
>
> 해당 파일의 위치에 표준형식에 따라 표시 해준다.
>
> 원하는 형태의 코드로 직접 수정을 하고 직접 commit을 발생 시켜야 한다.

1. feature/test branch 생성 및 이동

   ```bash
   (master) $ git checkout -b feature/test
   ```

   

2. 작업 완료 후 commit

   ```bash
   # README.md 파일 열어서 수정
   (feature/test) $ touch test.txt
   (feature/test) $ git add .
   (feature/test) $ git commit -m 'Add test.txt'
   (feature/test) $ git log --oneline
   95fad1c (HEAD -> feature/test) README 수정하고 test 작성하고
   582902d (master) Merge branch 'feature/about'
   98c5528 마스터 작업....
   5e1f6de 자기소개 페이지 완료!
   b534a34 Complete Home!!!!
   e89616a Init
   ```


3. master 이동

   ```bash
   $ git checkout master
   ```

   


4. master에 추가 commit을 발생시키기

   * **동일 파일을 수정 혹은 생성해야한다.**

   ```bash
   # README.md 파일 열어서 수정
   (master) $ git add README.md
   (master) $ git commit -m 'Update README.md'
   ```

   

5. master에 병합

   ```bash
   (master) $ git merge feature/test 
   Auto-merging README.md
   CONFLICT (content): Merge conflict in README.md
   Automatic merge failed; fix conflicts and then commit the result.
   ```

   


6. 결과 -> *merge conflict발생*

   > git status 명령어로 충돌 파일을 확인할 수 있음.

   ```bash
   (master|MERGING) $ git status
   On branch master
   You have unmerged paths.
     (fix conflicts and run "git commit")        
     (use "git merge --abort" to abort the merge)
   
   Changes to be committed:
           new file:   test-1.txt
           new file:   test-2.txt
           new file:   test.txt
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both modified:   README.md
   ```

   


7. 충돌 확인 및 해결

   ```
   <<<<<<< HEAD
   # 마스터에서 작업함...
   =======
   # 테스트에서 작성
   >>>>>>> feature/test
   ```

   


8. merge commit 진행

   ```bash
   (master|MERGING) $ git add .
   (master|MERGING) $ git commit
   ```

   * vim 편집기 화면이 나타난다.

     * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료.
     * `w` : write
     * `q` : quit

   * vs code 편집기에서 메시지보고 닫을것.

     

9. 커밋 및 확인하기

   ```bash
   (master) $ git log --oneline --graph
   *   bc1c0cd (HEAD -> master) Merge branch 'feature/test'
   |\  
   | * 95fad1c (feature/test) README 수정하고 test 작성하고
   * | 2ecad28 리드미 수정
   |/  
   *   582902d Merge branch 'feature/about'
   |\  
   | * 5e1f6de 자기소개 페이지 완료!
   * | 98c5528 마스터 작업....
   |/  
   * b534a34 Complete Home!!!!
   * e89616a Init
   ```




10. branch 삭제

    ```bash
    (master) $ git branch -d feature/test
    ```






#### merge에 관한 참고하기 좋은 자료

https://otzslayer.github.io/git/2021/12/05/git-merge-fast-forward.html







