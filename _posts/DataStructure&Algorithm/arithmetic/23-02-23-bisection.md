---
layout: single
title: "Bisection"
categories: TIL/DataStructure&Algorithm
---
```python
from collections.abc import Callable

def bisection(function, a: float, b: float):
    start = a
    end = b

    if function(a) == 0:    # a 혹은 b가 함수의 근일 때
        return a
    elif function(b) == 0:
        return b
    elif function(a) * function(b) > 0:
        raise ValueError("could not find root in given interval.")
        # 근이 없고, 두 변수의 부호가 같을 때 해당 알고리즘으로 근을 판별할 수 없다.
    else:
        mid = start + (end - start) / 2.0
        while abs(start - mid) > 10 ** -7:
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = start + (end - start) / 2.0
        return mid

def f(x):
    return x ** 3 - 2 * x - 5

if __name__ == "__main__":
    print(bisection(f, 1, 1000))
```
