---
layout: single
title: Opencv 4.5.5 Install - Ubuntu 18.04
categories: TIL
use_math: true
---

프로젝트 진행에 있어서 Xycar와 환경을 맞추기 위해 VMware에 Opencv 4.5.5 version을 설치해야하는데 설치 내용을 기록해 두고자 한다.

1. Check to see if OpenCV is already installed
```
pkg-config --modversion opencv
```

2. If you see it already installed delete the previous version by executing the following commands
```
sudo apt-get purge libopencv* python-opencv
sudo apt-get autoremove
```

3. Delete all the existing OpenCV libraries
```
sudo find /usr/local/ -name "*opencv*" -exec rm {} \;
```

4. Update and upgrade packages on Ubuntu
```
sudo apt-get update
sudo apt-get upgrade
```

5. Install build-essential and cmake packages
```
sudo apt-get install build-essential cmake
```

6. Install pkg-config
```
sudo apt-get install pkg-config
```

7. Install packages for recording images in a certain format
```
sudo apt-get install libjpeg-dev libtiff5-dev libpng-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev
```

8. Install drivers to capture real-time video capture on Linux
```
sudo apt-get install libv4l-dev v4l-utils
```

9. Install GStreamer
```
sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
```

10. Use GUI to show images
```
sudo apt-get install libgtk2.0-dev
```

11. Install OpenGL libraries
```
sudo apt-get install mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev
```

12. Install libraries to optimize OpenCV
```
sudo apt-get install libatlas-base-dev gfortran libeigen3-dev
```

13. Install Python dev packages
```
sudo apt-get install python2.7-dev python3-dev python-numpy python3-numpy
```

14. Create OpenCV directory then move on
```
mkdir opencv # ~/opencv
cd opencv
```

15. Download and unzip OpenCV source code
```
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.5.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.5.zip
unzip opencv_contrib.zip
```

16. Create a build directory which takes care of compilation
```
cd opencv-4.5.5/
mkdir build # ~/opencv/opencv-4.5.5/build
cd build
```

17. Utilize 'cmake' to configure OpenCV complie settings
```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D WITH_TBB=OFF \
-D WITH_IPP=OFF \
-D WITH_1394=OFF \
-D BUILD_WITH_DEBUG_INFO=OFF \
-D BUILD_DOCS=OFF \
-D INSTALL_C_EXAMPLES=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D BUILD_EXAMPLES=OFF \
-D BUILD_TESTS=OFF \
-D BUILD_PERF_TESTS=OFF \
-D WITH_QT=OFF \
-D WITH_GTK=ON \
-D WITH_OPENGL=ON \
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.5.5/modules \
-D WITH_V4L=ON  \
-D WITH_FFMPEG=ON \
-D WITH_XINE=ON \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D OPENCV_GENERATE_PKGCONFIG=ON ../
```

if you see the message like below, you successfully finished configuration

Configuring done<br>
Generating done<br>
Build files have been written to: /home/webnautes/opencv/opencv-4.5.5/build<br>

18. If you have more than 4 cores, then use the following command
```
time make -j4
```

19. Install Output
```
sudo make install
```

20. Install CV Bridge which works between ROS and CV
```
sudo apt-get install ros-melodic-cv-bridge
```

21. This will be used to publish the camera feedback. To be able to subscribe we must be able to publish the data. Instill the video stream package first
```
sudo apt-get install ros-melodic-video-stream-opencv
```

Ref: https://www.daslhub.org/unlv/wiki/doku.php?id=installing_opencv4_on_ubuntu_18