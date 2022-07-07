# git(4) - branch🌲🍆



## branch?

소프트웨어 개발 시 개발자들은 동일한 소스코드를 공유해서 다루게 된다. 만일 여러 사람이 **동일한 소스코드를 기반으로 서로 다른작업을 하게되는 경우에는 각각 서로 다른 버전의 코드가 여러갈래로 나올 수 밖에 없다.**

이런 경우에 **개발자들이 동시에 다양한 작업을 할 수 있게 해주는 기능이 브랜치(branch)다.** 브랜치는 각자 독립적인 작업 영역(repository) 안에서 소스코드를 변경할 수 있다. 또한, 작업 후에 원래 버전과 비교 해 다른 하나의 새로운 버전을 만들어 낼 수 있다.



## 1. branch 관련 명령어

> Git branch를 위해 root-commit(최초 커밋)이 필요하다.

1. branch 생성

   * branch name 미 입력시 브랜치 목록 조회

   ``` bash
   (master) $ git branch {branch name}
   (master) $ git branch --all # 서버에 있는 모든 브랜치 목록 확인
   (master) $ git branch example
   ```

2. branch 이동

   ``` bash
   (master) $ git checkout {branch name}
   (master) $ git switch {branch name}
   (master) $ git checkout example
   ```

3. branch를 생성하면서 이동(생성과 이동 동시에)

   ``` bash
   (master) $ git checkout -b {branch name}
   (master) $ git switch -b {branch name}
   (master) $ git checkout -b example
   ```

4. branch 삭제

   ``` bash
   (master) $ git branch -d {branch name}
   (master) $ git push origin --delete # 서버에 있는 브랜치 삭제
   (master) $ git branch -d example
   ```

5. branch 목록

   ``` bash
   (master) $ git branch
   ```





git(5) - merge에서 계속



