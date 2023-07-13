---
layout: single
title: Feature detector
categories: Autonomous_Driving_course
use_math: true
---

# Pre - 1980
1. Sobel-Operator
    * line detect을 위한 gradient operator를 기반으로 만들어짐
    * Strong edge를 찾기위한 적당한 threshold값을 찾기 어려움
2. Hough-transform
    * Sobel-operator로 뽑아낸 edge들을 parameter-space에 표현
    * Hough transform을 기점으로 robust하게 line을 찾을 수 있어짐
    * GPU가 없는 상황에서 최근까지도 자주 사용됨
3. Canny Edge Detection
    * Sobel-operator의 결과로 strong-edge를 찾는 방법

# Feature Detector
1. Keypoint detector
    * searches for 'interesting points'
    * ex) x: 100, y: 200
2. Descriptor extractor
    * Describing the patch around the keypoint
    * 특징 기술자라고도 칭함
    * Keypoint 근처의 pixel들을 분석해 descriptor 객체로 만듬
    * ex) Keypoint 근처 10*10 pixel들의 밝기값을 histogram으로 표현 <-descriptor
3. Correspondence matcher
    * 두 개의 point feature가 실제로 같은 객체를 의미하는지에 대한 matching 정보
    * 두point feature의 descriptor들을 비교
4. Local feature
    * Local scale로 이미지를 표현할 수 있는 방법

# Corner Detection Method
1. Moravec(1980)
    * First 'robust' corner detector
    * Analyze gradient changes in {0, 0}, {1, 0}, {1, 1}, {0, 1}, {-1, 1} direction and if above threshold, identify corner
    * corner detection -> Match between 2images -> calculate relative rotation / translation
2. Harris Corner
    * Moravec detector를 개선
    * x, y 방향의 gradient를 계산 -> 코너의 방향성을 분석할 수 있는 Matrix 생성
    * Eigenvalue 추출, Moravec보다 robust
    * Mathmatical evaluation of flat/edge/corner - 'corner-ness' score
3. SIFT
    * DL 출시 이전 가장 정확한 corner detector
    * scale invariant, rotation invariant
    * 추출한 keypoint 주변 16 * 16의 gradient를 계산 -> descriptor extract
4. Fast
    * 17 * speed of Harris
    * 42 * Speed of SIFT
    * Robust in fast motion + orientation changek
5. BRIEF
    * Binary descriptor
    * Memory efficient, compared to floating-point descriptor
6. FLANN
    * C++ Library for fast multi-dimensional vector match
7. ORB
    * oriented FAST(scale invariant) + rotated BRIEF(rotation invariant)
    * Aim to be 'SIFT in real-time'
8. AKAZE
    * More robust than SIFT and ORB
    * speed - between ORB~SIFT