---
layout: single
title: Sorting Algorithm
categories: Jungle
---

# 정렬
항목들을 체계적으로 정리하는 과정, 순서를 정하거나 분류가 가능하다는 특징을 갖고, 효율적인 검색과 정렬한 순서에 따라 데이터 처리가 가능하게 된다.<br>
반대되는 과정은 셔플로 임의의 순서로 항목을 재정렬하는 과정이다.<br>

## 정렬의 종류
* 버블 정렬
* 선택 정렬
* 퀵 정렬
* 힙 정렬
* 삽입 정렬
* 병합 정렬
* 셸 정렬
* 기수 정렬
* 카운팅 정렬

## 버블 정렬
서로 인접한 두 원소를 검사하여 정렬하는 알고리즘 - 인접한 2개의 인덱스에 있는 요소를 비교하여 지정한 순서가 아닐 경우 서로 교환<br>

### 장점
* 구현이 쉽다

### 단점
* 하나의 요소가 끝에서 끝으로 정렬되기 위해서는 배열의 모든 요소들과 교환되어야 한다 - O(n)
* 자료의 교환 작업(swap)이 자료의 이동 작업(move)보다 더 복잡해서 버블정렬은 거의 쓰이지 않음

### Code
```python
def bubbleSort(array):
  length = len(array)
  for i in range(length-1, 0, -1):
    for j in range(i):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
  return array

if __name__=="__main__":
  array = [1, 7, 3, 8, 4, 2]
  print(bubbleSort(array))

####### output: [1, 2, 3, 4, 7, 8] ############
```

### 시간복잡도
* n-1, n-2, ... 1 -> n(n-1)/2 -> O(n^2)

## 선택 정렬
주어진 배열에서 최소값을 찾아 맨 앞에 위치한 값과 교체하는 알고리즘

### 장점
간단하게 위의 버블정렬과 비교했을 때 비교하는 횟수에 비해 교환이 적게 일어남

### 단점
정렬 시간이 오래 걸림

### Code
```python
def selectionSort(array):
  length = len(array)
  for i in range(length-1):
    min_element_index = i
    for j in range(i+1, length):
      if array[min_element_index] > array[j]:
        min_element_index = j
    array[i], array[min_element_index] = array[min_element_index], array[i]
  return array

if __name__=="__main__":
  array = [1, 7, 3, 8, 4, 2]
  print(selectionSort(array))

####### output: [1, 2, 3, 4, 7, 8] ############
```

## 퀵 정렬
‘찰스 앤터니 리처드 호어(Charles Antony Richard Hoare)’가 개발한 정렬 알고리즘으로, 불안정 정렬에 속하며 다른 원소와의 비교로 정렬을 수행하는 비교 정렬에 속한다.<br>
퀵 정렬은 분할 정복(divide and conquer) 방법을 통해 배열을 정렬한다.
1. 배열 가운데에서 하나의 원소를 고름 -> 피벗(pivot)
2. 피벗 엎에는 피벗보다 값이 작은 요소들이 오고, 피벗 뒤에는 피벗보다 값이 큰 요소들이 오도록 배열을 둘로 나눔(이를 분할이라고 하고, 해당 분할작업 후에 피벗은 움직이지 않음)
3. 분할된 배열에 대해 재귀적으로 1~2과정을 반복

-> 글로는 잘 이해되지 않아 나무위키에 예제 부분에 설명이 잘 되어있어 링크를 첨부한다([링크](https://ko.wikipedia.org/wiki/%ED%80%B5_%EC%A0%95%EB%A0%AC))

### 시간복잡도
1. 순환 호출의 깊이
    * 배열의 길이가 2^n형태라고 가정하면 2^3->2^2->2^1->2^0 순으로 줄어둘어 순환 호출의 깊이는 3이 됨
2. 각 순환 호출 단계의 비교 연산
    * 각 순환 호출에서는 배열의 모든 요소에 대해 비교를 수행하므로 평균 n번 수행됨
3. 시간복잡도
    * 순환 호출의 깊이 * 각 순환 호출 단계의 비교 연산 = nlog_2(n)

### Note
시간복잡도에서 평균적으로 좋은 성능을 보여주는 정렬 알고리즘이나, 최악의 경우 시간복잡도를 계산해보면 n개의 깊이와 n번의 연산을 수행하게 되어 O(n^2)의 복잡도를 갖게 된다.


### Code
```python
def quickSrot(array):
    if len(array) <= 1:
        return arary
    
    pivot = array[len(array) // 2]
    less = list()
    more = list()
    equal = list()

    for element in array:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            more.append(element)
        else:
            equal.append(element)
    return quickSort(less) + equal + quickSort(more)

####### output: [1, 2, 3, 4, 7, 8] ############
```

## 힙 정렬

해당 정렬도 글로 읽는 것보다 이루어지는 대략적인 영상을 보고 이해하는것이 빨랐다.[링크](https://commons.wikimedia.org/wiki/File:Heapsort-example.gif)<br>
또한 파이썬에서의 힙은 구현할 필요 없이 라이브러리에서 가져다 쓰면 되기에 코드는 생략한다.

## 삽입 정렬
두 번째 요소부터 그 앞의 요소들과 비교하여 삽입할 위치를 지정한 후 요소를 뒤로 옮기고 지정한 자리에 삽입하는 알고리즘

### 장점
* 안정적
* 배열이 이미 정렬되어 있는 경우 매우 효율적 - 기존 요소들을 뒤로 미루는 작업이 발생하지 않기 때문

### 단점
* 장점에 든 정렬된 배열의 경우는 극히 드문 경우이고 정렬되지 않은 배열의 경우 요소들의 이동이 빈번하게 일어나게 됨
* 배열의 길이가 길 경우 적합하지 않음

### 시간복잡도
1. 비교
    * 인덱스로 접근 후 값의 비교는 O(1)
    * 인덱스 접근 루프는 n-1번 발생(2번 요소부터 비교를 시작하기 때문) O(n)
2. 교환
    * 비교 후 해당 인덱스 이후의 요소들을 하나씩 뒤로보내는 작업 O(n)

    -> O(n^2)

### Code
```python
def insertSort(array):
  for element in range(1, len(array)):  # 2번 요소부터 탐색
    j = i-1
    key = array[i]
    while array[j] > key and j >= 0:
      array[j+1] = x[j]
      j = j - 1
    array[j+1] = key
  return array
if __name__=="__main__":
  array = [1, 7, 3, 8, 4, 2]
  print(selectionSort(array))

####### output: [1, 2, 3, 4, 7, 8] ############
```

## 병합 정렬
비교 기반 정렬 알고리즘으로 안정 정렬에 속하며 분할 정복 알고리즘중 하나.<br>

1. 정렬되지 않은 리스트를 각각 하나의 원소만 포함하는 n개의 부분리스트로 분할
2. 부분 리스트가 하나만 남을 때 까지 반복하여 병합 정렬된 부분 리스트 생성
3. 마지막으로 남은 부분 리스트가 정렬된 리스트

이해를 도와줄 그림 [링크](https://ko.wikipedia.org/wiki/%ED%95%A9%EB%B3%91_%EC%A0%95%EB%A0%AC#/media/%ED%8C%8C%EC%9D%BC:Merge-sort-example-300px.gif)

