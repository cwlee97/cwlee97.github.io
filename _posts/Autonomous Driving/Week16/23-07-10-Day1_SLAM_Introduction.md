---
layout: single
title: SLAM Introduction
categories: Autonomous_Driving_course
---

# SLAM
- Simultaneous - 동시적
- Localization - 위치추정
- And - 및
- Mapping - 지도 작성

SLAM 은 Mobile robotics에서부터 시작되었다. 

## Percaption & Control feedback loop
* Proprioceptive sensing의 안정성 확보가 어려움
* Exteroceptive sensing / Proprioceptive sensing의 신뢰도
* 노이즈 분석을 하는 동안 이동 불가
* 둘 중 하나의 sensing이 정확하다면 다른 sensing의 optimal한 값을 추정 가능

## Monte Carlo Localization
* Given a configuration space(i.e. map), use particle filter to estimate pose
* Low-quality map leads to localization failure
* Cannot run without a map
* Being a discrete multi-modal estimation, similar observations lead to confusion
* Initialization - motion update - measurement - weight update - resampling
* Monte Carlo Localization은 map에 전적으로 의존하기 때문에 map이 부정확하면 위치 추정이 불가능하다.

## Chicken and Egg problem
* Localization requires "High-quality map"
* Mapping requires "High-quality pose information"
* 해당 문제를 해결하기 위해 SLAM 등장 - 최적의 Map + 최적의 odometry 추정(Simultaneously)

## Localization, SLAM의 차이는 무엇인가?

# Sensor
SLAM에는 두 종류의 센서가 사용된다.
* Proprioceptive sensor 
* Exterocaptive sensor

## Proprioceptive sensor 
1. Wheel Encoder
    * 바퀴의 회전량(RPM)과 이동량을 측정하는 센서
    * 장점
        * 자동차에는 기본적으로 탑재
    * 단점
        * Odometry를 할시 drift에 약함
        * 바퀴가 헛도는 경우 잘못된 센서의 값이 생길 수 있음
        * 바퀴의 둘레가 주행 중 자주 바뀜
2. IMU - Inertial measurement unit
    * Linear accelerator(선형 가속도 측정) 센서와 Angular gyroscope(각속도 측정) 센서가 혼합된 센서
    * Spring-damper system의 원리를 이용
        * Optimal system - 차량용 IMU
        * MEMS - 스마트폰 및 소형 디바이스 IMU
    * 장점
        * Consumer grade 제품은 저렴한 편(자동차는 동일 성능에 저렴하지 않음)
        * 높은 sensitivity
        * 높은 FPS
    * 단점
        * 엄청 빠른 drift 누적
        * 보정을 위해 Camera / LiDAR / GNSS와 함께 사용

## Exterocaptive sensor
1. GNSS - Global navigation satellite system
    * 흔히 GPS라 칭함
    * 비콘 기반의 위치 추정 센서
        * 다수의 비콘에 대한 통신시간 차이를 이용하여 비콘-로봇의 거리를 구하곡 삼각 측량을 통해 localization 수행
        * Ego-motion을 추정하기 때문에 proprioceptive sensor같지만, 외부 비콘을 이용하기 때문에 exteroceptive sensor임
    * 나라마다 시스템이 다름
    * 장점
        * 저렴하고 사용이 쉬움
    * 단점
        * 부정확함(10~25m 오차)
        * RTK-GPS, DGPS를 사용할 경우 오차는 cm단위로 내려옴
        * 고층 빌딩 사이에서 multi-path 문제
        * 실내, 지하에서 사용 불가능
        * KPS가 아직 없음
2. LiDAR - Light detection and ranging sensors
    * 적외선 레이저를 쏘고 반사 시간을 측정하여 거리를 추정하는 센서
    * 주변 환경을 3D point cloud 형태로 바로 알 수 있음
    * 장점
        * Exteroceptive 센서 중 가장 정확한 편
        * 자율주행용 라이다는 ~100m 유효 거리
        * 빛의 파장이 일어나지 않기 때문에 낮/밤 사용 가능
    * 단점
        * 고가
        * 카메라에 비해 resolution이 낮음
        * 눈/비/안개 등 날씨에 영향을 받음
        * Multi-path problem
        * Solid-state LiDAR의 경우 여러 방향으로 탑재 필요
3. RADAR - Radio detection and ranging sensor
    * 반사되어 돌아오는 전파를 측정하여 radial 거리를 재는 센서
    * Deppler 효과를 이용하여 이동중인 물체의 속도 추정 가능
    * 전파의 종류를 바꿈으로써 near-range와 far-range 선택 가능
    * 장점
        * 날씨에 영향이 없음
        * 타 센서에서는 얻지 못하는 '속도'값 추정 가능
    * 단점
        * 작은 물체들은 detection 불가능
        * LiDAR보다 낮은 resolution
        * Multi-path 문제
4. Ultrasound
    * 초음파 이용 - RADAR와 방식 동일
5. Camera
    * 광센서를 이용해 빛 신호를 받고, debayering 프로세스를 통해 RGB 색 재구성
    * 장점
        * 저렴
        * 좋은 성능
        * 렌즈 교환을 통해 시야각 변경 가능
        * 사람이 보는 시야와 가장 유사
    * 단점
        * Depth 정보 소실
        * 조명 영향
6. Microphones
    * 공기의 진동을 transducer 센서를 통해 전기 신호로 변환하는 센서
    * 여러개의 마이크를 통해 소리의 근원에 대한 위치를 계산 가능
    * 장점
        * 유일하게 소리 정보를 사용하는 센서
        * 저렴한 가격
    * 단점
        * Geometry가 부정확함
        * 잡음이 심함

# SLAM 종류
* Visual-SLAM / VSLAM
* LiDAR SLAM
* RADAR SLAM

## Visual SLAM
Visual 정보를 이용하는 SLAM
* 장점
    * 저렴한 센서를 사용
    * 센서의 성능을 조절하기 쉬움
    * 센서 속도가 빠른 편
    * 이미지 기반 딥러닝 적용 가능 - Object Detection, Segmentation
    * 이미지로 사람이 이해하기 쉬운 시각화 가능
* 단점
    * 갑작스러운 빛 변화에 대응 불가능
    * 시야가 가려지거나 어두운 곳에서 사용 불가능
* 종류
    * Monocular Visual Slam
        * monocular camera - 1 camera
        * 1대의 카메라에서만 이미지를 받음
        * 장점
            * Stereo / Multi camera VSLAM보다 저렴함
        * 단점
            * Scale ambiguity - 3D 공간을 실제 스케일로 추정할 수 없음
    * Stereo camera - 2 camera / Multi camera - N cameras
        * 특징
            * Stereo Camera 사용
            * Multi-camera - N대의 카메라 사용
            * 인접한 카메라들간의 baseline 거리를 이용하여 삼각측량을 통해 거리/깊이 추정 가능
        * 장점
            * 두 이미지간의 disparity 정보를 이용해서 픽셀마다 depth를 추정할 수 있음
            * Metric scale의 3D 공간을 복원 가능
        * 단점
            * 카메라 설정 및 캘리브레이션이 어려움
            * 모든 픽셀마다 disparity 정보로 depth를 계산하는데에는 많은 계산량이 필요하며, 이를 위해 CPU나 FPGA 계산을 요구하기도 함
    * RGB-D Camera (Depth camera)
