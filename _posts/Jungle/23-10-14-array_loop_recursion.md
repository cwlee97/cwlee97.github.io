---
layout: single
title: Array&List&Recursion
categories: Jungle
---
# 알고리즘

알고리즘이란 어떤 목적을 달성하거나 결과물을 만들어내기 위해 거쳐하나는 일련의 과정들<br>
결과물까지의 루트는 다양할 수 있음<br>

알고리즘의 실행시간은 컴퓨터가 알고리즘 코드를 실행하는 속도에 의존<br>

알고리즘의 실행시간은 두 부분으로 나뉨<br>
1. 입력값의 크기에 따라 알고리즘의 실행시간을 검증
2. 입력값의 크기에 따른 함수의 증가량(성장률이라고 칭함)

<br>
이때 중요하지 않은 상수와 계수를 제거 하면 알고리즘의 실행시간에서 중요한 성장률에 집중 가능 -> 점근적 표기법<br>

3가지 점근적 표기법<br>
* 최상의 경우: 오메가 표기법
* 평균의 경우: 세타 표기법
* 최악의 경우: 빅오 표기법

<br>

## 빅오 표기법(Big-O)
* 불필요한 연산을 제거하여 알고리즘 분석을 쉽게 할 목적으로 사용
* 시간복잡도, 공간복잡도가 측정됨
    * 시간복잡도: 입력된 N의 크기에 따라 실행되는 조작의 수
    * 공간복잡도: 알고리즘이 실행될 때 사용하는 메모리의 양

### 시간복잡도
시간 복잡도의 가장 간단한 정의는 알고리즘의 성능을 설명하는 것
알고리즘을 수행하기 위해 프로세스가 수행해야 하는 연산을 수치화 한 것

실행시간X, 연산 수치로 판별 -> 실행시간은 하드웨어, 프로그래밍 언어에 따라 편차가 크기 때문

시간복잡도에서 중요하게 보는 것은 가장 큰 영향을 미치는 n의 단위

```
1           O(1)    -> 상수
2n+20       O(n)    -> n이 가장 큰 영향
3n^2        O(n^2)  -> n^2이 가장 큰 영향
```

### O(1)

입력에 관계 없이 복잡도가 동일

```python
def hello_world():
        print("hello, world!")
```

### O(logn), O(nlogn)

입력의 크기에 따라 처리 시간이 증가하는 정렬 알고리즘에서 많이 사용

### O(n)

입력과 처리 시간이 선형적일 때 사용 ex)for

```python
def func(arr):
    for ele in arr:
        print(ele)
```

### O(n^2)

이중 for문과 같은 케이스
```python
def func(arr1, arr2):
    for ele1 in arr1:
        for ele2 in arr2:
            print(ele1, ele2)
```

### 시간복잡도 계산 요령
* 하나의 루프를 사용하여 단일 요소 집합을 반복: O(n)
* 컬렉션의 절반 이상을 반복: O(n/2) -> O(n)
* 두 개의 다른 루프를 사용하여 두 개의 개별 컬렉션 반복: O(n+m) -> O(n)
* 이중 루프를 사용하여 단일 컬렉션을 반복하는 경우: O(n^2)
* 컬렉션 정렬을 사용하는 경우: O(n*log(n))

<br>

# 자료구조

여러개의 원소를 저장할 때 선택할 수 있는 두 가지는 배열, 리스트이다.

## 배열
* Static Array의 경우 크기가 고정되어 있어 크기 이상의 데이터를 저장할 수 없음
* 같은 타입의 변수들로 이루어진 집합
* 각각의 요소들을 배열 요소(element)라고 하며, 배열에서의 위치를 가리키는 수는 인덱스(index)라고 함
* 배열의 인덱스: 0 ~ size-1
* 배열 A의 n번 째에 해당하는 변수는 A[n]으로 표시
* 접근(access), 검색(search), 추가(add), 제거(remove) 연산이 가능

### 접근
* 배열 내 n번째 인덱스의 값을 찾아내는 연산
* 배열의 첫 번째 변수에는 시작 주소값이 저장되어 n번째 요소를 찾기 위해 주소값에서 단순 사칙연산이 수행되기 때문에 접근의 시간복잡도는 O(1)

### 검색
* 배열의 요소들을 순차적으로 돌며 원하는 값을 찾음
* 검색 시기에 따라 시간복잡도가 변화하나 최대 O(n)의 시간 복잡도를 갖는다(for문을 size만큼 돌렸다고 생각하자)

### 추가, 삭제
* 추가, 삭제의 경우 접근, 검색의 방법에 따라 시간복잡도가 다름
* 해당 인덱스를 찾아서 추가, 삭제가 진행된다면 검색과 같이 O(n)의 시간복잡도
* 배열의 처음, 중간에 추가, 삭제를 하게되면 해당 인덱스 이후의 데이터를 밀거나 당겨야 해서 O(n)의 시간복잡도
* 반대로 배열의 끝에 삽입, 삭제는 O(1)의 시간복잡도
* 인덱스를 활용한 데이터에 대한 접근이 장점인 자료구조라서 삭제 된 상태를 빈 공간으로 남겨야함 - 메모리 낭비

