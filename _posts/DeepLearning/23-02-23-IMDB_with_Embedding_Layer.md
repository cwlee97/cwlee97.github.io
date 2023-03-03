---
layout: single
title: "IMDB With Embedding Layer"
categories: TIL
---
```python
# 단어 수준의 원-핫 인코딩하기
import numpy as np
samples = ['The cat sat on the mat.', 'The dog ate my homework.']

token_index = {} # 데이터에 있는 모든 토큰의 인덱스를 구축합니다.
for sample in samples:
  for word in sample.split(): # split() 메서드를 사용하여 샘플을 토큰으로 나눕니다. 실전에서는 구두점과 특수 문자도 사용합니다.
    if word not in token_index:
      token_index[word] = len(token_index) + 1

max_length = 10 # 샘플을 벡터로 변환합니다. 각 샘플에서 max_length까지 단어만 사용합니다.

results = np.zeros(shape=(len(samples),
                   max_length,
                   max(token_index.values()) + 1))
for i, sample in enumerate(samples):
  for j, word in list(enumerate(sample.split()))[:max_length]:
    index = token_index.get(word)
    results[i, j, index] = 1.
```


```python
import string
samples = ['The cat sat on the mat.', 'The dog ate my homework.']
characters = string.printable # 출력 가능한 모든 아스키 문자
token_index = dict(zip(characters, range(1, len(characters) + 1)))

max_length = 50
results = np.zeros((len(samples), max_length, max(token_index.values()) + 1))
for i, sample in enumerate(samples):
  for j, character in enumerate(sample):
    index = token_index.get(character)
    results[i, j, index] = 1.
print(results)
```

    [[[0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      ...
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]]
    
     [[0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      ...
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]]]
    


```python
# 케라스를 사용한 단어 수준의 원-핫 인코딩하기
from keras.preprocessing.text import Tokenizer
samples = ['The cat sat on the mat.', 'The dog ate my homework.']
tokenizer = Tokenizer(num_words = 1000) # num_words=1000: 가장 빈도수가 높은 단어만 선택하여 tokenizer객체에 저장
tokenizer.fit_on_texts(samples) # 단어 인덱스를 구축합니다.

sequences = tokenizer.texts_to_sequences(samples)

one_hot_results = tokenizer.texts_to_matrix(samples, mode = 'binary')

word_index = tokenizer.word_index
print('%s 개의 고유한 토큰을 찾았습니다.' % len(word_index))
```

    9 개의 고유한 토큰을 찾았습니다.
    


```python
print(tokenizer.word_index)
```

    {'the': 1, 'cat': 2, 'sat': 3, 'on': 4, 'mat': 5, 'dog': 6, 'ate': 7, 'my': 8, 'homework': 9}
    


```python
# 해싱 기법을 사용한 단어 수준의 원-핫 인코딩하기
samples = ['The cat sat on the mat.', 'The dog ate my homework.']

dimensionality = 1000 # 단어를 크기가 1000인 벡터로 저장합니다. 1000개의 단어가 있다면 해싱 충돌이 늘어나고, 인코딩의 정확도가 감소합니다.
max_length = 10

results = np.zeros((len(samples), max_length, dimensionality))
for i, sample in enumerate(samples):
  for j, word in list(enumerate(sample.split()))[:max_length]:
    index = abs(hash(word)) % dimensionality
    results[i, j, index] = 1.
```


```python
print(results)
```

    [[[0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      ...
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]]
    
     [[0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      ...
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]
      [0. 0. 0. ... 0. 0. 0.]]]
    


```python
''' Embeddong 층의 객체 생성하기 '''
from keras.layers import Embedding

embedding_layer = Embedding(1000, 64)
# Embedding 층은 적어도 2개의 매개변수를 받습니다.
# 가능한 토큰의 개수(여기서는 10000으로 단어 인덱스 최대값 + 1입니다.)와 임베딩 차원(여기서는 64) 입니다.
```


```python
# Embedding 층에 사용할 IMDB 데이터 로드하기
from keras.datasets import imdb
from keras import preprocessing

max_features = 10000
maxlen = 10

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words = max_features)

# 리스트를 (samples, maxlen) 크기의 2D 정수 텐서로 변환합니다.
x_train = preprocessing.sequence.pad_sequences(x_train, maxlen = maxlen)
x_test = preprocessing.sequence.pad_sequences(x_test, maxlen = maxlen)
```


```python
# IMDB 데이터에 Embedding 층과 분류기 사용하기
from keras.models import Sequential
from keras.layers import Flatten, Dense, Embedding

model = Sequential()
model.add(Embedding(10000, 8, input_length = maxlen))

model.add(Flatten())

model.add(Dense(1, activation = 'sigmoid'))
model.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy', metrics = ['acc'])
model.summary()

history = model.fit(x_train, y_train,
                    epochs = 10,
                    batch_size = 32,
                    validation_split = 0.2)
```

    Model: "sequential_1"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    embedding_2 (Embedding)      (None, 10, 8)             80000     
    _________________________________________________________________
    flatten_1 (Flatten)          (None, 80)                0         
    _________________________________________________________________
    dense_1 (Dense)              (None, 1)                 81        
    =================================================================
    Total params: 80,081
    Trainable params: 80,081
    Non-trainable params: 0
    _________________________________________________________________
    Epoch 1/10
    625/625 [==============================] - 2s 2ms/step - loss: 0.6766 - acc: 0.5975 - val_loss: 0.6453 - val_acc: 0.6602
    Epoch 2/10
    625/625 [==============================] - 1s 2ms/step - loss: 0.5897 - acc: 0.7132 - val_loss: 0.5724 - val_acc: 0.6974
    Epoch 3/10
    625/625 [==============================] - 1s 2ms/step - loss: 0.5193 - acc: 0.7488 - val_loss: 0.5454 - val_acc: 0.7126
    Epoch 4/10
    625/625 [==============================] - 1s 2ms/step - loss: 0.4820 - acc: 0.7696 - val_loss: 0.5389 - val_acc: 0.7160
    Epoch 5/10
    625/625 [==============================] - 1s 2ms/step - loss: 0.4579 - acc: 0.7857 - val_loss: 0.5379 - val_acc: 0.7212
    Epoch 6/10
    625/625 [==============================] - 1s 2ms/step - loss: 0.4381 - acc: 0.8007 - val_loss: 0.5421 - val_acc: 0.7188
    Epoch 7/10
    625/625 [==============================] - 1s 2ms/step - loss: 0.4212 - acc: 0.8107 - val_loss: 0.5479 - val_acc: 0.7192
    Epoch 8/10
    625/625 [==============================] - 1s 2ms/step - loss: 0.4054 - acc: 0.8196 - val_loss: 0.5516 - val_acc: 0.7202
    Epoch 9/10
    625/625 [==============================] - 1s 2ms/step - loss: 0.3914 - acc: 0.8288 - val_loss: 0.5588 - val_acc: 0.7192
    Epoch 10/10
    625/625 [==============================] - 1s 2ms/step - loss: 0.3777 - acc: 0.8358 - val_loss: 0.5654 - val_acc: 0.7170
    


```python
model.evaluate(x_test, y_test)
```

    782/782 [==============================] - 1s 969us/step - loss: 0.5733 - acc: 0.7149
    




    [0.5732532143592834, 0.7148799896240234]




```python

```
