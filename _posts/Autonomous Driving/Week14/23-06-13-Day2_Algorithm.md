---
layout: single
title: Algorithm - K-Means, DBSCAN, RANSAC
categories: Autonomous_Driving_course
use_math: true
---

# K-Means
Clustering 알고리즘 중 하나로, 주어진 데이터를 지정된 개수(K)개의 그룹으로 나누는 알고리즘이다.<br>

## 순서
1. 임의의 K개의 중심점(Centroids)을 선택한다.
2. 각 데이터를 가장 가까운 중심점에 속한 그룹으로 분류한다.
3. 그룹의 중심점을 새로 계산한다.
4. 2~3 단계를 새로운 중심점과 기존 중심점이 충분히 일치할 때 까지 반복한다.

## 장점
* 알고리즘의 구현 난이도가 쉽다.
* 다양한 데이터에 활용 가능하다.

## 단점
* 그룹의 개수를 사전에 정의해야 한다.
* 가중치 및 거리 정의가 필요하다.

## 개선 포인트
* 다양한 K값을 갖는 알고리즘을 병렬로 실행할 수 있을까?
* 다양한 결과에 대해 최적의 K값은 어떻게 찾을 수 있을까?
* For Each K-Means Result: $Optimized(K) = argmin(d(P_{max} - P_{min}))$

# DBSCAN
Clustering 알고리즘 중 하나로, 고차원 공간에서의 군집화 알고리즘이다.<br>
일정 거리 이내에 데이터가 최소 몇 개 이상이면 하나의 그룹으로 간주한다.<br>
DBSCAN에서는 중심점(Core Point)과 경계점(Border Point), 노이즈(Noise) 개념이 있다.

## 순서
1. Core/ Border/ Noise 분류
    1. 임의의 포인트를 하나 선정한다.
    2. 선택한 포인트로부터 반경 epsilon만큼 원을 만든다. == 각 Points와의 거리가 epsilon보다 작은지를 확인한다.
    3. 원 안에 다른  포인트의 개수를 확인한다.
        * 0: 노이즈로 분류
        * 1 ~ (min_point1): Border Point로 분류
        * \> min_point: Core Point로 분류
    4. 모든 포인트에 대해 분류를 반복한다.
2. Core Points 그룹화
    1. Core Points 중에서 하나의 Point를 선택하여 하나의 그룹으로 설정한다.(기본값, n_clusters = 0)
    2. 선택한 Point의 반경 epsilon 안에 포함되는 Core Points를 같은 그룹으로 그룹화 한다.
    3. 선택한 Point에 가장 이웃한 Core Point를 선택하고, 반경(epsilon)안에 다른 Core Points가 포함되지 않을 때 까지 반복한다.
    4. n_clusters를 하나 증가시키고, 방문하지 않은 Core Points 중에서 하나를 선택하고 2~3 단계를 반복한다.
3. Border Points 그룹화
    1. Border Points 중에서 하나의 Point를 선택하고, 가장 이웃한 그룹화된 Core Point의 그룹으로 설정한다.
    2. 남은 Border Points가 없을 때까지 반복한다.

## 장점
* 모든 데이터에 대해 그룹화를 진행하지 않으므로, 노이즈 대처가 가능하다.
* 그룹의 수를 미리 지정하지 않는다.

## 단점
* 듬성듬성(Sparse)한 데이터에 대해 잘 동작하지 않는다.
* 선택한 Point에 대해 다른 Points와의 거리를 계산하기 때문에 계산 복잡도가 높다.

## 개선 포인트
* 모든 노드를 순회하기 보다 Noise Point를 사전에 제외할 수 있을까?
* Border Points에 대해 Cluster Point를 찾기 보다 더 편한 비교 방법이 있을까?

# RANSAC
데이터셋에서 주어진 모델을 추정하는 알고리즘. 주어진 데이터셋에서 임의의 샘플들을 이용해 모델을 추정하고 이를 조정하는 방법을 사용<br>

## 순서
1. 샘플 데이터를 선택하고, 이를 이용해 모델을 추정한다.
2. 샘플 데이터 외에 나머지 데이터를 이용해 추정 모델과 일치하는(method) 데이터의 개수를 계산한다.
3. 일치하는 데이터의 개수가 일정한 임계치 이상이라면, 이를 최종 추정 모델로 사용한다.
4. 새로운 샘플을 선택하고, 일정 횟수만큼 반복한다.

## 장점
* 예외(Outlier)를 효과적으로 제거할 수 있다.
* 구현 난이도가 낮고, 다양한 모델에 대해 적용이 가능하다.

## 단점
* Sampling 결과에 따라 비효율적인 결과를 나타낼 수 있다.
* Prior Sampling을 사용하지 않기 때문에, 매 회 처음부터 다시 시작한다.

## 개선 포인트
* max_trials을 고정하지 않고, 조기에 종료할 수 있는 방법이 없을까?
* Sampling 결과를 제한할 수 있는 방법이 없을까?