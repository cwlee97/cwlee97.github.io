---
layout: single
title: OpenCV Parallel Programming
categories: Autonomous_Driving_course
use_math: false
---

# 영상의 병렬 처리
영상 처리시에 이중 for루프로 모든 픽셀을 돌며 연산을 하게되면 비효율적이다. 따라서 해당 영상을 나누어(예를 들어 4개의 행) 나눈 영상들을 각 코어마다 배정하여 병렬처리를 하게되면 더욱 수월하게 진행된다.

## OpenCV에서 지원하는 병렬 프로그래밍 기법
* Inter TBB(Threading Building Blocks)
* HPX(High Performance ParalleX)
* OpenMP(Open Multi-Processing)
* APPLE GCD(Grand Central Dispatch)
* Window RT concurrency
* Windows concurrency
* Pthreads

## 병렬 처리용 for 루프 함수

```cpp
void parallel_for_(const Range& range, const ParallelLoopBody& body, double nstripes = -1.)
void parallel_for_(const Range& range, std::function<void(const Range&)> functor, double nstripes = -1.)
```

* range: 병렬 처리를 수행할 범위
* body: 함수 객체. ParallelLoopBody 클래스를 상속받은 클래스 또는 C++11 람다 표현식(OpenCV 3.3^)

## ParallelLoopBody 자식 클래스 사용 예제
```cpp
class ParallelContrast : public ParallelLoopBody{
    public:
    ParallelContrast(Mat& src, Mat& dstd, const float alpha): m_src(src), m_dst(dst), m_alpha(alpha) {
        m_dst = Mat::zeros(src.rows, src.cols, src.type());
    }

    virtual void operator()(const Range& range) const {
        for (int  r = range.start; r < range.end; r++_){
            uchar* pSrc = m_src.ptr<uchar>(r);
            uchar* pDst = m_dst.ptr<uchar>(r);
            

            for (int x = 0; x < m_src.cols; x++) pDst[x] = saturate_cast<uchar>((1 + m_alpha) * pSrc[x] - 128 * m_alpha);
        }
    }
    ParallelContrast& operator = (const ParallelContrast &) {
        return *this;
    };

    private:
    Mat& m_src;
    Mat& m_dst;
    float m_alpha;
}

int main(){
    Mat src = imread("hongkong.jpg", IMREAD_GRAYSCALE);
    Mat dst;
    parallel_for_(Range(0, src.rows), ParallelContrast(src, dst, 1.f));
}
```


# 룩업 테이블(LUT: Lookup Table)이란?
* 특정 연산에 대해 미리 결과 값을 계산하여 배열 등으로 저장해 놓은 것
* 픽셀 값을 변경하는 경우, 256 * 1 크기의 unsigned char 행렬에 픽셀 값 변환 수식 결과 값을 미리 저장한 후, 실제 모든 픽셀에 대해 실제 연산을 수행하는 대신 행렬(룩업 테이블) 값을 참조하여 결과 영상 픽셀 값을 설정
* sin, cos같은 입력 값에 따른 출력값이 항상 일정한 테이블을 미리 저장
