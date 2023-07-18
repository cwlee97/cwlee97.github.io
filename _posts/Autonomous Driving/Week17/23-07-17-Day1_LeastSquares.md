---
layout: single
title: Least Squares
categories: Autonomous_Driving_course
use_math: true
---

* A method to get solution of an over-determined system
    * All SLAM problems are over-determined system

* Over-determined system = There are more equations than unknown
    * i.e. More sensor measurements than the number of states

* What is the state 'x' which minimizes the sum of Z-Z^?
    * What is the robot pose and landmark location, which minimizes the difference between our measurements and given the sensor readings

## Maximum-a-posteriori(MAP) estimation in SLAM
![png](../../../images/Autonomous_Driving/Week17/1.png)
<br>

![png](../../../images/Autonomous_Driving/Week17/2.png)
<br>

