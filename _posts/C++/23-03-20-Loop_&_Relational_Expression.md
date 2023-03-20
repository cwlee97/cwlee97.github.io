---
layout: single
title: "Loop & Relational Expression"
categories: TIL
---
# for Loop
실제 프로그래밍을 하다보면 반복 작업을 손 쉽게 풀어주는 가장 첫 번째 도구는 for loop이다. 오늘은 이 for loop에 대하여 공부해보도록 하자.
```cpp
// Listing 5.1
// forloop.cpp
#include <iostream>
int main()
{
    using namespace std;
    int i;                  // 카운터 선언
    // 초기화; 조건검사; 갱신
    for (i = 0; i < 5; i++)
        cout << "C++ for loop, 5 times\n";
    cout << "for loop end" << endl;
    return 0;
}
```

## for 루프의 각 구문
for 루프는 단계적인 처리를 통해 반복 작업을 수행한다. for 루프가 반복 작업을 어떻게 수행하는지 좀 더 자세히 알아보자. for 루프를 구성하는 각 부분은 순서대로 다음과 같은 단계를 처리한다.
1. 조건 검사에 사용할 카운터 값을 초기화한다.
2. 루프를 진행할 것인지 조건을 검사한다.
3. 루프 몸체를 수행한다.
4. 카운터 값을 갱신한다.

for 루프를 구성하는 각 부분들은 각자의 역할이 무엇인지 알기 쉬운 위치에 자리잡고 있다. 초기화(initialization), 조건 검사(test), 갱신(update)을 처리하는 for 루프의 세 제어 부분은 괄호로 묶여 있다. 이들은 각각 하나의 표현식이며, 세미콜론에 의해 분리되어 있다.<br><br>

루프 몸체는 조건 검사가 참일 경우에만 수행한다.
```cpp
for (initialization; test-expression; update-exptression)
    body
```

test-expression은 루프 몸체 body를 실행할 것인지 여부를 결정한다. 일반적으로 test-expression은 두 개의 값을 서로 비교하는 관계식이다. 이것이 0을 나타내게 되면 bool형 값 false로 변환되고, 루프가 종료된다.
```cpp
// Listing 5.2
// num_test.cpp
#include <iostream>
int main()
{
    using namespace std;
    cout << "카운트 시작값을 입력하십시오: ";
    int limit;
    cin >> limit;
    int i;
    for (i = limit; i; i--)                     // i가 0이면 종료
        cout << "i = " << i << "\n";
    cout << "i = " << i << "이므로 루프를 종료합니다.\n";
    return 0;
}
```
값이 0일 때 로프를 종료하는 test-expression에 i < 5 와 같은 관계 표현식을 사용하였을 때 루프는 어떻게 동작하게 될까? C++에 bool형이 도입되기 이전에 관계 표현식은 참이면 1, 거짓이면 0으로 평가되었다. 즉, i < 5의 값은 1로, 5 < 5의 값은 0으로 평가되었다. 그러나 이제 C++에 bool형이 추가되었으므로, 관계 표현식은 1과 0 대신에 bool형 리터럴 true와 false로 평가된다. C++ 프로그램은 정수값이 요구될 때 true와 false를 1과 0으로 변환한다. 그리고 bool형 값이 요구될 때에는 0은 false로, 0이 아닌 수들은 true로 변환하기 때문에 호환성에 아무런 문제를 일으키지 않는다.<br><br>

x < y와 같은 관계 표현식은 bool값인 true나 false로 평가된다. Listing 5.3은 표현식의 값에 대해 설명하는 예제이다. 여기서 << 연산자는 이 표현식에 사용된 다른 연산자보다 우선순위가 높다. 그렇기 때문에 연산 순서를 정확하게 지정할 목적으로 괄호를 사용하였다.
```cpp
// Listing 5.3
// express.cpp
#include <iostream>
int main()
{
    using namespace std;
    int x;

    cout << "대입 표현식 x = 100의 값은 ";
    cout << (x = 100) << endl;
    cout << "현재 x의 값은 " << x << endl;
    cout << "관계 표현식 x < 3의 정수값은 ";
    cout << (x < 3) << endl;
    cout << "관계 표현식 x > 3의 정수값은 ";
    cout << (x > 3) endl;
    cout.setf(ios_base::boolalpha);
    cout << "관계 표현식 x < 3의 bool값은 ";
    cout << (x < 3) << endl;
    cout << "관계 표현식 x > 3의 bool값은 ";
    cout << (x > 3) << endl;
    return 0;
}
```

