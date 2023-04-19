---
layout: single
title: Opencv with C++
categories: Autonomous_Driving_course
use_math: true
---

# 카메라 열기
```cpp
VideoCapture::VideoCapture(int index, int apiPreference = CAP_ANY);
bool VideoCapture::open(int index, apiPreference = CAP_ANY);
```

* index: 사용할 캡쳐 장비의 ID, 시스템 기본 카메라를 열려면 0을 지정
* apiPreference: 선호하는 카메라 처리 방법을 지정
* 반환값: VideoCapture 생성자는 VideoCapture 객체를 반환, VideoCapture::open() 함수는 작업이 성공하면 true, 실패하면 false 반환
* filename: 동영상 파일 이름, 정지 영상 시퀀스, 비디오 스트림 URL등

```cpp
bool VideoCapture::read(OutputArray image);
VideoCapture& VideoCapture::operator >> (Mat& image);
```

* image: 현재 프레임. 만약 현재 프레임을 받아오지 못하면 비어 있는 영상으로 설정됨
* 반환값: VideoCapture::read() 함수는 작업이 성공하면 true, 실패하면 false를 반환

```cpp
double VideoCapture::get(int propId) const;
bool VideoCapture::set(int propId, double value);
```

* propid:  속성 플래그. cv::VideoCaptureProperties 또는 Additional flags for video I/O backends 상수 중 선택
* Reference: https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html?highlight=get#cv2.VideoCapture.get
* value: 속성 값. 필요한 경우 정수형으로 변환하여 사용

# OpenCV 그리기 함수

## 직선 그리기
```cpp
void line(InputOutputArray img, Point pt1, Point pt2, const Scalar& color, int thickness = 1, int lineType = LINE_8, int shift = 0);
```

* lineType: 선 타입, LINE_4, LINE_8, LINE_AA 중 하나를 지정
* shift: 그리기 좌표 값의 축소 비율

## 사각형 그리기
```cpp
void rectangle(InputOutputArray img, Rect rec, const Scalar&color, int thickness = 1, int lineType = LINE_8, int shift = 0);
```

## 원 그리기
```cpp
void circle(InputOutputArray img, Point center, int radius, const Scalar& color, int thickness = 1, int lineType = LINE_8, int shift = 0);
```

## 다각형 그리기 함수
```cpp
void polylines(InputOutputArray img, InputOutputArray pts, bool isClosed, const Scalar& color, int thickness = 1, int lineType = LINE_8, int shift = 0);
```

## 문자열 출력하기
```cpp
void putText(InputOutputArray img, const String& text, Point org, int fontFace, double fontScale, Scalar color, int thickness = 1, int lineType = LINE_8, bool bottomLeftOrigin = false);
```

# 이벤트 처리하기
## 키보드 입력 대기
```cpp
int waitKey(int delay = 0);
```
* delay: 밀리초 단위 대기 시간. delay <= 0이면 무한히 기다림
* 반환 값: 눌린 키 값. 키가 눌리지 않으면 -1

## 마우스 이벤트 처리를 위한 콜백 함수 등록
```cpp
void setMouseCallback(const String& winname, MouseCallback onMouse, void* userdata = 0);
```

* winname: 창 이름
* onMouse: 마우스 콜백 함수 이름

```cpp
typedef void (*MouseCallback)(int event, int x, int y, int flags, void* userdata);
```
* #include <opencv2/highgui.hpp>
* event: 마우스 이벤트 종류
* x, y: 마우스 이벤트 발생 좌표
* flags: 마우스 이벤트 플래그
* userdata: setMouseCallback() 함수에서 지정한 사용자 지정 데이터

# 유용한 OpenCV 함수
## 행렬의 합 구하기
```cpp
Scalar sum(InputArray src);
```

## 행렬의 평균 구하기
```cpp
Scalar mean(InputArray src, InputArray mask = noArray());
```

* mask: 마스크 영상

## 행렬의 최대, 최솟값 구하기
```cpp
void minMaxLoc(InputArray src, double* minVal, double* maxVal = 0, Point* minLoc = 0, Point* maxLoc = 0, InputArray mask = noArray());
```

* minVal, maxVal: 최대, 최솟값 변수 포인터
* minLoc, maxLoc: 최대, 최솟값 위치 변수 포인터

## 행렬의 자료형 변환
```cpp
void Mat::convertTo(OutputArray m, int rtype, doubel alpha = 1, double beta = 0) const;
```

* m: 출력 영상
* rtype: 원하는 출력 행렬 타입
* alpha: 추가적으로 곱할 값
* beta: 추가적으로 더할 값

## 행렬의 정규화
```cpp
void normalize(InputArray src, InputOutputArray dst, double alpha = 1, double beta = 0, int norm_type = NORM_L2, int dtype = -1, InputArray mask = noArray());
```

## 색 공간 변화 함수
```cpp
void cvtColor(InputArray src, OutputArray dst, int code, int dstCn = 0);
```

* dstCn: 결과 영상의 채널 수. 0이면 자동 결정됨

## 채널 분리
```cpp
void split(const Mat& src, Mat* mvbegin);
void split(InputArray src, OutputArrayOfArrays mv);
```

* mvbegin: Mat 배열의 주소
* mv: 행렬의 벡터. vector<Mat\>

## 채널 결합
```cpp
void merge(const Mat* mv, size_t count, OutputArray dst);
void merge(InputArrayOfArrays mv, OutputArray dst);
```

