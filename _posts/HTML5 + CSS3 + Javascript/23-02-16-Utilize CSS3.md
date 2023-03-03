---
layout: single
title: "Utilize CSS3"
categories: TIL
---
# CSS3 고급 활용
HTML 태그가 출력되는 모양은 항상 박스(box model)이다.
* 배치
* 리스트 꾸미기
* 표 꾸미기
* 폼 꾸미기
* 애니메이션 등 동적 변화 만들기
에 대해 알아보고자 한다.

# 1. 배치
앞서 작성한 코드들은 웹 페이지에 작성된 순서대로 출력되는것이 대부분이었다. CSS3를 이용하면 HTML 태그를 브라우저의 특정 위치에 고정 출력시키거나, 스크롤바를 굴려도 항상 그 자리에 보이도록 할 수 있고, 경우에 따라 보이지 않게 숨길 수도 있다. 이와 같은 기능을 배치(positioning)라고 부른다.

## CSS3 property

* display
* position
* left, right, top, bottom
* float
* z-index
* visibility
* overflow

## 블록 박스와 인라인 박스
HTML 태그는 블록 태그와 인라인 태그로 나뉜다.
* 블록 태그(새 라인에서 시작. 옆에 다른 태그 배치 불가): <p\>, <hl\>, <div\>, <ul\>
* 인라인 태그(블록 안에 배치. 옆에 다른 태그 배치 가능): <span\>, <a\>, <img\>

## 박스의 유형 제어, display
* property
    * 블록 박스- display: block
    * 인라인 박스- display: inline
    * 인라인 블록 박스- display: inline-block

## 박스의 배치, position
* 정적 배치- position: static(default)
* 상대 배치- position: relative
* 절대 배치- position: absolute
* 고정 배치- position: fixed
* 유동 배치- float: left or float: right

## float property를 이용한 유동 배치
보통 마우스로 브라우저 크기를 변경하면, 텍스트나 이미지가 다음 줄로 내려가는 등 위치가 변한다. 하지만 float property를 지정하면 태그를 오른편이나 왼편에 항상 배치시킬 수 있다.

## 수직으로 쌓기, z-index
HTML 태그들을 z축을 딸라 수직으로 쌓는 순서(stacking order)를 지정하는 프로퍼티로 값이 클수록 위에 쌓인다.

## 보일 것인가 숨길 것인가, visibility
HTML 태그를 출력할 것인지 숨길 것인지를 지정할 수 있다. visibility:hidden은 HTML태그에 출력공간을 할당한 채 보이지만 않게 한다.

## 콘텐츠를 자를 것인가 말 것인가, overflow
HTML 콘텐츠가 width와 height 프로퍼티에 주어진 태그의 크기를 넘어가는 경우 콘텐츠를 자를 것인지 말 것인지를 지정하는 프로퍼티로서, 블록 태그에만 적용된다.
프로퍼티가 적용되려면 width와 height 프로퍼티에 박스 크기가 설정되어 있어야 한다.

# 2. 리스트 꾸미기
리스트는 데이터를 나열하여 보여주는 목적 외에도 목차를 만들거나 메뉴를 만들거나 관련 링크 모음을 만드는 등, 웹 페이지에서 여러 가지 용도로 활용된다.

## List를 꾸미는 CSS3 property
* list-style-type: 아이템 마커 타입 지정
* list-style-image: 아이템 마커 이미지 지정
* list-style-position: 아이템 마커의 출력 위치 지정(아이템 영역 내 혹은 영역 바깥)
* list-style: 앞의 3개 프로퍼티 값을 한번에 지정하는 단축 프로퍼티

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h3>커피 메뉴</h3>
        <hr>
        <ul>
            <li>Espresso</li>
            <li>Cappuccino</li>
            <li>Cafe Latte</li>
        </ul>
    </body>
