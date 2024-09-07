

1. 작업할 로컬 브랜치를 생성합니다.(이름 자유)

```shell
git checkout -b choi
```
<img width="487" alt="Screenshot 2024-08-08 at 3 46 02 PM" src="https://github.com/user-attachments/assets/eb589686-0227-4d25-a42a-869f2700c205">



2. 작업 변경사항을 로컬 브랜치에 add, commit 합니다.

```shell
git add . # 작업 내용 전체를 추가
git commit -m "message" # commit -m(메시지) "작업 내용"
```
<img width="508" alt="Screenshot 2024-08-08 at 3 44 23 PM" src="https://github.com/user-attachments/assets/8223782a-cce7-4a9f-b360-b4855e92d9e9">



3. commit한 내용을 자신의 로컬 브랜치에 push한다.

```shell
git push origin choi
```
<img width="493" alt="Screenshot 2024-08-08 at 3 48 44 PM" src="https://github.com/user-attachments/assets/44939b37-b9f8-4691-b396-5e0ff2763ad5">



4. 작업중인 팀의 원격 저장소로 이동하면 Compare & pull request가 뜹니다.
<img width="1108" alt="Screenshot 2024-08-08 at 3 24 12 PM" src="https://github.com/user-attachments/assets/7c548e0b-87ec-45b1-8308-13ec52cb15ad">

5. compare할 브랜치와 병합될 브랜치를 확인 후 pull request를 합니다.
<img width="773" alt="Screenshot 2024-08-08 at 3 25 49 PM" src="https://github.com/user-attachments/assets/e3fca7e3-31af-4ebf-9293-5a91ba6d0f21">

6. 병합에 이상이 없는지 검수 후 merge를 합니다. 병합 후에는 branch를 삭제합니다.
<img width="773" alt="Screenshot 2024-08-08 at 3 31 35 PM" src="https://github.com/user-attachments/assets/fbb0f20a-d456-444d-bedb-7af64b3c7526">


7. 로컬 저장소에서 main으로 돌아와서 원격 저장소의 내용을 업데이트 합니다.
``` shell
git checkout main
git pull origin main # 원격 저장소의 내용을 로컬에서 최신화
```
<img width="549" alt="Screenshot 2024-08-08 at 3 32 27 PM 1" src="https://github.com/user-attachments/assets/50213f60-6391-4492-bf41-f2591cf4d069">



8. 사용했던 브랜치를 삭제합니다.
``` Shell
git branch -D choi
```
<img width="480" alt="Screenshot 2024-08-08 at 3 58 07 PM" src="https://github.com/user-attachments/assets/7562d765-5eae-47d8-94e6-5a0e8f212c8b">



9. 1의 내용을 다시 순서대로 반복합니다. 
