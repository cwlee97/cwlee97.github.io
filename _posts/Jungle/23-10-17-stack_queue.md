---
layout: single
title: Stack & Queue
categories: Jungle
---

## 스택(Stack)
LIFO(후입 선출)의 특징을 가진 자료구조

### How to use stack in python?
1. list를 활용한 스택 구현
2. deque를 활용하여 스택처럼 사용

### Note
파이썬에서는 스택 라이브러리가 따로 존재하지 않는다. deque를 import하여 스택처럼 사용하는 경우가 많다.

## 큐(Queue)
FIFO(선입 선출)의 특징을 가진 자료구조

### How to use queue in python?
1. list를 활용한 큐 구현
2. stack과 같아 deque를 이용한 큐 사용
3. queue 모듈의 queue 클래스 사용

### Note
3번의 경우 주로 멀티 스레딩 환경에서 사용되고, 내부적으로 라킹(locking)을 지원하여 여러 개의 스레드가 동시에 데이터를 추가하거나 삭제가 가능

## 우선순위 큐(Priority Queue)
이름에 큐가 들어가 FIFO형식의 자료구조라고 생각할 수 있으나, 우선순위 큐는 우선순위가 높은 데이터가 먼저 나가는 형태의 자료구조<br>
일반적으로 힙을 통해 구현

### 힙(Heap)
우선순위 큐를 위해 고안ㄴ된 완전 이진트리 형태의 자료구조로, 여러개의 값 중 최대값 또는 최소값을 찾아내는 연산이 빠름

### 힙 특징
* 완전이진트리 형태로 이루어져 있음
* 부모노드와 서브트리간 대소 관계가 성립(반정렬 상태)
* 이진탐색트리(BST)와 달리 중복된 값이 허용