</html>
```

## 리스트와 아이템의 배경
background 프로퍼티로 리스트나 아이템에 배경색이나 배경 이미지를 줄 수 있다.
```html
ul {
    background: goldenrod;
    padding: 10px 10px 10px 50px;
}
ul li {
    background: greenyellow;
    margin-bottom: 5px;
}
```

## 마커의 위치, list-style-position
마커의 위치를 지정할 때 사용
```html
list-style-position: inside | outside(default)
```

## 마커 종류, list-style-type
```html
list-style-type: disc | ormenion | circle | cjk-ideographic | decimal | georgian | lower-alpha | lower-roman | upper-alpha | upper-roman | none
```

## 이미지 마커, list-style-image
개인이 소유한 이미즈를 마커로 만들 수 있게 한다. 공통 이미지를 모든 아이템 마커로 적용할 수 있고, 아이템마다 다른 이미지를 달 수도 있다.

## 리스트 단축 프로퍼티, list-style
마커의 타입, 위치, 이미지 등을 한번에 지정하는 단축 프로퍼티
```html
list-style: list-style-type list-style-position list-style-image
```

## CSS3 스타일을 응용하여 리스트로 메뉴 만들기
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <style>
            #menubar {
                background: olive;
            }
            #menubar ul{
                margin: 0;
                padding: 0;
                width: 567px;
            }
            #menubar ul li{
                display: inline-block;
                list-style-type: none;
                padding: 0px 15px;
            }
            #menubar ul li a{
                color: white;
                text-decoration: none;
            }
            #menubar ul li a:hover{
                color: violet;
            }
        </style>
    </head>
    <body>
        <nav id="menubar">
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Espresso</a></li>
                <li><a href="#">Cappuccino</a></li>
                <li><a href="#">Cafe Latte</a></li>
                <li><a href="#">F.A.Q</a></li>
            </ul>
        </nav>
    </body>
</html>
```
# 3. 표 꾸미기
CSS3 스타일 시트를 활용한 표 꾸미기
## 표 테두리 제어, border
border값은 테두리의 두께, 모양, 색을 지정 가능
```html
table {
    border: 1px solid blue;
}
td, th{
    border: 1px dotted green;
}
```
<table\>, <td\>, <th\>에 모두 테두리를 주었기 때문에 테두리가 이중으로 나타난다. 이를 하나로 합치려면 border-collapse property에 collapse값을 주면 된다.
```html
table {
    border: 1px solid blue;
    border-collapse: collapse;
}
td, th{
    border: 1px dotted green;
}
```

## 셀 크기 제어, width height
width와 height property를 이용하면 셀의 크기를 지정할 수 있다.
```html
th{
    height: 40px;
    width: 100px;
}
td{
    height: 20px;
    width: 100px;
}
```
또한 셀의 크기를 %단위로 지정할 수도 있다. 브라우저의 폭에 같은 비율로 출력하고자 할 때 사용한다.
```html
table{width: 100%;}
```
## 셀 여백 및 정렬
디폴트로 <th\>셀은 중앙 정렬, <td\> 셀은 왼쪽 정렬이다. 하지만 text-align property에 left, right, center 등의 값으로 정렬 방식을 바꿀 수 있다.
```html
td, th{
    height: 20px;
    width: 100px;
    padding: 10px;
    text-align: right;
}
```
## 배경색과 테두리 효과
셀의 배경색은 가독성을 높인다. 배경색은 background, 글자는 color property를 사용한다.
```html
thread{
    background: darkgray;
    color: yellow;
}
```
## 줄무늬 만들기
배경색과 더불어 줄무늬도 가독성에 영향을 준다.
```html
tr:nth-child(even){
    background: aliceblue;
}
```

# 4. 폼 꾸미기
많은 웹 사이트들이 고객이나 방문객으로부터 질의를 받는 contact us 페이지를 두고 있다.
contact us 페이지를 만드는 사례를 통해 폼을 꾸미는 CSS3 스타일을 알아보자.

