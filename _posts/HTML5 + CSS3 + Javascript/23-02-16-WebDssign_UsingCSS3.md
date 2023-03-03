---
layout: single
title: "WebDssign_UsingCSS3"
categories: TIL
---
# CSS3로 웹 꾸미기
## 1. CSS3
* HTML문서에 색이나 모양, 출력 위치 등 외관을 꾸미는 언어
* CSS3로 작성된 코드를 스타일 시트라고 부른다.

### 맛보기 예제
1. HTML태그로만 작성된 예제
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h3>CSS 스타일 맛보기</h3>
        <hr>
        <p>나는 <span>웹 프로그래밍</span>을 좋아합니다.</p>
    </body>
</html>
```

2. CSS3 스타일 시트로 꾸민 웹 페이지
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <style>
            body{background-color : mistyrose;}
            h3{color : purple;}
            hr{border : 5px solid yellowgreen;}
            span{color : blue; font-size : 20px;}
        </style>
    </head>
    <body>
        <h3>CSS 스타일 맛보기</h3>
        <hr>
        <p>나는 <span>웹 프로그래밍</span>을 좋아합니다.</p>
    </body>
</html>
```

<hr>

## 2. CSS3 스타일 시트 만들기
* CSS3 스타일 시트를 작성하는 방법에는 다음 3가지가 있다.
    * <style\></style\>태그에 스타일 시트 작성
    * style 속성에 스타일 시트 작성
    * 스타일 시트를 별도 파일로 작성하고, <link\> 태그나 @import로 불러 사용
### <style\>태그로 스타일 시트 만들기
```html
<head>
    <style>
        body{background-color:mistyrose;}
        h3{color : purple;}
    </style>
    <style>
        hr{border : 5px solid yellowgreen;}
        span{color : blue; font-size : 20px;}
    </style>
</head>
```

이 방법은 다음과 같은 특징이 있음
* <style\> 태그는 반드시 <head\>태그 내에서만 작성 가능
* <style\> 태그는 여러 번 작성 가능하며 스타일 시트들이 합쳐 적용됨
* <style\> 태그에 작성된 스타일 시트는 웹 페이지 전체에 적용

### <style\> 태그로 스타일 시트 만들기
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <style>
            body{background-color: linen; color: blueviolet; margin-left: 30px; margin-right: 30px;}
            h3{text-align: center; color: darkred;}
        </style>
    </head>
    <body>
        <h3>소연재</h3>
        <hr>
        <p>저는 체조 선수 소연재입니다. 음악을 들으면서 책읽기를 좋아합니다. 김치 찌개와 막국수를 무척 좋아합니다.</p>
    </body>
</html>
```

### style 속성에 스타일 시트 만들기
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <style>
            p{color: red; font-size: 15px;}
        </style>
    </head>
    <body>
        <h3>손흥민</h3>
        <hr>
        <p>오페라를 좋아하고</p>
        <p>엘비스 프레슬리를 좋아하고</p>
        <p style="color:blue">김치부침개를 좋아하고</p>
        <p style="color:magenta; font-size:30px">축구를 좋아합니다.</p>
    </body>
</html>
```

<hr>

## 3. 외부 스타일 시트 파일 불러오기
불러오는 방법에는 2가지가 있다.
1. <link\> 태그 이용
2. @import 이용

### <link\> 태그 이용
```html
<head>
    <link href= "mystyle.css" type="text/css" rel="stylesheet">
</head>
```

### @import 이용
```html
<style>
    @import url(mystyle.css);
</style>
```

###  부모 스타일 상속
<em\>태그가 <p\>태그의 자식으로서 상식받는 예제를 보자.
```html
<p style="color: green">자식 태그는 부모의 스타일을
    <em style="font-size: 25px">상속</em>받는다.</p>
```

<hr>

## 4. 셀렉터
### 태그 이름 셀렉터
태그 이름이 셀렉터로 사용되는 유형으로, 셀렉터와 같은 이름의 모든 태그에 CSS3 시타일 시트를 적용
```html
h3, li {color:brown;}
```

### class 셀렉터
셀렉터 이름 앞에 점을 붙인 경우, 이 셀렉터는 HTML 태그의 class 속성으로만 지정할 수 있다.
```html
.warning{color: red;}
<div class="warning"></div>
```

### id셀렉터
셀렉터 이름 앞에 '#'을 붙인 경우, 이 셀렉터는 HTML 태그의 id 속성으로만 지정할 수 있다.
```html
#list {background: mistyrose;}
<ul id = 'list'>
```

### 전체 셀렉터
와일드카드 문자(*)를 사용하여 웹 페이지의 모든 HTML 태그에 적용할 스타일을 만드는 셀렉터
```html
* {color: green;}
```

### 속성 셀렉터
HTML 태그의 특정 속성(attribute)에 대해 값이 일치하는 태그에만 스타일을 적용하는 셀렉터
```html
input[type=text] {color: red;}
```

### 가상 클래스 셀렉터
어떤 상황이 발생하였을 때만 적용하도록 CSS3 표준에 만들어진 셀렉터
```html
a:visited {color: green;} /* 방문한 후부터 <a>의 링크  텍스트 색을 green으로 출력*/
li:hover {background: yellowgreen;} /*<li> 태그 위에 마우스가 올라오면,  yellowgreen을 배경색으로 출력. 마우스가 내려가면 원래대로 복귀*/
```

<hr>

# Reference
* 명품 HTML5 + CSS + Javascript 웹 프로그래밍 개정판(황기태, (주)생능출판사)
