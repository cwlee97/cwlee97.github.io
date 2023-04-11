---
layout: single
title: UltraSonic Detection & Driving
categories: Autonomous_Driving_course
---

```py
#! /usr/bin/env python

import rospy, time
from std_msgs.msg import Int32MultiArray
from xycar_msgs.msg import xycar_motor

ultra_msg = None
motor_control = xycar_motor()

def callback(data):
    global ultra_msg
    ultra_msg = data.data


def motor(angle, speed):
    global pub
    global motor_control

    motor_control.angle = angle
    motor_control.speed = speed

    pub.publish(motor_control)
    
rospy.init_node('driver')
rospy.Subscriber('xycar_ultrasonic', Int32MultiArray, callback, queue_size = 1)
pub = rospy.Publisher('xycar_motor', xycar_motor, queue_size = 1)

while not rospy.is_shutdown():
    # right_back = ultra_msg[7]
    # back = ultra_msg[6]
    # left_back = ultra_msg[5]
    
    try:
        min_front = ultra_msg[6]
        min_left = ultra_msg[7]
        min_right = ultra_msg[5]

        distance = 30

        if min_front < 10:
            speed, angle = 0, 0
            motor(angle, speed)
            print("CLAER")
            break
        elif min_left >= distance and min_right >= distance:
            speed, angle = -3, 0
            motor(angle, speed)
            time.sleep(0.1)

        elif min_left < distance:
            speed, angle = -3, 50
            motor(angle, speed)
            time.sleep(0.1)

        elif min_right < distance:
            speed, angle = -3, -50
            motor(angle, speed)
            time.sleep(0.1)
        else:
            speed, angle = -3, 0
            motor(angle, speed)
            time.sleep(0.1)
    except: pass
```
