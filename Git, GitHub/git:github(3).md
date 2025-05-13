# git(3) - clone



## 명령어 clone에 관해

clone은 원격 저장소를 복제하여 가져오는것이다.

``` bash
$ git clone <원격저장소주소>
$ git clone https://github.com/kimbap918/dukbokki.git
```

![](https://i.imgur.com/b4MQaas.png)

원격 저장소를 보면 Clone 할 수 있는 주소와 Download ZIP이 있다. 

두가지 다 실행 시 폴더를 받아오지만 다른점이 있다.



1. Clone

   ``` bash
   Desktop/test_folder - (main) > git clone https://github.com/kimbap918/TIL.git
   Cloning into 'TIL'...
   remote: Enumerating objects: 125, done.
   remote: Counting objects: 100% (125/125), done.
   remote: Compressing objects: 100% (101/101), done.
   remote: Total 125 (delta 14), reused 123 (delta 12), pack-reused 0
   Receiving objects: 100% (125/125), 1.24 MiB | 2.29 MiB/s, done.
   Resolving deltas: 100% (14/14), done.
   ```

   ![](https://i.imgur.com/d77H9Ab.png)확인해보면 .git 폴더가 있다.



2. Download ZIP

   ![](https://i.imgur.com/81lzPRE.png)

   ZIP 파일은 .git 폴더가 없다.



.git 폴더가 없다는것은, Download ZIP으로 생성된 폴더는 git으로 관리가 안된다는 뜻이다. 이 점을 유의하자.



### 그렇다면 pull과의 차이는?

clone과 pull모두 원격 저장소에서 받아온다는 점에서 헷갈릴 수 있다.

clone은 **저장소 그 자체**를 받아오는것이고(폴더)

pull은 저장소 내의 **변경된 커밋**을 받아온다.(내용)