## 실행 결과
```
대입 표현식 x = 100의 값은 100
현재 x의 값은 100
관계 표현식 x < 3의 정수값은 0
관계 표현식 x > 3의 정수값은 1
관계 표현식 x < 3의 bool값은 false
관계 표현식 x > 3의 bool값은 true
```
일반적으로 cout은 출력하기 전에 bool값을 int형으로 변환한다. 그러나 cout.setf(ios_base::boolalpha) 함수 호출이 있으면 cout이 1이나 0 대신에 true나 false를 출력하도록 플래그를 설정한다.

## for 루프에 대한 보충
for 루프를 유용한 작업에 사용해보자. Listing 5.4는 for 루프를 사용하여 처음 16개의 계승(factorial)을 계산하여 저장한다. 계승은 다음과 같은 방법으로 계산한다. 먼저 0!은 1로 정의된다. 1!은 1 * 0!, 즉 1이다. 2!은 2 * 1! 즉 2이다. 이런식으로 어떤 정수의 계승은 그 수와 그 수보다 1만큼 작은 수의 계승을 곱해서 계산한다. 이 프로그램은 첫 번째 for루프를 사용하여 연속적인 계승의 값들을 계산하여 배열에 저장한다. 그러고 나서 두 번째 루프를 사용하여 그 결과를 출력한다. 또한 이 프로그램은 값을 보관해 두기 위한 외부 선언도 사용한다.
```cpp
// Listing 5.4
// formore.cpp
#include <iostream>
const int ArSize = 16;
int main()
{
    long long factorials[ArSize];
    factorials[1] = factorials[0] = 1LL;
    for (int i = 2; i < ArSize; i++)
        factorials[i] = i * factorials[i-1];
    for (int i = 0; i < ArSize; i++)
        std::cout << i << "!= " << factorials[i] << std::endl;
    return 0;
}
```

## 갱신 크기 변경
지금까지 for문에 세 번째 인자에 i++이나 i--를 사용하여 1씩 증가 혹은 감소시켰다. 갱신 표현식을 변경하면 루프 카운터가 갱신되는 크기를 바꿀 수 있다. 갱신 표현식으로 i++ 대신에 i = i + by 라는 표현식을 사용한다면 by만큼 증가하는 것이다.
```cpp
// Listing 5.5
// bigstep.cpp
#include <iostream>
int main()
{
    using std::cout;    // using 선언
    using std::cin;
    using std::endl;
    cout << "정수를 하나 입력하십시오: ";
    int by;
    cin >> by;
    cout << "갱신 크기 " << by << "s:\n";
    for (int i = 0; i < 100; i = i + by)
        cout << i << endl;
    return 0;
}
```

## for 루프를 사용한 문자열 처리
for 루프를 사용하여 문자열을 구성하는 문자들에 차례대로 접근할 수 있다. 예를 들어, Listing 5.6은 하나의 문자열을 입력받아 그 문자열을 거꾸로 출력한다. string 클래스 객체 또는 char형의 배열을 이 예제에 사용할 수 있다. 둘 다 배열 표기를 사용하여 문자열에 들어 있는 개별적인 문자에 접근하는 것을 허용한다. Listing 5.6은 string 클래스 객체를 사용한다. string 클래스의 size() 메서드가 문자열을 구성하는 문자 수를 알아낸다. 그러고 나서 루프의 초기화 표현식에서 i를 그 문자열의 마지막 문자를 나타내는 인덱스로 초기화하기 위해 이 값을 사용한다.
```cpp
// Listing 5.6
// forstr1.cpp
#include <iostream>
#include <string>
int main()
{
    using namespace std;
    cout << "단어 하나를 입력하십시오: ";
    string word;
    cin >> word;

    // 문자열을 거꾸로 출력한다.
    for (int i = word.size() - 1; i >= 0; i--)
        cout << word[i];
    cout << "\n종료.\n";
    return 0;
}
```
## 복합 구문 또는 블록
루프 몸체가 하나의 구문이어야 한다는 사실 때문에 for 구문의 구문이 제약적이라고 생각될 수도 있다. 이는 구문을 블록으로 묶어 해결 가능하다.
```cpp
// Listing 5.7
// block.cpp
#include <iostream>
int main()
{
    using namespace std;
    cout << "값 5개의 합계와 평균을 구합니다.\n";
    cout << "값 5개를 입력하십시오.\n";
    double number;
    double sum = 0.0;
    for (int i = 1; i <= 5; i ++)
    {
        cout << "값 " << i << ": ";
        cin >> number;
        sum += number;
    }
    cout << "값 5개가 모두 입력되었습니다.\n";
    cout << "입력한 값 5개의 합계는 " << sum << "입니다.\n";
    cout << "입력한 값 5개의 평균은 " << sum / 5 << "입니다\n";
    return 0;
}
```
위에서 중괄호 안에 모든 내용이 for구문의 몸체가 된다.<br>
복합 구문은 재미있는 특성을 하나 더 가지고 있다. 블록 안에서 새로운 변수를 정의하면, 그 변수는 그 블록 안에 속해 있는 구문들을 실행하는 동안에만 존재하고, 제어가 블록을 빠져나오면 그 변수는 사라진다. 즉, 블록 내의 변수는 블록 안에서만 사용 가능하다.

