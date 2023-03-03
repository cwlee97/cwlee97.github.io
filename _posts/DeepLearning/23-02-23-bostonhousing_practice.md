---
layout: single
title: "Boston Housing Practice"
categories: TIL
---
```python
from keras.datasets import boston_housing

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()
```

    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/boston_housing.npz
    57344/57026 [==============================] - 0s 0us/step
    65536/57026 [==================================] - 0s 0us/step
    


```python
mean = train_data.mean(axis = 0)
std = train_data.std(axis = 0)

train_data -= mean
train_data /= std

test_data -= mean
test_data /= std
```


```python
from keras import models
from keras import layers

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation = 'relu', input_shape = (train_data.shape[1], )))
    model.add(layers.Dense(64, activation = 'relu'))
    model.add(layers.Dense(1)) # 선형층: 스칼라 회귀(하나의 연속적인 값을 예측)를 위한 구성
    model.compile(optimizer = 'rmsprop',
                  loss = 'mse', metrics = ['mae'])
    return model

# mse(mean squared error): 평균 제곱 오차
# mae(mean absolute error): 평균 절대 오차
```


```python
''' k-겹 검증을 사용한 훈련 '''
import numpy as np
k = 4
num_val_samples = len(train_data) // k
num_epochs = 100
all_scores = []

for i in range(k):
  print('처리 중인 폴드 #', i)
  val_data = train_data[i * num_val_samples : (i + 1) * num_val_samples]
  val_targets = train_targets[i*num_val_samples : (i + 1) * num_val_samples]
  partial_train_data = np.concatenate([train_data[: i * num_val_samples],
                                       train_data[(i + 1) * num_val_samples:]])
  partial_train_target = np.concatenate([train_targets[: i * num_val_samples],
                                         train_targets[(i + 1) * num_val_samples:]])
  model = build_model()
  model.fit(partial_train_data, partial_train_target,
            epochs = num_epochs, batch_size = 1, verbose = 0)
  val_mse, val_mae = model.evaluate(test_data, test_targets, verbose = 0)
  all_scores.append(val_mae)
```

    처리 중인 폴드 # 0
    처리 중인 폴드 # 1
    처리 중인 폴드 # 2
    처리 중인 폴드 # 3
    


```python
results = model.evaluate(test_data, test_targets)
print(results)
```

    4/4 [==============================] - 0s 3ms/step - loss: 19.2833 - mae: 2.9951
    [19.283279418945312, 2.9951038360595703]
    


```python

```
