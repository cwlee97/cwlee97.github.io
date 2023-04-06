---
layout: single
title: Lidar Sensor
categories: Autonomous_Driving_course
---

# 라이다 데이터 시각화
## 1. 패키지 생성 - rviz_lidar

```
xycar_ws-- src--rviz_lidar-- rviz
                          └- launch
                          └- src
```
<br>

```
$ catkin_create_pkg rviz_lidar rospy tf geometry_msgs urdf rviz xacro
```

## 2. launch 디렉토리 아레에 lidar_3d.launch 파일 만둘기(실제 라이다 구동 시)
```html
<!-- ~/xycar_ws/src/rviz_lidar/launch/lidar_3d.launch-->
<launch>
    <!-- rviz display-->
    <node name = "rviz_visualizer" pkg = "rviz" type = "rviz" required = "true" args = "-d $(find rviz_lidar)/rviz/lidar_3d.rviz"/>
    <node name = "xycar_lidar" pkg = "xycar_lidar" type = "xycar_lidar" output = "screen">
        <param name = "serial port" type = "string" value = "/dev/ttyRPL"/>
        <param name = "serial_baudrate" type = "int" value = "115200"/>
        <param name = "frame_id" type = "string" value = "laser"/>
        <param name = "inverted" type = "bool" value = "false"/>
        <param name = "angle_compensate" type = "bool" value = "true"/>
    </node>
</launch>
```

## 라이다 장치가 없는 경우
* 실제 라이다 장치를 대신하여 /scan 토픽을 발행하는 프로그램을 이용
* ROS에서 제공하는 "rosbag" 이용

## launch 디렉토리 아레에 lidar_3d.launch 파일 만둘기(rosbag 사용 시)

```html
<!-- ~/xycar_ws/src/rviz_lidar/launch/lidar_3d_rosbag.launch-->
<launch>
    <!-- rviz display-->
    <node name = "rviz_visualizer" pkg = "rviz" type = "rviz" required = "true" args = "-d $(find rviz_lidar)/rviz/lidar_3d.rviz"/>
    <node name = "rosbag_play" pkg = "rosbag" type = "play" output = "screen" required = "true" args = "$(find rviz_lidar)/src/lidar_topic.bag"/>
</launch>
```

## 3. RVIZ 실행
```
$ roslaunch rviz_lidar lidar_3d.launch
```

## 4. rviz 설정 변경 후 저장


# ROSBAG
* 토픽을 구독하여 파일로 저장하거나, 파일에서 토픽을 꺼내 발행하는 기능

## 사용법
```
<terminal>
$ rosbag record -O lidar_topic scan
$ rosbag play lidar_topic.bag
```

```html
<!-- launch file-->
<launch>
    <node name = "rosbag_play" pkg = "rosbag" type = "play" output = "screen" required = "true" args = "$(find_rviz_lidar)/src/lidar_topic.bag"/>
</launch>
```

# Range 메시지를 RVIZ에서 시각화 하는 방법
* 기존 rviz_lidar에서 작업

## 1. Range 토픽 데이터 구조 확인
![6.png](../../../images/Autonomous_Driving/Week3/6.png)
<br>

## 2. 파이썬 파일 작성
```py
# ~/xycar_ws/src/rviz_lidar/src/lidar_range.py
#! /usr/bin/env python

import serial, time, rospy
from sensor_msgs.msg import Range
from std_msgs.msg import Header

rospy.init_node('lidar_range')

pub1 = rospy.Publisher('scan1', Range, queue_size = 1)
pub2 = rospy.Publisher('scan2', Range, queue_size = 1)
pub3 = rospy.Publisher('scan3', Range, queue_size = 1)
pub4 = rospy.Publisher('scan4', Range, queue_size = 1)

'''
Range 채우기
헤더 정보 채우기
원뿔 모양의 Range 표시에 필요한 정보 채우기
'''
msg = Range()
h = Header()
h.frame_id = "sensorXY"
msg.header = h
msg.radiation_type = Range().ULTRASOUND
msg.min_range = 0.02
msg.max_range = 2.0
msg.field_of_view = (30.0/180.0)*3.14

while not rospy.is_shutdown():
    msg.header.stamp = rospy.Time.now()
    
    # 장애물 까지의 거리를 입력으로 넣고 토픽 발행
    msg.range = 0.4
    pub1.publish(msg)

    msg.range = 0.8
    pub2.publish(msg)

    msg.range = 1.2
    pub2.publish(msg)

    msg.range = 1.6
    pub2.publish(msg)

    time.sleep(0.2)
```

## 3. launch 파일 작성
```html
<!-- ~/xycar_ws/src/rviz_lidar/launch/lidar_range.launch-->
<launch>
    <!--rviz display-->
    <node name = "rviz_visualizer" pkg = "rviz" type = "rviz" required = "true" args = "-d $(find rviz_lidar)/rviz/lidar_range.rviz"/>
    <node name = "lidar_range" pkg = "rviz_lidar" type = "lidar_range.py"/>
</launch>
```

## 4. 토픽 전달 확인 및 Rviz 설정 저장

```
$ rostopic echo scan1
```

![7.png](../../../images/Autonomous_Driving/Week3/7.png)
<br>

![8.png](../../../images/Autonomous_Driving/Week3/8.png)
<br>

![9.png](../../../images/Autonomous_Driving/Week3/9.png)
<br>

# 과제: RVIZ에서 라이다 정보를 Range로 표시하기

## 1. 데이터 타입 확인