## 콤마 연산자
매 루프 주기마다 하나의 변수는 1씩 증가하고, 다른 하나의 변수는 1씩 감소해야 하는 루프가 필요하다고 하자. for루프의 갱신 부분에서 이 두가지 일을 함께 처리할 수 있으면 무척 편리할 것이다. 그러나 for 루프의 구문 규칙은 그 자리에 하나의 표현식만을 허용한다. 이 문제를 해결하는 방법은 콤마 연산자를 사용하여 두 개의 표현식을 하나로 결합하는 것이다.
```cpp
// Listing 5.8
// forstr2.cpp
#include <iostream>
#include <string>
int main()
{
    using namespace std;
    cout << "단어를 하나 입력하십시오: ";
    string word;
    cin >> word;
    
    // string 객체를 실제로 변경한다.
    char temp;
    int i, j;
    for (j = 0, i = word.size() - 1; j < i; --i, ++j>)
    {
        temp = word[i];
        word[i] = word[j];
        word[j] = temp;
    }
    cout << word << "\n종료\n";
    return 0;
}
```

## C 스타일 문자열 비교
문자 배열에 들어 있는 문자열이 mate라는 단어인지 알고 싶다고 가정하자.
```
word == "mate"
```
위와 같은 검사는 원하는 바를 수행하지 않는다. 배열의 이름은 주소를 배열의 주소를 나타내고, 큰 따옴표로 묶인 문자열 상수 또한 주소를 나타내기 때문이다.<br>
C++는 C스타일 문자열을 주소로 처리하기 때문에, 문자열 비교 관계 연산자를 사용할 수 없다. 그 대신에 C 스타일의 문자열 라이브러리 함수인 strcmp()를 사용할 수 있다. strcmp()함수는 매개변수로 두 개의 문자열 주소를 취한다. 포인터나 문자열 상수, 문자 배열의 이름을 매개변수로 사용할 수 있다. 두 문자열이 같으면 strcmp() 함수는 0을 리턴한다. 알파벳 순서로 보았을 때 첫 번째 문자열이 두 번째 문자열보다 앞에 오면 음수를 리턴하고, 뒤에 오면 양수를 리턴한다. 여기서 알파벳 순서라는 말보다 시스템 조회 순서(system collating sequence)라는 말이 정확한 표현일 것이다.
```cpp
//Listing 5.9
//compstr1.cpp
#include <iostream>
#include <cstring>      // strcmp() 함수 원형
int main()
{
    using namespace std;
    char word[5] = "?ate";

    for (char ch = 'a'; strcmp(word,"mate"); ch++)
    {
        cout << word << endl;
        word[0] = ch;
    }
    cout << "루프가 끝난 후에 단어는 " << word << "입니다.\n";
    return 0;
}
```

### 실행 결과
```
?ate
aate
bate
cate
date
eate
fate
gate
hate
iate
jate
kate
late
루프가 끝난 후에 단어는 mate입니다.
```

