---
layout: single
title: The Code Explained
categories: Autonomous_Driving_course
---
# teacher.py
```py
#!/usr/bin/env python   
# Sheband(#!)라인
# 문법: #!<interpreter> [optional-arg]
#스크립트 파일의 첫 줄에 사용된다.
# 해당 파일의 실행에 어떤 인터프리터를 사용할지 지정한다.
# PATH 환경변수에서 가장 우선되는 인터프리터를 찾아해당 스크립트 파일을 실행한다.

import rospy    # rospy 모듈 임포트
from std_msgs.msg import String # std_msgs의 모듈 중 String 모듈을 임포트

rospy.init_node('teacher')
'''
----- init_node() -----
노드 초기화 및 노드 이름 설정
노드에는 고유의 이름을 할당해야함
---가장 많이 쓰이는 형태---
rospy.init_node('my_node_name')
and
rospy.init_node('my_node_name', anonymous=True)
'''

pub = rospy.Publisher('my_topic', String)
'''
----- rospy.Publisher() -----
토픽 이름, 메시지 클래스, queue_size를 인자로 갖는다.
pub = rospy.Publisher('topic_name', std_msgs.msg.String, queue_size=10)
topic_name 이라는 이름의 토픽을 발행하겠다고 ROS 시스템에 자신을 Publisher로 등록하는 부분
'''
rate = rospy.Rate(2) # 1초에 2번 loop를 반복할 수 있도록 설정

while not rospy.is_shutdown():  # 시스템이 shutdown되기 전 까지 실행문 반복
    pub.publish('call me please') # 'call me please' 메시지를 topic_name에 담아 Publish
    rate.sleep()    # rospy.Rate()에서 설정한 주기만큼 반복문이 돌 수 있게 반복문 내에 선언
```

# student.py
```py
#!/usr/bin/env python
# Sheband(#!)라인
# 문법: #!<interpreter> [optional-arg]
#스크립트 파일의 첫 줄에 사용된다.
# 해당 파일의 실행에 어떤 인터프리터를 사용할지 지정한다.
# PATH 환경변수에서 가장 우선되는 인터프리터를 찾아해당 스크립트 파일을 실행한다.

import rospy    # rospy 모듈 임포트
from std_msgs.msg import String # std_msgs의 모듈 중 String 모듈을 임포트

def callback(msg):  # callback이라는 함수 정의
    print msg.data  # msg.data 출력
    
rospy.init_node('student')
'''
----- init_node() -----
노드 초기화 및 노드 이름 설정
노드에는 고유의 이름을 할당해야함
---가장 많이 쓰이는 형태---
rospy.init_node('my_node_name')
and
rospy.init_node('my_node_name', anonymous=True)
'''

sub = rospy.Subscriber('my_topic', String, callback)
'''
----- rospy.Subscriber() -----
토픽을 받는 구독자 노드
받는 토픽의 이름: 'my_topic'
토픽 데이터 타입: String
토픽이 도착할 때 마다 callback함수 호출
'''
rospy.spin()    # 노드가 shutdown되기 전 까지 Block
```