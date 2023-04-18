---
layout: single
title: Opencv Function & Class
categories: Autonomous_Driving_course
use_math: true
---

# 영상 파일 불러오기
```cpp
#include <iostream>
#include "opencv2/opencv.hpp"

using namespace cv;
using namespace std;

int main()
{
    Mat img = imread("lenna.bmp");

    if (img.empty()) {
        cerr << "Image load failed" << endl;
        return -1;
    }

    namedWindow("image"));
    imshow("Image", img);
    waitKey();
    destroyAllWindows();
}
```

# 함수

## 영상 파일 불러오기

```cpp
Mat imread(const String& filename, int flags = IMREAD_COLOR);
```

* filename: 불러올 영상 팡리의 이름
* flags: 영상 파일 불러오기 옵션 플래그
    * IMREAD_UNCHANGED: 영상 속성 그대로 읽기
    * IMREAD_GRAYSCALE: 1채널 그레이스케일 영상으로 읽기
    * IMREAD_COLOR: 3채널 BGR컬러 영상으로 읽기
* 반환값: 불러온 영상 데이터(Mat)

## 비어있는 Mat객체 확인

```cpp
bool Mat::empty() const
```

* 반환값: rows, cols, data 멤버 변수가 0이면 true 반환

## 영상 파일 저장하기
```cpp
bool imwrite(const String& filename, InputArray img,
             const std::vector<int>& params = std::vector<int>());
```

* filename: 저장할 영상 파일 이름. 파일 이름에 포함된 확장자를 분석하여 해당 파일 형식으로 저장됨
* img: 저장할 영상 데이터(Mat)
* params: 파일 저장 옵션 지정(속성 & 값의 정수 쌍)
* 반환값: 정상적으로 저장하면 true, 실패하면 false

## 새 창 띄우기
```cpp
void namedWindow(const String& winname, int flages = WINDOW_AUTOSIZE);
```

* winname: 창 고유 이름
* flags: 창 속성 지정 플래그
    * WINDOW_NORMAL: 영상 크기가 창 크기에 맞게 지정됨
    * WINDOW_AUTOSIZE: 창 크기가 영상 크기에 맞게 자동으로 변경됨
    * WINDOW_OPENGL: OPENGL 지원

## 창 닫기
```cpp
void destroyWindow(const String& winname);
void destroyAllWindows();
```

* winname: 닫고자 하는 창의 이름
* 참고사항
    * 일반적인 경우 프로그램 종료 시 운영 체제에 의해 열려 있는 모든 창이 자동으로 닫힘

## 창 위치 지정
```cpp
void moveWindow(const String& winname, int x, int y);
```

* winname: 창 이름
* x, y: 이동할 위치 좌표

## 창 크기 지정
```cpp
void resizeWindow(const String& winname, int width, int height);
```

* winname: 창 이름
* width, height: 변경할 창의 크기
* 참고 사항
    * 윈도우가 WINDOW_NORMAL 속성으로 생성되어야 동작함

## 영상 출력하기
```cpp
void imshow(const String& winname, InputArray mat);
```

* winname: 영상을 출력할 대상 창 이름
* mat: 출력할 영상 데이터

* 영상 출력 방식
    * 8-bit unsigned: 픽셀 값을 그대로 출력
    * 16-bit unsigned or 32-bit integer: 픽셀 값을 255로 나눠 출력
    * 32-bit or 64-bit floating-point: 픽셀 값에 255를 곱해 출력

* 참고 사항
    * 만약 winname에 해당하는 창이 없으면 WINDOW_AUTOSIZE 속성의 창을 새로 만들고 영상을 출력함
    * 실제로는 waitKey() 함수를 호출해야 화면에 영상이 나타남

## 키보드 입력 대기
```cpp
int waitKey(int delay = 0);
```

* delay: 밀리초 단위 대기시간. delay <= 0 이면 무한히 기다림
* 반환 값: 눌린 키 값. 키가 눌리지 않으면 -1
* 참고 사항:
    * waitKey()함수는 openCV창이 하나라도 있어야 정상 동작함
    * imshow() 함수 호출 후에 waitKey()함수를 호출해야 영상이 화면에 나타남
    * 주요 특수키 코드 ESC -> 27, ENTER -> 13, TAB -> 9