## string 클래스 문자열 비교
클래스 설계가 문자열 비교에 관계 연산자를 사용하는 것을 허용하기 때문에, C스타일 문자열 대신 string 클래스 문자열을 사용하는 것이 훨씬 편리하다. 이것이 가능한 것은, 연산자들을 "오버로딩" 또는 재정의하는 클래스 함수를 정의할 수 있기 때문이다. 이 기능을 클래스 설계와 통합하는 방법은 추후에 공부하기로 하자. 그러나 실제적인 견지에서, 지금 당장은 관계 연산자들을 string 클래스 객체와 함께 사용할 수 있다는 사실만 알면 된다.
```cpp
//Listing 5.10
//compstr2.cpp
#include <iostream>
#include <string>
int main()
{
    using namespace std;
    string word = "?ate";
    for (char ch = 'a'; word != "mate"; ch++)
    {
        cout << word << endl;
        word[0] = ch;
    }
    cout << "루프가 끝난 후에 단어는 " << word << "입니다.\n";
    return 0;
}
```

# while 루프

while 루프는 for 루프에서 초기화한 부분과 갱신 부분을 없애고, 루프 몸체와 조건 검사 부분만 남겨놓은 것이다.

```cpp
while (test-expression)
    body
```

프로그램은 먼저 괄호안의 조건 검사인 표현식 test-expression을 평가한다. 표현식이 true로 평가되면 루프 몸체에 있는 구문(들)을 실행한다. for루프와 마찬가지로, 루프 몸체는 하나의 구문 또는 한 쌍의 중괄호를 묶은 블록이다. 루프 몸체의 실행이 끝나면 조건 검사 표현식으로 돌아와서 표현식을 다시 평가한다. 조건 검사 표현식이 여전히 true이면 루프 몸체를 다시 실행한다.<br>
언젠가 루프를 끝내려면 조건 검사 표현식에 영향을 주는 것이 루프 몸체 안에 있어야 한다.<br>

```cpp
// Listing 5.13
// while.cpp
#include <iostream>
const int ArSize = 20;
int main()
{
    using namespace std;
    char name[ArSize];

    cout << "영문 이름을 입력하십시오: ";
    cin >> name;
    cout << "귀하의 영문 이름을 한 줄에 한 자씩\n";
    cout << "ASCII 코드와 함께 표시하면 이렇습니다.\n";
    int i = 0;
    while (name[i] != '\0')
    {
        cout << name[i] << ": " << int(name[i]) << endl;
        i++;
    }
    return 0;
}
```

## 프로그램 분석
Listing 5.13 프로그램에 사용된 while 조건 검사는 다음과 같다.

```cpp
while (name[i] != '\0')
```

이것은 배열 안에 있는 특정 문자가 널 문자인지 검사한다. 이 조건 검사가 언젠가 성공하려면 루프 몸체 안에서 i의 값을 변경하며 진행하여야 한다.

```cpp
while (name[i])
```

조건 검사식을 위와 같이 바꿔보자. name[i]가 일반적인 문자이고, 그 값이 0이 아니므로 true가 되어 조건문이 실행된다. 그러나 name[i]가 널 문자가 되면 문자 코드의 값이 0이 되어 false가 된다.

# for와 while
C++에서 for루프와 while루프는 사실상 같은 것이다. 예를 들어 다음과 같은 for 루프는
```cpp
for(init-expression; test-expression; update-expression;)
{
    statement(s)
}
```

while 루프를 사용하여 다음과 같이 고쳐 쓸 수 있다.
```cpp
init-expression;
while (test-expression)
{
    statement(s)
    update-expression
}
```

마찬가지로, 다음과 같은 while 루프는
```cpp
while (test-expression)
    body
```

for 루프를 사용하여 다음과 같이 고쳐 쓸 수 있다.
```cpp
for ( ;test-expression;)
    body
```

이 for루프는 세 개의 표현식을 요구한다. 그러나 비어 있는 표현식(구문)도 사용할 수 있다. 세미콜론은 반드시 2개가 필요하다. for 루프에서 조건 검사 표현식을 생략하면 true로 해석된다. 그래서 다음과 같은 루프는 영원히 멈추지 않는다.
```cpp
for( ; ; )
    body
```

