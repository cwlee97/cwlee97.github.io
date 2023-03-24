---
layout: single
title: REGEX
categories: Autonomous_Driving_course
---
# Greedy matching이란?
```
$ var2 = "It's gonna be <b>read</b>It's gonna <i>change everything</i> I feel"
$ echo $var2 | egrep -o "<.+>"
```

* pattern은 최대한 많은 수의 매칭을  하려고 하는 성질이 있다.
* 위 코드의 결과값은 <b\>read</b\>It's gonna <i\>change everything</i\>이다.

# Non-greedy matching
태그 부분만을 뽑아내고 싶다면,
```
$ echo $var2 | egrep -o "<[^<>]+>"
```
와 같이 사용한다면 태그 부분만 뽑아낼 수 있다. 위와 같이 사용한다면 최소 매칭이 가능하다.<br>
POSIX RE에서는 non-greedy matching 수량자를 제공하지 않는다. 따라서 패턴을 변경하여 non-greedy matching과 유사한 결과를 얻어낼 수 있다.<br><br>

# vim에티터를 통한 Greedy matching & Non-greedy matching
1. vim 에디터 타이핑<br>
![72.png](../../../images/Autonomous_Driving/Week1/72.png)
<br><br>

2. /<.\\+>으로 검색 - Greedy matching<br>
![73.png](../../../images/Autonomous_Driving/Week1/73.png)
<br><br>

3. /<.\\{-}>으로 검색 - Non-greedy matching<br>
![74.png](../../../images/Autonomous_Driving/Week1/74.png)
<br><br>

# Backslach
* meta char.의 의미를 없앤다.
1. c.b
    * cab, cbb, ccb, cdb 등등..
2. c\\.b
    * dot(.)이 아닌, 진짜 일반 문자 '.'을 의미
* BRE에서 ERE의 일부 기능을 표현할 때 사용
    * ERE의 {m, n}을 BRE로 표현할 때 \\{m, n\\}으로 사용
* 이와 같은 사용을 escape라고 함

