---
layout: single
title: Lidar Detection & Driving
categories: Autonomous_Driving_course
---

```py
import rospy
from sensor_msgs.msg import LaserScan
from xycar_motor.msg import xycar_motor
import time
import numpy as np
 
msg_list = None

def callback(msg):
    global msg_list
    msg_list = np.array(msg.ranges)

def motor(angle, speed):
    global pub
    global motor_control

    motor_control.angle = angle
    motor_control.speed = speed

    pub.publish(motor_control)

motor_control = xycar_motor()
rospy.init_node("driver")
rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('xycar_motor', xycar_motor, queue_size = 1)

while not rospy.is_shutdown():
    # lidar detection
    left_range = msg_list[(msg_list.size * 1) // 6 : (msg_list.size * 2) // 6]
    front_range = np.append(msg_list[:(msg_list.size * 1)], msg_list[(msg_list.size * 5) // 6:])
    right_range = msg_list[(msg_list.size * 4) // 6 : (msg_list.size * 5) // 6]
    
    left_range = left_range[left_range != 0]
    right_range = right_range[right_range != 0]
    front_range = front_range[front_range != 0]
    try:
        min_front = min(front_range)
        min_left = min(left_range)
        min_right = min(right_range)

        distance = 0.25

        if min_front < 0.15:
            speed, angle = 0, 0
            motor(angle, speed)
            print("CLAER")
            break
        elif min_left >= distance and min_right >= distance:
            speed, angle = 3, 0
            motor(angle, speed)
            time.sleep(0.1)

        elif min_left < distance:
            speed, angle = 3, 50
            motor(angle, speed)
            time.sleep(0.1)

        elif min_right < distance:
            speed, angle = 3, -50
            motor(angle, speed)
            time.sleep(0.1)
        else:
            speed, angle = 3, 0
            motor(angle, speed)
            time.sleep(0.1)
    except: pass
```