for 루프와 while 루프는 거의 동등하기 때문에, 어느 것을 선택하느냐는 사용자의 프로그래밍 스타일에 달려 있다. 일반적으로 for 루프는 초기값, 종료값, 카운터 갱신 방법을 한곳에 넣을 수 있기 때문에 루프를 카운트해야 할 때 주로 사용한다. while 루프는 얼마만큼 루프를 반복해야 할지 미리 알 수 없을때 사용한다.

```
루프를 설계할 때에는 다음과 같은 지침을 고려하자
* 루프 실행을 종료시키는 조건을 파악한다.
* 첫 번째 조건 검사를 하기 전에 그 조건을 초기화한다.
* 조건 검사를 다시 하기 전에 매 루프 주기마다 그 조건을 갱신한다.
```

# 잠시만-시간 지연 루프
시간을 지연시키는 동작을 프로그램 안에 넣어야 할 때가 간혹 있다. 예를 들어, 메시지를 출력한 뒤에 사용자가 그 메시지를 읽기도 전에 다른 동작으로 후딱 전환하는 프로그램이 있다고 가정해 보자. 이렇게 되면 그 메시지가 대단히 중요한데도 어물거리다가 그만 그 정보를 놓칠 수 있다. 대략 5초정도 기다렸다가 다음 동작으로 옮겨간다면 대단히 좋은 프로그램이 될 수 있을 것이다. while루프는 간단하게 이런 효과를 만들어 낸다.
```cpp
long wait = 0;
while (wait < 10000)
    wait++;
```

이 방법의 문제점은 컴퓨터 프로세서의 성능에 따라 카운트 수의 한계를 변경해주어야 한다는 것이다.

ANSI C와 C++ 라이브러리는 이 용도로 사용할 수 있는 clock()이라는 함수를 제공한다. 이 함수는 프로그램이 실행된 순간부터 이 함수가 호출된 순간까지 경과한 시스템 시간을 리턴한다. 그렇지만 이 함수를 사용하는 데에는 두 가지 제약이 있다. 첫째, clock() 함수가 리턴하는 값은 초(second) 단위 시간이 아니다. 둘째, 이 함수가 리턴하는 데이터형은 어떤 시스템에서는 Long형, 다른 시스템에서는 unsigned long형, 또 다른 시스템에서 또다른 데이터형일 수 있다.

clock()함수와 ctime헤더 파일을 사용하여 시간 지연 루프를 만드는 방법을 알아보자.
```cpp
// Listing 5.14
//waiting.cpp
#include <iostream>
#include <ctime>
int main()
{
    using namespace std;
    cout << "지연 시간을 초 단위로 입력하십시오: ";
    float secs;
    cin >> secs;
    clock_t delay = secs * CLOCK_PER_SEC;   // 지연 시간을 시스템 단위 클록 수로 변환
    cout << "카운트를 시작합니다.\a\n";
    clock_t start = clock();
    while (clock() - start < delay) // 시간이 경과할 때까지 대기
        ;                           // 세미콜론에 유의
    cout << "종료\a\n";
    return 0;
}
```

# do while 루프
지금까지 우리는 for 루프와 while 루프에 대해서 알아보았다. 이제는 do while 루프를 살펴볼 차례이다. do while 루프는 for 루프나 while 루프와 달리, 탈출 조건(exit-condition)루프이다. 이 말은 루프 몸체를 먼저 실행하고, 조건을 나중에 검사한다는 뜻이다. 검사하는 조건이 false로 평가되면 루프가 종료된다. 검사하는 조건이 true로 평가되면 새로운 루프 주기와 조건 검사가 시작된다. 그러므로 do while 루프는 조건을 평가하기 전에 루프 몸체를 적어도 한번 실행한다.
```cpp
do
    body
while (test-expression);
```
루프 몸체 부분은 단일 구문 또는 중괄호로 둘러싸인 블록이다. 일반적으로 먼저 조건을 검사하는 루프가 나중에 조건을 검사하는 루프보다 더 나은 선택이다.
```cpp
// Listing 5.15
// dowhile.cpp
#include <iostream>
int main()
{
    using namespace std;
    int n;

    cout << "1부터 10까지의 수 중에서 ";
    cout << "내가 좋아하는 수를 한번 맞추어 보십시오.\n";
    do
    {
        cin >> n;
    } while (n != 7);
    cout << "맞았습니다. 내가 좋아하는 수는 럭키 세븐 7입니다.\n";
    return 0;
}
```