![10.png](../../../images/Autonomous_Driving/Week3/10.png)
<br>

## 2. 파이썬 파일 작성
* rosbag으로부터 토픽을 받아 range토픽을 발행하는 파일

```py
# ~/xycar_ws/src/rviz_lidar/src/lidar_urdf.py
#! /usr/bin/env python

import serial, time, rospy
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Range
from std_msgs.msg import Header

lidar_points = None

def lidar_callback(data):
    global lidar_points
    lidar_points = data.ranges

rospy.init_node('lidar')
rospy.Subscriber("/scan", LaserScan, lidar_callback, queue_size = 1)

pub1 = rospy.Publisher('scan1', Range, queue_size = 1)
pub2 = rospy.Publisher('scan2', Range, queue_size = 1)
pub3 = rospy.Publisher('scan3', Range, queue_size = 1)
pub4 = rospy.Publisher('scan4', Range, queue_size = 1)

msg = Range()
h = Header()

msg.radiation_type = Range.ULTRASOUND
msg.min_range = 0.02
msg.max_range = 2.0
msg.field_of_view = (30.0/180.0) * 3.14

while not rospy.is_shutdown():
    if lidar_points == None:
        continue
    # pub1
    h.frame_id = "front"
    msg.header = h
    msg.range=lidar_points[(360 / 4) * 1]
    pub1.publish(msg)

    # pub2
    h.frame_id = "right"
    msg.header = h
    msg.range=lidar_points[(360 / 4) * 2]
    pub2.publish(msg)

    # pub3
    h.frame_id = "back"
    msg.header = h
    msg.range=lidar_points[(360 / 4) * 3]
    pub3.publish(msg)

    # pub4
    h.frame_id = "left"
    msg.header = h
    msg.range=lidar_points[(360 / 4) * 0]
    pub4.publish(msg)

    time.sleep(0.5)
```

## 2. urdf파일 작성
* 경로: ~/xycar_ws/src/rviz_lidar/urdf/lidar_urdf.urdf

```html
<?xml version="1.0" ?>
<robot name="xycar" xmlns:xacro="http://www.ros.org/wiki/xacro">
  <link name="base_link"/>

  <!-- baselink => baseplate -->
  <link name="baseplate">
    <visual>
      <material name="red"/>
      <origin rpy="0 0 0" xyz="0 0 0"/>
      <geometry>
        <box size="0.2 0.2 0.07"/>
      </geometry>
    </visual>
  </link>

  <joint name="base_link_to_baseplate" type="fixed">
    <parent link="base_link"/>
    <child link="baseplate"/>
    <origin rpy="0 0 0" xyz="0 0 0"/>
  </joint>

  <!-- lidar data -->
  <!-- front -->
  <link name="front" />
  <joint name="baseplate_to_front" type="fixed">
    <parent link="baseplate"/>
    <child link="front"/>
    <origin rpy="0 0 0" xyz="0.25 0 0"/>
  </joint>

  <!-- back -->
  <link name="back" />
  <joint name="baseplate_to_back" type="fixed">
    <parent link="baseplate"/>
    <child link="back"/>
    <origin rpy="0 0 3.14" xyz="-0.25 0 0"/>
  </joint>

  <!-- left -->
  <link name="left" />
  <joint name="baseplate_to_left" type="fixed">
    <parent link="baseplate"/>
    <child link="left"/>
    <origin rpy="0 0 1.57" xyz="0 0.1 0"/>
  </joint>

  <!-- right -->
  <link name="right" />
  <joint name="baseplate_to_right" type="fixed">
    <parent link="baseplate"/>
    <child link="right"/>
    <origin rpy="0 0 -1.57" xyz="0 -0.1 0"/>
  </joint>


  <!-- 색상 정보 -->
  <material name="black">
      <color rgba="0.0 0.0 0.0 1.0"/>
  </material>
  <material name="blue">
      <color rgba="0.0 0.0 0.8 1.0"/>
  </material>
  <material name="green">
      <color rgba="0.0 0.8 0.0 1.0"/>
  </material>
  <material name="grey">
      <color rgba="0.2 0.2 0.2 1.0"/>
  </material>
  <material name="orange">
      <color rgba="1.0 0.423529411765 0.0392156862745 1.0"/>
  </material>
  <material name="brown">
      <color rgba="0.870588235294 0.811764705882 0.764705882353 1.0"/>
  </material>
  <material name="red">
      <color rgba="0.8 0.0 0.0 1.0"/>
  </material>
  <material name="white">
      <color rgba="1.0 1.0 1.0 1.0"/>
  </material>
  <material name="acrylic">
      <color rgba="1.0 1.0 1.0 0.4"/>
  </material>
</robot>
```
<br>

## 3. launch파일 작성
```html
<!-- ~/xycar_ws/src/rviz_lidar/launch/lidar_urdf.launch-->
<launch>
    <param name="robot_description" textfile="$(find rviz_lidar)/urdf/lidar_urdf.urdf"/>
    <param name="use_gui" value="true"/>
    <node name="rviz_visualizer" pkg="rviz" type="rviz" required="true" args="-d $(find rviz_lidar)/rviz/lidar_urdf.rviz"/>
    <node name="robot_state_publisher" pkg="robot_state_publisher" type="state_publisher"/>
    <node name"rosbag_play" pkg="rosbag" type="play" output="screen" required="true" args="$(find rviz_lidar)/src/lidar_topic.bag"/>
    <node name="lidar" pkg="rviz_lidar" type="lidar_urdf.py" output="screen"/>
</launch>
```

