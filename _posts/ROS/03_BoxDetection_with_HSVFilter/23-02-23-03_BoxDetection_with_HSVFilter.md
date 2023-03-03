---
layout: single
title: "Box Detection with HSV Filter"
categories: TIL
---
# MotorSet
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup (36, GPIO.OUT)

EN1 = 11
IN1 = 13
IN2 = 15
EN2 = 29
IN3 = 31
IN4 = 37

GPIO.setup (EN1, GPIO.OUT)
GPIO.setup (IN1, GPIO.OUT)
GPIO.setup (IN2, GPIO.OUT)
GPIO.setup (EN2, GPIO.OUT)
GPIO.setup (IN3, GPIO.OUT)
GPIO.setup (IN4, GPIO.OUT)

p = GPIO.PWM (36,50) # gripper
#servo
p.start(12)
GPIO.output(EN1, False)
GPIO.output(EN2, False)

'''p.ChangeDutyCycle(12)#open
time.sleep(5)
p.ChangeDutyCycle(4.4)
time.sleep(5)
p.ChangeDutyCycle(12)#open
time.sleep(5)

'''
GPIO.output(EN2, False)
GPIO.output(EN1, True)
GPIO.output(IN1, False)
GPIO.output(IN2, True)
time.sleep(5)
GPIO.output(EN1, False)
GPIO.output(EN2, False)
time.sleep(10)
'''
try:
   #motor
    while True:
        print("on going")
        GPIO.output(EN1, False)
        GPIO.output(EN2, False)
        p.ChangeDutyCycle(4.4)
        time.sleep(2)
        
        GPIO.output(EN2, True)
        GPIO.output(IN4, False)
        GPIO.output(IN3, True)
        time.sleep(5)
        p.ChangeDutyCycle(12)
        GPIO.output(EN2, False)
        time.sleep(2)
        GPIO.output(EN2, False)
        GPIO.output(EN1, True)
        GPIO.output(IN2, False)
        GPIO.output(IN1, True)
        time.sleep(5)
        
        GPIO.output(EN1, False)
        GPIO.output(EN2, False)
        time.sleep(10)

except:
    pass
finally:
    GPIO.cleanup()'''
```

# Variables
```python
import numpy as np
import rospy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
import time
import cv2



GPIO.setmode(GPIO.BOARD)

GPIO.setup (36, GPIO.OUT)
GPIO.setup (37, GPIO.OUT)
GPIO.setup (38, GPIO.OUT)

trig = 33
echo = 35

GPIO.setup (trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

EN1 = 11
IN1 = 13
IN2 = 15

GPIO.setup (EN1, GPIO.OUT)
GPIO.setup (IN1, GPIO.OUT)
GPIO.setup (IN2, GPIO.OUT)

p = GPIO.PWM (36,50) # gripper
p1 = GPIO.PWM (37,50) # R
p2 = GPIO.PWM (38,50) # L

mode = None

twist = Twist()
vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 20)

CAMERA_DEVICE_ID = 0
IMAGE_WIDTH = 320
IMAGE_HEIGHT = 240

# create video capture
cap = cv2.VideoCapture(CAMERA_DEVICE_ID)

# set resolution to 320x240 to reduce latency 
cap.set(3, IMAGE_WIDTH)
cap.set(4, IMAGE_HEIGHT)
rospy.init_node('vel_pub')

# Read the frames frome a camera
_, frame = cap.read()
frame = frame[(IMAGE_HEIGHT*1)//3:]
frame = cv2.blur(frame,(3,3))

# Convert the image to hsv space and find range of colors
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

hsv_Red_m = np.array((120, 150, 108))
hsv_Red_M = np.array((178, 255, 255))
hsv_Blue_m = np.array((93, 91, 33))
hsv_Blue_M = np.array((120, 255, 255))
hsv_White_m = np.array((18, 1, 180))
hsv_White_M = np.array((90, 7, 210))
hsv_Black_m = np.array((101,17,51))
hsv_Black_M = np.array((120,255,255))
hsv_Yellow_m = np.array((30,3,148))
hsv_Yellow_M = np.array((67,9,160))

#hsv_White_m = np.array((120, 51, 10))
#hsv_White_M = np.array((120, 51, 10))

thresh_Red = cv2.inRange(hsv, hsv_Red_m, hsv_Red_M)
thresh_Blue = cv2.inRange(hsv, hsv_Blue_m, hsv_Blue_M)
thresh_White = cv2.inRange(hsv, hsv_White_m, hsv_White_M)
thresh_Black = cv2.inRange(hsv, hsv_Black_m, hsv_Black_M)
thresh_Yellow = cv2.inRange(hsv, hsv_Yellow_m, hsv_Yellow_M)

# findContours() has different form for opencv2 and opencv3
contours_Red, hierarchy = cv2.findContours(thresh_Red, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours_Blue, hierarchy = cv2.findContours(thresh_Blue, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours_White, hierarchy = cv2.findContours(thresh_White, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours_Black, hierarchy = cv2.findContours(thresh_Black, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours_Yellow, hierarchy = cv2.findContours(thresh_Yellow, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
```

# Function
```python
import numpy
import rospy
from geometry_msgs.msg import Twist
import cv2
import numpy as np
from BoxDetectionwithHSV_variables import *
import RPi.GPIO as GPIO

def forward():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
    twist.linear.x = 0.3; twist.linear.y = 0; twist.linear.z = 0
def left():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0.5
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
def right():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -0.5
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
def stop():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
    
def hsv2rgb(h, s, v):
    h = float(h) * 2
    s = float(s) / 255
    v = float(v) / 255
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return (r, g, b)


def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
        v = mx   


    h = int(h / 2)
    s = int(s * 255)
    v = int(v * 255)

    return (h, s, v)

def isset(v):
    try:
        type (eval(v))
    except:
        return 0
    else:
        return 1

def contour_red(frame, contours_R, box_r_pos, box_r_pixel):
    for c in contours_R:
        # get rotated rectangle from contour
        rot_rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rot_rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 0), 2)
        M = cv2.moments(c)
        if M["m00"] > 1:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            temp = [cX, cY]
            box_r_pos.append(temp)
            box_r_pixel.append(cX)
        else:
            pass

def contour_blue(frame, contours_B, box_b_pos, box_b_pixel):
    for c in contours_B:
        # get rotated rectangle from contour
        rot_rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rot_rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 0), 2)
        M = cv2.moments(c)
        if M["m00"] > 150:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            temp = [cX, cY]
            box_b_pos.append(temp)
            box_b_pixel.append(cX)
        else:
            pass

def contour_white(frame, contours_W, box_w_pos, box_w_pixel):
    for c in contours_W:
        # get rotated rectangle from contour
        rot_rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rot_rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 0), 2)
        M = cv2.moments(c)
        if M["m00"] > 150:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            temp = [cX, cY]
            box_w_pos.append(temp)
            box_w_pixel.append(cX)
            
        else:
            pass

