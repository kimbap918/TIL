# 1. 라이브러리 불러오기
import FinanceDataReader as fdr
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras
from keras import layers

# 2. 전역 변수 설정
windowSize = 30 # 한달

# 3. 데이터 불러오기
df_data = fdr.DataReader('005930')

print(df_data)
print(type(df_data))

# 4. 판다스 -> 넘파이형태로 변환
df_numpy = df_data[['Open', 'High', 'Low', 'Volume', 'Close']].to_numpy()
print(df_numpy)
print(type(df_numpy))
print(df_numpy.shape)

# 5. 학습데이터와 평가데이터로 분리( 8:2, 7:3 )
trainSize = int(len(df_numpy) * 0.7)
print("훈련데이터 : ", trainSize)
testSize = int(len(df_numpy) * 0.3)
print("평가데이터 : ", testSize)

# 6. 데이터 분리
trainSet = df_numpy
testSet = df_numpy[trainSize-windowSize:]
print("훈련데이터셋 :", len(trainSet))
print("평가데이터셋 :", len(testSet))

# 6. 정규화 처리 ( 0 ~ 1 사이의 데이터로 정규화 처리 )
def MinMaxScaler(data):
    print(np.max(data, 0))
    print(np.min(data, 0))
    sp1 = np.max(data, 0) - np.min(data, 0)
    sp2 = data-np.min(data, 0)

    return sp2/sp1 # 0~1 사이의 실수로 변환

# 7. 찾은 데이터의 값을 복원
def rollBackMinMax(data, value):
    diff = np.max(data, 0)-np.min(data, 0)
    backupData = value * diff + np.min(data, 0)

    return backupData

# 8. 데이터 정규화
trainSet1 = MinMaxScaler(trainSet)
print("trainSet1 = ", trainSet1)
testSet1 = MinMaxScaler(testSet)
print("testSet1 = ", testSet1)

# 9. WindowCreate 함수
# 30일간 생성되는 윈도우 제작
# xdata = ['Open','High', 'Low', 'Volume'] => 문제
# ydata = ['Close'] => 답
def WindowCreate(data, seqLen):
    xdata = []
    ydata = []

    # 반복 범위(for문에서 사용할 반복범위)
    dataMax = len(data) - seqLen
    print("반복 횟수 :", dataMax)

    for i in range(0, dataMax):
        # 문제와 답을 분리
        dataX = data[i:i+seqLen,:-1]
        dataY = data[i+seqLen, [-1]]
        # print("윈도우제작 X :", dataX)
        # print("윈도우제작 y :", dataY)
        # print(data[i:i+seqLen])
        xdata.append(dataX)
        ydata.append(dataY)

    return np.array(xdata), np.array(ydata)

# 10. 윈도우(Window) 만들기
trainX, trainY = WindowCreate(trainSet1, windowSize)
testX, testY = WindowCreate(testSet1, windowSize)

# print(trainX)
# print(trainY)
print(trainX.shape, trainY.shape)
# print(testX)
# print(testY)
print(testX.shape, testY.shape)

##################################################
# 11. RNN 모델 설계
##################################################
model = keras.Sequential()

model.add(layers.SimpleRNN(
    units=10,
    activation='tanh',
    input_shape=[windowSize, 4]
))

model.add(layers.Dense(1))
model.summary()

# 모델 컴파일
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

# 모델 훈련하기
history = model.fit(trainX, trainY, epochs=200, batch_size=16)

# 테스트
result = model.evaluate(testX, testY, batch_size=16)
print('테스트 결과 loss = {}, mae = {}'.format(result[0], result[1]))

# 결과 예측
prediction = model.predict(testX)
# print("실제 예측값 :", testY)
# print("예측 결과값 :", prediction)

# 실제 정확도를 측정(MAE : Mean Absolute Error)
print("모델 정확도 : ", np.average( (prediction-testY)**2 ))

# 모델 예측값
rollback_prediction = rollBackMinMax(testSet[:,[-1]], prediction)
rollback_test = rollBackMinMax(testSet[:,[-1]], testY)
print("예측값 : ", rollback_prediction)
print("실제값 : ", rollback_test)

# 결과 예측 내일 주가
reuslt_pre = format(int(rollback_prediction[-1]), ',')
print(f"내일 삼성전자 주가 : {reuslt_pre}원 입니다.")