## input[type=text]로 폼 요소에 스타일 입히기
셀렉터 중에는 속성 값이 일치하는 HTML 태그에만 스타일을 적용하는 속성 셀렉터가 있음. 다음은 type 속성 값이 'text'인 <input\> 태그에 글자를 red로 출력하는 경우이다.
```html
input[type=text] {
    color: red;
}
```

## input[type=text]로 폼 요소의 테두리 만들기
```html
input[type=text]{
    border: 2px solid skyblue;
    border-radius: 5px;
}
```

## 폼 요소에 마우스 처리
폼 요소에 마우스가 접근할 때 폼 요소의 모양을 바꿔보자
* 마우스가 올라올 때, :hover
```html
input[type=text]{
    color: red;
}
input[type=text]:hover{
    background: aliceblue;
}
```

* 입력할 때, :focus
포커스는 키 입력에 대한 독점권을 뜻함.
```html
input[type=text]:focus{
    font-size: 120%;
}
```

# 5. CSS3 스타일로 태그에 동적 변화 만들기
자바스크립트를 사용하지 않고 CSS3 만으로 HTML 태그의 모양에 동적인 변화를 줄 수 있다.
* 애니메이션(animation)
* 전환(transition)
* 변환(transform)

## 애니메이션
HTML 태그의 모양 변화를 시간 단위로 설정하여 쉽게 애니메이션 효과를 만들 수 있다. 다만 2가지 작업이 필요하다.
1. 시간별 애니메이션 장면 작성
```html
@keyframs name{
    시간비율 {스타일; 스타일;}
    ...
    시간비율 {스타일; 스타일;}
}

@keyframes textColorAnimation {
    0% {color: blue;}
    30% {color: green;}
    100% {color: red;}
}
```

2. 애니메이션 스타일 시트 작성
```html
animation-name: 애니메이션 이름;
animation-duration: 시간;
animation-iteration-count: 애니메이션 반복 횟수;

span{
    animaiton-name: textColorAnimation;
    animation-duration: 5s;
    animation-iteration-count: infinite;
}
```

## 전환
전환이란 HTML 태그에 적용된 CSS3 property 값이 변할 때, 값의 변화를 서서히 진행시켜 애니메이션 효과를 내는 것이며, 1회만 시행한다.

1. 전환 프로퍼티와 전환 시간 지정
```html
transition: 전환프로퍼티 전환시간
/* 전환프로퍼티: 이 프로퍼티 값이 변경되면 현재 값에서 새 값으로 전환효과 시작
전환시간: 현재 값에서 새 값으로 전환하는데 걸리는 시간 */

span{
    transition: font-size 5s;
}
```

2. 전환 효과 시작
전환 프로퍼티의 값이 변경되면 전환은 자동으로 진행됨.
전환 프로퍼티의 현재 값에서 바뀐 값까지 전환 시간동안 진행됨.
```html
span:hover{
    font-size: 500%;
}
```
위의 코드는 span 태그에 마우스가 올라가면 font-size를 500%로 변경함.
이전 전환 시간을 5초로 정해두었기에 5초동안 font-size가 500%까지 커지는 애니메이션 효과 생성

## 변환
CSS3의 변환 기능은 텍스트나 이미지에 회전이나 확대 등 다양한 기하학적 모양을 부여할 수 있음. 또한 마우스를 올릴 때 순간적으로 변환을 일으키는 것 또한 가능
변환에서 사용하는 회전 각도의 단위는 deg이면 시계방향으로 회전함.

* ## transform property
CSS3에서 제공하는 변환 함수를 transform property에 적용하면 쉽게 변환 가능
```html
div{
    transform: rotate(20deg);
}
```
Reference:  https://developer.mozilla.org/en-US/docs/Web/CSS/transform

* ## 다중 변환
여러 변환을 동시에 하려면 transform property에 변환 함수들을 나열하면 된다.
```html
div{
    transform: rotate(20deg) scale(3, 1);
}
```
