## git으로 협업을 해봅시다

### git clone

1. 데스크탑의 로컬 저장소에 아래의 주소를 복사합니다.

![](https://i.imgur.com/2sb2sgq.png)


<br>

2. git bash 에서 **git clone https://github.com/be-farmer/tomato.git** 후 로컬 저장소에 폴더가 생성되었는지 확인합니다.

```
git clone https://github.com/be-farmer/tomato.git
```
![](https://i.imgur.com/SbcLMqc.png)
![](https://i.imgur.com/Oj6BM38.png)


<br>

### branch 사용하기
* 작업을 할 때 각자의 작업을 식별하고, 작업의 충돌을 방지하기 위해 branch를 사용합니다.

<br>

1. **git checkout -b 브랜치명** : 새 작업 시작시 git bash에서 브랜치 생성합니다.
``` bash
# 예시
git checkout -b choi
# 아래에서는 choi/branch로 생성했습니다.
```
![](https://i.imgur.com/JbO0ad6.png)

<br>

2.  **git add**  : 작업한 내용을 branch의 stage에 추가합니다. 
```bash
git add . # 브랜치에 변경된 작업 전부를 추가합니다.
```
* 작업물이 추가된 후에는 git status를 통해 어떤 부분이 변경되고 추가 되었는지 확인해보는게 좋습니다.
``` bash
git status
```
![](https://i.imgur.com/oxa8lls.png)

<br>

3. **git commit -m "브랜치명 커밋내용"** : stage에 추가된 작업물을 commit합니다.
```bash
# 예시
git commit -m "2019~2020 토마토 생산량 정보"
```
![](https://i.imgur.com/V3GZwyz.png)

<br>

5. **git push origin 브랜치명** : 브랜치에 커밋 된 작업을 push합니다.
``` bash
git push origin choi
```
![](https://i.imgur.com/TI7xlXa.png)

<br>

6. tomato의 repo에 가면 compare & pull request가 뜬걸 확인할 수 있습니다.
![](https://i.imgur.com/EldGfnb.png)
![](https://i.imgur.com/H1sfbMn.png)

create pull request를 합니다. 충돌이 없다면 초록색으로 Merge pull request가 뜹니다.

![](https://i.imgur.com/O57DWuh.png)

작업이 다 된 branch는 삭제해줍니다.
![](https://i.imgur.com/XA6mZM2.png)

<br>

git bash로 돌아옵니다.

7. **git checkout main** : 브랜치에서 메인으로 전환합니다.
* 여기서 main으로 돌아오면 branch의 작업 변경사항이 로컬의 메인에는 반영되어있지 않습니다.
* 그렇기 때문에 작업물을 원격저장소의 메인에서 가져와야 합니다.
``` bash
git checkout main
```
![](https://i.imgur.com/okbxPOT.png)

<br>

8. **git pull origin main** : 작업물 당겨오기 
``` bash
git pull origin main
```

로컬에 작업물을 업데이트 했습니다.
![](https://i.imgur.com/S1VkCew.png)


8. **git branch -d 브랜치명** : 작업했던 브랜치를 삭제합니다. 작업을 다시 시작할때는 branch를 새로 생성합시다.
``` bash
# 예시
git branch -d choi
```

<br>

### main에 바로 작업을 하고 push를 하면 안되는 이유

![](https://i.imgur.com/kr7mvF3.png)

협업을 하다보면 팀원 간 작업파일이 겹치는 경우가 종종 있습니다. 이런 경우에 충돌이 발생하기도 하는데, main에 작업물을 바로 푸시해버리면 충돌에 대한 대처가 힘들어집니다.

브랜치(나뭇가지)에서 작업을 해서 메인(기둥)에 작업이 완료된 것들을 푸시하는게 좋습니다.