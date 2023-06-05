---
layout: single
title: Autonomous Driving Perception Technology
categories: Autonomous_Driving_course
use_math: true
---

# 자율주행이란?
* 운전자의 개입(조작)없이 목적지까지 차량(Vehicle) 스스로 움직이는 기술이다.
* Autonomous Driving, Autonomous Vehicle, Self Driving Car등 다양한 용어로 불린다.

# 기술 요소
1. Perception: 자율주행 차량의 주행 환경에 대한 다양한 정보를 인지하는 기술
    * 다양한 센서(Vision, LiDAR, RADAR,...)를 사용하여 주행에 필요한 정보(장애물, 교통 신호, ...)를 인식
    * 인식된 다양한 정보로부터 자율주행 차량에 영향을 미칠 요소를 분석하고 측정하여 환경을 이해한다.
2. Localization: 자율주행 차량의 현재 위치를 추정하는 기술
    * GNSS 기반의 Global Position을 추정하는 방법 -> GPS/INS(&IMU) Fusion, GPS RTK, ...
    * 다른 센서 또는 데이터로부터 차량의 Global Posision을 추정하는 방법 -> SLAM, Map Matching
3. Planning: 자율주행 차량의 주행 환경, 위치 정보를 바탕으로 주행하는데 필요한 요소(경로, 판단,...)를 생성 & 결정하는 기술
    * 네비게이션과 같이, 현재 위치로부터 목적지까지 도로 단위의 경로를 설정한느 방법 -> Global Path Planning
    * 현재 주행 환경에서 원활한/안전한 주행을 위한 차선 단위의 경로를 설정하는 방법 -> Local Path Planning
4. Control: 자율주행 차량이 원활한 주행을 할 수 있도록 차량을 제어하는 기술
    * 자동차의 경우, 차량의(속도, 가속도, 순간 가속도)와 스팅어링을 제어한다.
    * 제어 대상의 Dynamics를 분석하고 주행 환경과의 상호작용을 통해 차량 안정성을 제어한다.

# HD Map - 정밀 지도
* HD(High Definition) Map으로 자율주행에 필요한 많은 사전 정보를 지도로 만들었다.
* HD Map을 만드는 화사마다 구체적인 정의, 데이터가 조금씩 다르며 계속 개발이 진행중이다.