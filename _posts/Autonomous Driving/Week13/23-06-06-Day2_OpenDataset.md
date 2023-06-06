---
layout: single
title: Open Dataset
categories: Autonomous_Driving_course
use_math: true
---

# 데이터 처리 순서
1. 데이터 가져오기
2. 데이터 탐색(EDA)
3. 데이터 가공(데이터 전처리)
4. 데이터 검증(training, test, validation dataset 분리)
5. 데이터 나누기

# KITTI Dataset
* 자율주행보다는 Visual SLAM에 더 최적화된 데이터셋
* 2D Object Detection 데이터셋
    * Left, Right 이밎
    * LiDAR data
    * Calibration 정보
    * 레이블링 데이터

# Pesudo Code(의사 코드)
알고리즘을 표현하는 방법 중 하나로, 일반적으로는 자연어를 이용해 만든 문장을 프로그래밍 언어와 유사한 형식으로 배치한 코드를 뜻한다.

## 의사코드
```
반복문 시작 (a를 2에서 9까지)
	반복문 시작 (b를 1에서 9까지)
		출력 : a * b  = 값 (개행)
	반복문 종료
반복문 종료
```

## 완성 코드
```py
# python
for i in range(2,10):
	for j in range(1,10):
		print(f'{i} X {j} = {i * j}')
```

```cpp
#include <iostream>

using namespace std;

int main(void)
{
    for(int A = 2; A < 10; A++)
    {
        for(int B = 1; B < 10; B++)
        {
            cout << A << " * " << B << " = " << A*B << endl;
        }
    }
    return 0;
}
```

Reference: https://namu.wiki/w/%EC%9D%98%EC%82%AC%EC%BD%94%EB%93%9C

# BDD100K
* 2017년에 공개하였으며, 자율주행을 위한 다양한 딥러닝 어플리케이션 데이터셋
* 홈페이지: https://www.bdd100k.com/
* 다양한 도시, 다양한 환경(날씨, 시간 등)에 대한 데이터로 보다 현실적인 상황을 담으려고 한다.
* 다운로드 홈페이지: https://bdd-data.berkeley.edu/index.html
* Object Detection, Segmentation, Lane Marking등 다양한 데이터가 존재한다.

# Cityscape
* 다양한 도시의 도로 Semantic Segmantation 데이터
* 홈페이지: https://www.cityscapes-dataset.com/

# Open Dataset Site
* [scale](https://scale.com/open-datasets)
* [Papers With Code](https://paperswithcode.com/)
    * 코드와 함께 공개한 논문들을 모아둔 사이트로, SOTA 모델을 활용해보기에 좋다.