### Note
* 인덱스로만 접근하여 배열을 사용하게 된다면 O(1)의 시간복잡도로 매우 빠른 자료구조
* 여러 설명하는 글을 참고하였는데 중간 원소 삭제 후 뒤 원소들을 당겨온다는 설명과 인덱스로 데이터의 접근이 장점인 자료구조로서 삭제 후 해당 공간을 비워둔다는 설명이 있는데 해당 부분은 조금 더 조사해볼 예정
* 위에는 서술하지 않았지만 Static, Dynamic Array의 경우 시간복잡도에서 차이가 발생한다

<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
<tbody>
<tr>
<td style="width: 20%; text-align: justify;">&nbsp;</td>
<td style="width: 20%; text-align: justify;">인덱스가 i인 소 접근</td>
<td style="width: 20%; text-align: justify;">마지막에 값 삽입,삭제</td>
<td style="width: 20%; text-align: justify;">i번째에 값 삽입, 삭제</td>
<td style="width: 20%; text-align: justify;">처음에 값 삽입, 삭제</td>
</tr>
<tr>
<td style="width: 20%; text-align: justify;">Static Array</td>
<td style="width: 20%; text-align: justify;">O(1)</td>
<td style="width: 20%; text-align: justify;">O(n)</td>
<td style="width: 20%; text-align: justify;">O(n)</td>
<td style="width: 20%; text-align: justify;">O(n)</td>
</tr>
<tr>
<td style="width: 20%; text-align: justify;">Dynamic Array</td>
<td style="width: 20%; text-align: justify;">O(1)</td>
<td style="width: 20%; text-align: justify;">O(1)</td>
<td style="width: 20%; text-align: justify;">O(n)</td>
<td style="width: 20%; text-align: justify;">O(n)</td>
</tr>
<tr>
<td style="width: 20%; text-align: justify;">Linked List</td>
<td style="width: 20%; text-align: justify;">O(n)</td>
<td style="width: 20%; text-align: justify;">O(1)</td>
<td style="width: 20%; text-align: justify;">O(1)</td>
<td style="width: 20%; text-align: justify;">O(1)</td>
</tr>
</tbody>
</table>

## 문자열
* 내부에 문자(char)로 된 버퍼(arr, list)를 갖고있고, 이를 조작하는 메소드를 제공
* 대부분의 라이브러리 함수들이 문자열을 다루는 경우 끝에 null char가 저장되어 있다는 가정 하에 동작(문자열의 끝을 알기 위함)

## 반복
* 명령을 반복적으로 실행하는 것이 목표
* for, while등 과 같은 함수를 사용
* 초기식, 조건식, 변화식이 있음
* 무한 루프에 유의
* 무한 루프는 CPU 사이클을 반복적으로 사용
```python
for i in range(min, max + 1, step)
# min: 초기식
# max: 조건식
# step: 변화식
# while에도 동일한 식들이 있음
```

## 재귀
* 반복과 목적은 동일
* 자기자신을 내부에서 호출
* 모든 재귀함수는 반복문만으로 동일한 동작이 가능
* 함수가 끝나지 않은 채 연속적으로 함수를 호출하므로 스택에 메모리가 쌓이게 됨
* stack 메모리 공간을 사용하여 해당 메모리에 제한이 있다면 stack overflow가 발생
* 반복과 비교하여 메모리, 시간에서는 손해지만, 적은 변수와 가독성이 좋은 장점이 있음
```python
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

### 꼬리 재귀
```python
# 일반 재귀
def sum(x) {
  if x == 100: return x
  else return x + sum(x + 1)
}

sum(0)

# 꼬리 재귀
def tailSum(x, answer) {
  if x > 100: return answer
  else return tailSum(x + 1, answer + x)
}

tailSum(0, 0)
```
* 일반 재귀의 단점인 스택오버플로우를 보완
* 일반 재귀와의 차이는 일반 재귀는 return 이전에 연산을 수행하고, 꼬리재귀는 return 이후에 연산을 수행
* 꼬리 재귀가 호출되는 시점에 컴파일러는 꼬리 재귀를 최적화하고, 이 때 꼬리 재귀는 반복문으로 변경
* 컴파일러가 이런 최적화 기능을 지원하는지 먼저 확인

### 재귀 함수의 조건
* 특정 입력에 대해서는 자기 자신을 호출하지 않고 종료되어야 함(base case)
* 모든 입력은 위의 base case으로 수렴해야 함

### Note
* 일반 재귀와 꼬리 재귀의 차이가 아직도 명확하지 않아 다시 정리해본다
    * 일반재귀
        * 호출 당한 함수가 호출한 함수에게 자신의 결과값을 알려주고 그 값을 전달받은 함수는 원래 자신이 갖고있던 값과 연산을 수행하여 전달
    * 꼬리재귀
        * 함수 자체에서는 일을 하지 않고 결과값만을 전달