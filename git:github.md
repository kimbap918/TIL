## GIT

### git은 분산 버전 관리시스템입니다.

1. git init

2. git add 파일명

3. git commit -m '커밋메시지'

4. git log, git log -1, git log --oneline, git log -1 oneline

5. git status

   * a.txt 파일을 만든 직후

     ``` bash
     $ git status
     On branch master
     
     # 트래킹이 되고 있지 않은 파일?
     # => 1통 (working directory)
     # => 한번도 git으로 관리되고 있지 않은 파일!
     Untracked files:
     (use "git add <file>..." to include in what will be committed)
      a.txt
      
     # 커밋할 것은 없어 => 2통이 비어있어
     # 하지만 트래킹되지 않은 파일은 존재한다.
     # git add 사용해서 트래킹해 
     nothing added to commit but untracked files present (use "git add" to track)
     ```

   * b.txt 파일을 만들고 add한 이후

     > 초록글씨 => 2통

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
     # 2통, 1통 모두 클린~!
     nothing to commit, working tree clean
     ```

     