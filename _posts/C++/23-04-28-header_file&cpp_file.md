---
layout: single
title: Header File & Cpp File
categories: TIL
---

프로젝트를 진행하면서 어지럽게 짜여진 하나의 main파일을 정리하는 방법으로 여러 함수들을 헤더파일과 cpp파일로 나누어 정리하여 깔끔한 main함수를 만들고자 한다.

# Header file
* Declaration(선언)을 담당

## 코드 예시

```cpp
#pragma once
class Person
{
public:
    Person(std::string name, int age)
    :name(std::move(name)), age(age){};
    void print() const;
private:
    std::string name;
    int age;
};
```

# Cpp file
* Definition(정의)를 담당

## 코드 예시

```cpp
#include "person.h"
#include <iostream>

void Person::print() const
{
    std::cout << "name: " << name
    << "age: " << age << std::endl;
}
```

# Compile Process
C++는 forward declaration으로 function/class/variable의 symbol을 읽어서 컴파일을 한다. 여기서 헤더 파일이 해당 역할을 맡아 한다.<br>

cpp는 implementation파트를 컴파일 하고 마지막으로 링크 과정을 통해 프로그램/라이브러리가 완성된다.

# 기존 main.cpp

```cpp
#include <iostream>
#include "opencv2/opencv.hpp"

cv::Size image_size = cv::Size(640, 480);
constexpr int HALF_WIDTH = 320;
constexpr int HALF_HEIGHT = 240;

// Calibrate 관련 변수 선언
double calibrate_mtx_data[9] = {
	350.354184, 0.0, 328.104147,
	0.0, 350.652653, 236.540676,
	0.0, 0.0, 1.0
};
double dist_data[5] = { -0.289296, 0.061035, 0.001786, 0.015238, 0.0 };

cv::Rect roi;

cv::Mat calibrate_mtx(3, 3, CV_64FC1, calibrate_mtx_data);
cv::Mat distCoeffs(1, 4, CV_64FC1, dist_data);
cv::Mat cameraMatrix = getOptimalNewCameraMatrix(calibrate_mtx, distCoeffs, image_size, 1, image_size, &roi);

// calibrate 함수
cv::Mat calibrate_image(cv::Mat const& src, cv::Mat const& map1, cv::Mat const& map2)
{
	// image calibrating
	cv::Mat mapping_image = src.clone();
	cv::Mat calibrated_image;
	remap(src, mapping_image, map1, map2, cv::INTER_LINEAR);

	// image slicing & resizing
	mapping_image = mapping_image(roi);
	resize(mapping_image, calibrated_image, image_size);

	return calibrated_image;
};

// warp 함수
cv::Mat warp_image(cv::Mat image)
{
	// Warping 관련 변수 선언
	int warp_image_width = HALF_WIDTH;
	int warp_image_height = HALF_HEIGHT;

	int warp_x_margin = 30;
	int warp_y_margin = 3;

	cv::Point src_pts1 = cv::Point2f(290 - warp_x_margin, 290 - warp_y_margin);
	cv::Point src_pts2 = cv::Point2f(100 - warp_x_margin, 410 + warp_y_margin);
	cv::Point src_pts3 = cv::Point2f(440 + warp_x_margin, 290 - warp_y_margin);
	cv::Point src_pts4 = cv::Point2f(580 + warp_x_margin, 400 + warp_y_margin);

	cv::Point dist_pts2 = cv::Point2f(0, warp_image_height);
	cv::Point dist_pts3 = cv::Point2f(warp_image_width, 0);
	cv::Point dist_pts4 = cv::Point2f(warp_image_width, warp_image_height);
	cv::Point dist_pts1 = cv::Point2f(0, 0);

	std::vector<cv::Point2f> warp_src_mtx = { src_pts1, src_pts2, src_pts3, src_pts4 };
	std::vector<cv::Point2f> warp_dist_mtx = { dist_pts1, dist_pts2, dist_pts3, dist_pts4 };

	cv::Mat src_to_dist_mtx = getPerspectiveTransform(warp_src_mtx, warp_dist_mtx);

	cv::Mat warped_image;
	warpPerspective(image, warped_image, src_to_dist_mtx, cv::Size(warp_image_width, warp_image_height), cv::INTER_LINEAR);

	// warp 기준점 확인
	circle(image, src_pts1, 20, cv::Scalar(255, 0, 0), -1);
	circle(image, src_pts2, 20, cv::Scalar(255, 0, 0), -1);
	circle(image, src_pts3, 20, cv::Scalar(255, 0, 0), -1);
	circle(image, src_pts4, 20, cv::Scalar(255, 0, 0), -1);

	return warped_image;
};

cv::Mat warp_process_image(cv::Mat image)
{
	int num_sliding_window = 20;
	int width_sliding_window = 20;
	int min_points = 5;
	int lane_bin_th = 145;

	cv::Mat blur;
	GaussianBlur(image, blur, cv::Size(5, 5), 0);

	cv::Mat hls;
	cvtColor(blur, hls, cv::COLOR_BGR2HLS);
	std::vector<cv::Mat> L;
	split(hls, L);

	cv::Mat lane;
	threshold(L[1], lane, lane_bin_th, 255, cv::THRESH_BINARY);
	// threshold(L, lane, lane_bin_th, 255, THRESH_BINARY_INV);

	return lane;
}


int main()
{
	// Video load
	cv::VideoCapture capture("track2.avi");

	if (!capture.isOpened()) {
		std::cerr << "Image laod failed!" << std::endl;
		return -1;
	}

	cv::Mat src;

	/*
	* FPS 세팅함수를 사용해서 배속조정이 가능한지 실험해보았는데, 해당 함수로는 배속 조정이 불가합니다.
	capture.set(CAP_PROP_FPS, 50);
	*/

	// Video width, height 설정
	capture.set(cv::CAP_PROP_FRAME_WIDTH, 640);
	capture.set(cv::CAP_PROP_FRAME_HEIGHT, 480);

	// FPS 측정을 위한 변수 선언
	int capture_fps = capture.get(cv::CAP_PROP_FPS);

	// 기존 undistort함수를 initUndistortRectifyMat(), remap()으로 나눠 loop 밖에서 initUndistortRectifyMat() 선언
	cv::Mat map1, map2;
	initUndistortRectifyMap(calibrate_mtx, distCoeffs, cv::Mat(), cameraMatrix, image_size, CV_32FC1, map1, map2);


	while (true) {
		capture >> src;

		if (src.empty()) {
			std::cerr << "Frame empty!" << std::endl;
			break;
		}

		// FPS 출력
		std::cout << "fps:" << capture_fps << std::endl;

		// calibrate image
		cv::Mat calibrated_image = calibrate_image(src, map1, map2);

		// warp image
		cv::Mat warped_image = warp_image(calibrated_image);

		cv::Mat lane = warp_process_image(warped_image);

		// Image 출력
		imshow("src", src);
		imshow("calibrated image", calibrated_image);
		imshow("warped image", warped_image);
		imshow("bin", lane);

		// waitKey(n)의 n값에 따라 동영상의 배속, 감속됨
		if (cv::waitKey(20) == 27) // ESC
			break;
	}
}
```
