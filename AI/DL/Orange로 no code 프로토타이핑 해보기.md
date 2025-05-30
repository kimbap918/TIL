

1. Data -> File을 선택
![](https://i.imgur.com/2Zp9Z21.png)



2. csv파일을 선택해서 file에 삽입
![](https://i.imgur.com/xPikYxf.png)



3. Concatenate : 불러온 데이터를 합친다.
![](https://i.imgur.com/JUXjNnF.png)

![](https://i.imgur.com/nutIuIz.png)



4. Concatenate를 더블클릭해서 feature 생성
![](https://i.imgur.com/vERAKYV.png)

![](https://i.imgur.com/0RboMuk.png)



5. Select Columns -> Features와 Target설정
![](https://i.imgur.com/3zTbaaj.png)


6. Data Sampler -> Fixed proportion of data : 훈련, 테스트 데이터셋 분리
![](https://i.imgur.com/SOOaE2e.png)


7. Model -> SVM, Random Forest, Neural Network 
![](https://i.imgur.com/GHIeDn6.png)



8. Random Forest -> Number of attributes considered at each split이 2인 이유는 현재 feature가 3개 이므로 랜덤으로 3개를 선택하면 전부를 선택하는것과 같아서 3보다 작은 값으로 선택한다.
![](https://i.imgur.com/W4quTAC.png)


9. Neural Network -> Neurons in hidden layers 에서 100, 50등으로 콤마로 나누는건 레이어를 새로 쌓기위해.
![](https://i.imgur.com/yWkcjcf.png)



10. Evaluate -> Predictions를 생성해 SVM, Random Forest, Neural Network, Data Sampler를 연결
Data Sampler의 Edit Links의 연결 변경
![](https://i.imgur.com/2qn4XyC.png)



## Orange에서 이미지 처리하기

1. option -> add-on -> Image Analytics 설치
![](https://i.imgur.com/pBKXRKC.png)


2. Import Images -> 사진이 든 폴더 선택
![](https://i.imgur.com/GSymUUC.png)



3. Image Viewer -> Import Images연결
![](https://i.imgur.com/ZkmvyJY.png)



4. Image Embedding -> Import된 이미지 연결
![](https://i.imgur.com/HedpZSp.png)



5. Image Embedding한 결과를 Data Table에 넣어보면 2048개의 feature에 대해 flatten한 값이 n0~n2047까지 나온다.
![](https://i.imgur.com/AjZsiT8.png)



6. Data Sampler로 training, test데이터 split후  Neural Network 연결
![](https://i.imgur.com/KgAIfC1.png)



##   Microsoft Machine Learning Studio (classic)

1. 로그인 후 Blank Experiment 클릭
![](https://i.imgur.com/ZdmzErL.png)



2. titanic azure classic 구글 검색 후 Azure AI Gallery 의 Titanic 1 Open in Studio 클릭
![](https://i.imgur.com/8qr9LJ2.png)
![](https://i.imgur.com/gC567qx.png)



3. 불러온 Titanic 1의 화면
![](https://i.imgur.com/rAsPMsY.png)



4. 클릭 후 오른쪽을 보면 데이터셋의 정보를 볼 수 있다.
![](https://i.imgur.com/yV4QfPv.png)



5. 오른쪽 클릭 후 Dataset -> Visualize를 클릭하면 시각화 할 수 있다.
![](https://i.imgur.com/2L2yFse.png)
![](https://i.imgur.com/lOjHEAv.png)




6. Select Columns in Dataset -> Launch column selector
![](https://i.imgur.com/5nOMgTR.png)
![](https://i.imgur.com/HEw8sEp.png)



7. Edit Metadata
* Data type : 데이터 타입
* Categorical : 데이터 특성 
* Fields : 데이터 필드
* New column names : 칼럼 명 변경
![](https://i.imgur.com/bG6Zqow.png)



8. Missing Values Scrubber
* For missing values : 결측값에 대한 처리
* Cols with all MV : 모든 값이 결측값인 값에 대한 처리
* MV indicator column : 결측값을 나타내는 특별한 열(column)을 만들거나 사용하는 것
![](https://i.imgur.com/x1bnQSH.png)



9. Split Data 
![](https://i.imgur.com/PwOs2en.png)



10. model 선택
![](https://i.imgur.com/57nHAHq.png)



11. 설정 후 run
![](https://i.imgur.com/Dem4epr.png)
