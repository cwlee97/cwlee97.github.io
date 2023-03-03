---
layout: single
title: "Lidar Detection"
categories: TIL
---
```python
#!/usr/bin/env python
import cv2
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time
import numpy as np

# Function
def callback(msg):
    global msg_list
    msg_list = np.array(msg.ranges)

def go_forward():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
    twist.linear.x = 0.5; twist.linear.y = 0; twist.linear.z = 0

def turn_left():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 1
    twist.linear.x = 0.5; twist.linear.y = 0; twist.linear.z = 0

def turn_right():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -1
    twist.linear.x = 0.5; twist.linear.y = 0; twist.linear.z = 0

# Variables
width , height = 640, 480
capture = cv2.VideoCapture(0)
twist = Twist()
count = 0
vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 20)
scan_sub = rospy.Subscriber('/scan', LaserScan, callback)
msg_list = None

# Setting
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
rospy.init_node('vel_pub')


# main
while not rospy.is_shutdown():
    # read camera image & convert to binary image
    ret, src = capture.read()
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    pixel_avg = gray.sum() / (width * height)
    ret, dst = cv2.threshold(gray, pixel_avg-50, 255, cv2.THRESH_BINARY)

    pixel_list = dst[height//2]
    temp = []

    # lidar detection
    left_range = msg_list[:(msg_list.size * 1) // 6]
    right_range = msg_list[(msg_list.size * 5) // 6:]
    
    left_range = left_range[left_range != 0]
    right_range = right_range[right_range != 0]

    try:
        end_time = time.time() + 0.8
        print("left_range: ", min(left_range))
        print("right_range: ", min(right_range))
        if min(left_range) < 0.3:
            while time.time() < end_time:
                twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -0.8
                twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
                vel_pub.publish(twist) 
            while time.time() < end_time + 1.5:
                twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0.8
                twist.linear.x = 0.3; twist.linear.y = 0; twist.linear.z = 0
                vel_pub.publish(twist) 
            while time.time() < end_time + 1:
                twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -0.8
                twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
                vel_pub.publish(twist) 
            continue
        elif min(right_range) < 0.3:
            while time.time() < end_time:
                twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0.8
                twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
                vel_pub.publish(twist) 
            while time.time() < end_time + 1.5:
                twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -0.8
                twist.linear.x = 0.3; twist.linear.y = 0; twist.linear.z = 0
                vel_pub.publish(twist) 
            while time.time() < end_time + 0.8:
                twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0.8
                twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
                vel_pub.publish(twist)
            continue
    except:
        pass

    # read line & get middle value
    try:
        for i in range(640-1):
            if pixel_list[i] != pixel_list[i+1]:
                temp.append(i)
        middle = (temp[-1]+temp[-2]) // 2

    except:
        turn_right()
        vel_pub.publish(twist)
        continue

    # move robot by line middle value
    if middle < width//2 - 100:
        turn_right()

    elif (middle >= width//2 - 100) and (middle <= width//2 + 100):
        go_forward()

    elif middle > width//2 + 100:
        turn_left()
        
    # Publish topic
    vel_pub.publish(twist)
```
