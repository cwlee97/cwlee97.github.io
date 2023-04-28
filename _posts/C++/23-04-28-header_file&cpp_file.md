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