2023.09.01

<br>

## 8-2 합성곱 신경망을 사용한 이미지 분류

<br>

understanding edge detection

https://medium.com/p/2aada303b900

<br>

### 합성곱(Convolution)
* 신호 처리, 이미지 처리, 음성 처리 등 다양한 분야에서 사용되는 연산 기법
* 입력 데이터 위에서 작은 커널(필터)을 슬라이딩하면서 커널과 입력 데이터의 해당 부분을 요소별로 곱한 뒤, 모든 곱셈 결과를 더해서 출력값을 계산하는 것
* perceptron = filter, cover, mask


![](https://i.imgur.com/s9eQBrO.png)

![](https://i.imgur.com/BvI8Yzl.png)

### 합성곱 신경망(Convolutional Neural Network, CNN)
* CNN은 합성곱 연산을 활용한 신경망의 한 종류로, 주로 컴퓨터 비전 분야에서 이미지 처리 작업에 사용된다.
* 이미지가 비정형적 데이터이기 때문에 특징을 뽑고, 분류한다.

1. 필터(커널) : 합성곱 계층(Convolutional Layer)에서 사용되는 작은 크기의 가중치 행렬, 일반적으로 필터는 2차원 행렬로 표현된다. 
2. 합성곱 계층(Convolutional Layer) : 입력 데이터에 여러 개의 필터(커널)를 적용하여 특징 맵(feature map)을 생성하고, 이를 통해 입력 데이터의 다양한 특징을 추출하는 계층
3. 특징 맵(Feature Map) : 합성곱 계층(Convolutional Layer)을 통해 추출된 특징들을 나타내는 맵 또는 2차원 배열

####  합성곱 신경망 (CNN)의 원리
![](convolution_schematic.webp)

1. **합성곱 계층 (Convolutional Layer)**: 이 계층은 입력 이미지에 여러 개의 필터(커널)를 적용하여 특징 맵(feature map)을 생성. 각 필터는 다양한 특징을 감지하는 역할을 수행하며, 여러 개의 필터를 사용하여 다양한 특징을 추출한다.

2. **활성화 함수와 풀링 계층 (Activation Function and Pooling Layer)**: 합성곱 계층 이후에는 활성화 함수를 적용하여 비선형성을 추가하고, 풀링(pooling) 계층을 통해 공간 해상도를 줄이고 중요한 정보를 보존한다. 대표적인 풀링 연산에는 최대 풀링(max pooling)이 있다.

> pooling에서 공간 해상도를 줄이는 이유? -> 계산 비용을 줄이고, 필터를 키우는 효과를 얻어 콧구멍에서 코로 점진적으로 확대해가며 특징을 얻어낼 수 있다.

3. **완전 연결 계층 (Fully Connected Layer)**: 합성곱 계층과 풀링 계층을 거치면서 추출된 특징을 바탕으로, 하나 이상의 완전 연결 계층이 사용된다. 이 계층은 분류나 회귀와 같은 최종 작업을 위해 필요한 출력을 생성한다.


```python
# 실행마다 동일한 결과를 얻기 위해 케라스에 랜덤 시드를 사용하고 텐서플로 연산을 결정적으로 만듭니다.
import tensorflow as tf

tf.keras.utils.set_random_seed(42)
tf.config.experimental.enable_op_determinism()
```

## 패션 MNIST 데이터 불러오기


```python
from tensorflow import keras
from sklearn.model_selection import train_test_split

(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

train_scaled = train_input.reshape(-1, 28, 28, 1) / 255.0

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)
```

    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-labels-idx1-ubyte.gz
    29515/29515 [==============================] - 0s 0us/step
    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-images-idx3-ubyte.gz
    26421880/26421880 [==============================] - 1s 0us/step
    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-labels-idx1-ubyte.gz
    5148/5148 [==============================] - 0s 0us/step
    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-images-idx3-ubyte.gz
    4422102/4422102 [==============================] - 1s 0us/step


## 합성곱 신경망 만들기


```python
model = keras.Sequential()
```


```python
# 32 : 필터(커널)의 개수 
# kernel_size : 필터의 크기 
# activation='relu' : 활성화 함수를 ReLU 사용, ReLU는 입력이 0보다 작으면 0으로 변환하고, 그 이상의 값은 그대로 출력하는 함수
# padding='same' : feature map을 입력 크기와 동일하게 유지하는 패딩 방식(0으로 채운다)
# input_shape = 입력 데이터의 형태. 여기서는 28x28 크기의 흑백 이미지 하나
model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu',
                              padding='same', input_shape=(28,28,1)))
```


```python
# MaxPooling을 통과시켜 28*28을 14*14로 만든다
model.add(keras.layers.MaxPooling2D(2))
```


```python
# kernel_size = (3, 3), 3 둘 다 같다.
model.add(keras.layers.Conv2D(64, kernel_size=(3,3), activation='relu',
                              padding='same'))
# 7*7
model.add(keras.layers.MaxPooling2D(2))
```


```python
model.add(keras.layers.Flatten())
# 7*7*64
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(10, activation='softmax'))
```


```python
model.summary()
```

> 바닐라 CNN은 컨볼루션 신경망의 기본적인 구조를 가진 모델

    Model: "sequential"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     # 32 * 9(필터) = 288+절편(32) = 320 
     conv2d (Conv2D)             (None, 28, 28, 32)        320       
                                                                     
     max_pooling2d (MaxPooling2D  (None, 14, 14, 32)       0         
     )                                                               
                                                                     
     # 32 * 64 * 9(필터) + 64(절편) = 18,496 
     conv2d_1 (Conv2D)           (None, 14, 14, 64)        18496     
                                                                     
     max_pooling2d_1 (MaxPooling  (None, 7, 7, 64)         0         
     2D)                                                             
     # 7 * 7 * 64                                                    
     flatten (Flatten)           (None, 3136)              0         
     # 3136 * 100 + 100                                              
     dense (Dense)               (None, 100)               313700    
                                                                     
     dropout (Dropout)           (None, 100)               0         
     # 100 * 10 + 10                                                 
     dense_1 (Dense)             (None, 10)                1010      
                                                                     
    =================================================================
    Total params: 333,526
    Trainable params: 333,526
    Non-trainable params: 0
    _________________________________________________________________



```python
keras.utils.plot_model(model)
```

![](https://i.imgur.com/2AZu3KT.png)




```python
keras.utils.plot_model(model, show_shapes=True)
```

![](https://i.imgur.com/XgSW3pG.png)




## 모델 컴파일과 훈련


```python
# 최적화 알고리즘 : Adam, 손실함수 : log loss, 원-핫인코딩, 평가지표 : accuracy
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics='accuracy')

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.h5',
                                                save_best_only=True)
# validation loss가 2번초과로 개선되지 않으면 종료
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
                                                  restore_best_weights=True)

history = model.fit(train_scaled, train_target, epochs=20,
                    validation_data=(val_scaled, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])
```

    Epoch 1/20
    1500/1500 [==============================] - 20s 5ms/step - loss: 0.5073 - accuracy: 0.8198 - val_loss: 0.3131 - val_accuracy: 0.8833
    Epoch 2/20
    1500/1500 [==============================] - 6s 4ms/step - loss: 0.3361 - accuracy: 0.8782 - val_loss: 0.2760 - val_accuracy: 0.8951
    Epoch 3/20
    1500/1500 [==============================] - 7s 5ms/step - loss: 0.2912 - accuracy: 0.8952 - val_loss: 0.2475 - val_accuracy: 0.9087
    Epoch 4/20
    1500/1500 [==============================] - 6s 4ms/step - loss: 0.2575 - accuracy: 0.9064 - val_loss: 0.2417 - val_accuracy: 0.9109
    Epoch 5/20
    1500/1500 [==============================] - 8s 5ms/step - loss: 0.2349 - accuracy: 0.9132 - val_loss: 0.2266 - val_accuracy: 0.9166
    Epoch 6/20
    1500/1500 [==============================] - 7s 5ms/step - loss: 0.2155 - accuracy: 0.9215 - val_loss: 0.2178 - val_accuracy: 0.9197
    Epoch 7/20
    1500/1500 [==============================] - 7s 5ms/step - loss: 0.1999 - accuracy: 0.9252 - val_loss: 0.2090 - val_accuracy: 0.9232
    Epoch 8/20
    1500/1500 [==============================] - 8s 5ms/step - loss: 0.1820 - accuracy: 0.9319 - val_loss: 0.2211 - val_accuracy: 0.9186
    Epoch 9/20
    1500/1500 [==============================] - 7s 4ms/step - loss: 0.1707 - accuracy: 0.9366 - val_loss: 0.2150 - val_accuracy: 0.9244



```python
import matplotlib.pyplot as plt
```


```python
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()
```


![](https://i.imgur.com/siCdnrP.png)



```python
model.evaluate(val_scaled, val_target)
```

    375/375 [==============================] - 1s 2ms/step - loss: 0.2090 - accuracy: 0.9232





    [0.20898833870887756, 0.9231666922569275]




```python
plt.imshow(val_scaled[0].reshape(28, 28), cmap='gray_r')
plt.show()
```

![](https://i.imgur.com/5RiMevd.png)



```python
preds = model.predict(val_scaled[0:1])
print(preds)
```

    1/1 [==============================] - 0s 118ms/step
    [[4.0748841e-15 2.2528982e-23 1.1966817e-18 3.3831836e-18 3.4746105e-17
      1.5839887e-14 1.3949707e-13 3.1241570e-14 1.0000000e+00 7.2195376e-16]]



```python
plt.bar(range(1, 11), preds[0])
plt.xlabel('class')
plt.ylabel('prob.')
plt.show()
```

![](https://i.imgur.com/2yabeoB.png)


```python
classes = ['티셔츠', '바지', '스웨터', '드레스', '코트',
           '샌달', '셔츠', '스니커즈', '가방', '앵클 부츠']
```


```python
import numpy as np
print(classes[np.argmax(preds)])
```

    가방



```python
test_scaled = test_input.reshape(-1, 28, 28, 1) / 255.0
```


```python
model.evaluate(test_scaled, test_target)
```

    313/313 [==============================] - 1s 3ms/step - loss: 0.2338 - accuracy: 0.9157





    [0.23381413519382477, 0.9157000184059143]

<br>


입력되는 입력값의 수보다 node의 수가 많은게 좋다.
``` python
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

(train_images, train_labels), (test_images, test_labels) = datasets.fashion_mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

# 모델 생성
model = models.Sequential()
model.add(layers.Conv2D(32, kernel_size=3, activation='relu', padding='same', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D(2))
model.add(layers.Conv2D(64, kernel_size=3, activation='relu', padding='same'))
model.add(layers.MaxPooling2D(2))

# Flatten한 다음에 
model.add(layers.Flatten())

# 3136개의 데이터보다 node의 수가 많은게 좋다 
model.add(layers.Dense(4096, activation='relu'))
model.add(layers.Dropout(0.4))
model.add(layers.Dense(10, activation='softmax'))

# 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')

# 체크 포인트
checkpoint_cb = keras.callbacks.ModelCheckpoint('개쩌는 모델.h5', save_best_only=True)

# 조기 종료
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)

# 모델 학습
history = model.fit(train_images, train_labels, epochs=20, validation_data=(test_images, test_labels), callbacks=[checkpoint_cb, early_stopping_cb])

# 모델 평가
print(model.evaluate(test_images, test_labels))

```
```