def grab():
    p1.ChangeDutyCycle(12)#front
    p2.ChangeDutyCycle(2)#front
    time.sleep(0.5)
    p1.ChangeDutyCycle(2)#front
    p2.ChangeDutyCycle(12)#front
    time.sleep(0.5)
    #p.ChangeDutyCycle (2)#close
    #time.sleep(2)
    #for i in range(2, 12):
    #    p1.ChangeDutyCycle(14-i)
    #    p2.ChangeDutyCycle(i)
    #    time.sleep(0.1)
    #p.ChangeDutyCycle(10)#open                
    #time.sleep(2)
```
# Main
```python
#!/usr/bin/python3

import cv2
import numpy as np
from math import radians, degrees, pi, sin, cos
import rospy
from geometry_msgs.msg import Twist, PoseWithCovarianceStamped
import actionlib
import time
from BoxDetectionwithHSV_variables import *
from BoxDetectionwithHSV_function import *

import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees, pi, sin, cos
from actionlib_msgs.msg import *
from geometry_msgs.msg import PoseWithCovarianceStamped
from copy import deepcopy
import tf

''' main '''
# servo
p.start(10)
p1.start(2.5)   #backR
p2.start(11.5)  #backL

while not rospy.is_shutdown():
    # try:
    #     for c in contours_Black:
    #         M = cv2.moments(c)
    #         if M["m00"] > 10:
    #             cY = int(M["m01"] / M["m00"])
    #             print("balck y: ", cY)
    #             if cY > 130:
    #                 right()
    #                 vel_pub.publish(twist)
    #                 break
    # except:
    #     print("black pass")
    #     pass
                
    box_r_pos, box_b_pos, box_w_pos = [], [], []
    box_r_pixel, box_b_pixel, box_w_pixel = [], [], []
    #thresh2 = thresh_R.copy()
    # find contours in the threshold image
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    # finding contour with maximum area and store it as best_cnt
    max_area = 0
    contour_red(frame, contours_Red, box_r_pos, box_r_pixel)
    contour_blue(frame, contours_Blue, box_b_pos, box_b_pixel)
    contour_white(frame, contours_White, box_w_pos, box_w_pixel)
    try:
        total_pixel = box_r_pixel + box_b_pixel + box_w_pixel
        if mode == None:
            if len(total_pixel) != 0:        
                if max(total_pixel) in box_r_pixel:
                    mode = "r"
                elif max(total_pixel) in box_b_pixel:
                    mode = "b"
                elif max(total_pixel) in box_w_pixel:
                    mode = "w"
            else:
                stop()
        
        elif mode == "r":
            if len(box_r_pixel) != 0:
                for i in range(len(box_r_pixel)):
                    if max(total_pixel) == box_r_pixel[i]:
                        if box_r_pos[i][0] < (IMAGE_WIDTH*1)//3:
                            print("turn left")
                            left()
                        elif box_r_pos[i][0] > (IMAGE_WIDTH*2)//3:
                            print("right")
                            right()
                        elif box_r_pos[i][1] > 105:
                            print("grab")
                            mode = "grab"
                            stop()
                        elif (box_r_pos[i][0] >= (IMAGE_WIDTH*1)//3) and (box_r_pos[i][0] < (IMAGE_WIDTH*2)//3):
                            print("forward")
                            forward()
            else:
                stop()
                vel_pub.publish(twist)
                if endtime == time.time():
                    mode = "r_end"
        elif mode == "grab":
            stop()
        elif mode == "r_end":
            for c in contours_Yellow:
                M = cv2.moments(c)
                if M["m00"] > 10:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    count += 1
        else:
            right()
    except:
        print("Exception")
        pass
    count = 0
    #for c in contours_Yellow:
    #    M = cv2.moments(c)
    #    if M["m00"] > 10:
    #        cX = int(M["m10"] / M["m00"])
    #        cY = int(M["m01"] / M["m00"])
    #        count += 1
    #print(count)
    # robot move
    #print("Mode:", mode)
    #print("box_r:", box_r_pos, "pixel", box_r_pixel)
    #print("box_b:", box_b_pos, "pixel", box_b_pixel)
    #print("box_w:", box_w_pos, "pixel", box_w_pixel)
    vel_pub.publish(twist)
    print(current_pose)
    #if mode == "grab":
    #    grab()           
    # if key pressed is 'Esc' then exit the loop
    if cv2.waitKey(33) == 27:
        break
        
# Clean up and exit the program
GPIO.cleanup()
cv2.destroyAllWindows()
cap.release()
```