# OpenCV 주요 클래스
## Point_
* 2차원 점의 좌표 표현을 위한 템플릿 클래스
* 멤버 변수: x, y
* 멤버 함수: dot(), ddot(), cross(), inside() 등
* norm(pt): 원점부터 point까지의 거리 반환
* 다양한 사칙 연산에 대한 연산자 오버로딩과 std::cout 출력을 위한 << 연산자 오버로딩을 지원

## Size_
* 영상 또는 사각형의 크기 표현을 위한 템플릿 클래스
* 멤버 변수: width, height
* 멤버 함수: area()
* 다양한 사칙 연산에 대한 연산자 오버로딩과 std::cout 출력을 위한 << 연산자 오버로딩 지원

## Rect_
* 2차원 사각형 표현을 위한 템플릿 클래스
* 멤버 변수: x, y, width, height
* 멤버 함수: tl(), br(), size(), area(), contains()
* 다양한 사칙 연산에 대한 연산자 오버로딩과 std::cout 출력을 위한 << 연산자 오버로딩을 지원

## Range
* 정수 값의 범위를 나타내기 위한 클래스
* 멤버 변수: start, end
* 멤버 함수: size(), empty(), all()
* start는 범위에 포함되고 end는 범위에 포함되지 않음

## String
* 원래 OpenCV에서 자체적으로 정의하여 사용하던 문자열 클래스였으나, OpenCV 4.x 버전부터 std::string 클래스로 대체됨
```cpp
typedef std::string cv::String;
```

* cv::format()함수를 이용하여 형식 있는 문자열 생성 가능 -> C언어의 printf() 함수 인자 전달 방식이 유사함


## Vec
* 벡터(vector)는 같은 자료형 원소 여러 개로 구성된 데이터 형식
* Vec클래스는 벡터를 표현하는 템플릿 클래스
* std::cout 출력을 위한 << 연산자 오버로딩을 지원

## Scalar
* 크기가 4인 double배열을 멤버 변수로 가지고 있는 클래스
* 4채널 이하의 영상에서 픽셀값을 표현하는 용도로 자주 사용
* []연산자를 통해 원소에 접근 가능

## Mat
* n차원 1채널 또는 다채널 행렬 표현을 위한 클래스
    * 실수 또는 복소수 행렬, GrayScale 또는 트루 컬러 영상, 벡터 필드, 히스토그램, 텐서 등을 표현
* 다양한 형태의 행렬 생성, 복사, 행렬 연산 기능을 제공
    * 행렬의 생성 시 행렬의 크기, 자료형과 채널 수(타입), 초기값 등을 지정할 수 있음
    * 복사 생성자 & 대입 연산자는 얕은 복사 수행(참조 계수로 관리)
    * 깊은 복사는 Mat::copyTo() 또는 Mat::clone()함수 사용
    * 다양한 사칙 연산에 대한 연산자 오버로딩과 std::cout 출력을 위한 << 연산자 오버로딩 지원
* 행렬의 원소(픽셀 값) 접근 방법을 제공
    * Mat::data 멤버 변수가 실제 픽셀 데이터 위치를 가리킴<br>
    $addr(M_{i,j})=M.data+M.step[0]*i+M.step[1]*j$
    * Mat::at<typename\>(int y, int x) 또는 Mat::ptr<typename\>(int y) 함수 사용을 권장

## InputArray
* 주로 Mat 클래스를 대체하는 프록시 클래스(proxy class)로 OpenCV 함수에서 입력 인자로 사용됨
* 사용자가 명시적으로 _InputArray 클래스의 인스턴스 또는 변수를 생성하여 사용하는 것을 금지

## OutputArray
* OpenCV 함수에서 출력 인자로 사용되는 프록시 클래스
* _OutputArray 클래스는 _InputArray 클래스를 상속받아 만들어졌으며, 새로운 행렬을 생성하는 create() 함수가 정의되어 있음
