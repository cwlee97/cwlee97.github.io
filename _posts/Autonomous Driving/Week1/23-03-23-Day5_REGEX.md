---
layout: single
title: REGEX
categories: Autonomous_Driving_course
---

# 정규 표현식의 종류
1. POSIX REGEX - UNIX 계열 표준 정규표현식
    * BRE(Basic RE) - grep이 작동되는 기본값
    * ERE(Extended RE) - egrep의 기본값, 좀 더 많은 표현식과 편의성 제공
2. PCRE(Perl Compatible Regular Expression) - Perl 정규표현식 호환으로 확장된 기능을 갖고 있다.
    * Perl에서 제공되던 REGEX의 기능이 좋아 만들어짐
    * POSIX REGEX에 비해 성능이 좋음
    * 현재는 PCRE2 버전을 사용

# grep : matcher
* -G
    * BRE를 사용하여 작동(default)
* -E
    * ERE를 사용하여 작동
* -P
    * PCRE를 사용하여 작동

# grep의 주요 옵션
* --color, 매칭에 성공한 부분을 색칠로 알려줌
* -o, 매칭에 성공한 부분만 잘라서 보여줌
* -e PATTERN
* -v, --invert-match, 검색에 실패한 부분만 보여줌
* -c
* -q, --quite

# POSIX REGEX: meta char
1. POSIX 연산자
    <table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
    <tbody>
    <tr>
    <td style="width: 9.6124%;">연산자</td>
    <td style="width: 11.3565%;">영문</td>
    <td style="width: 79.031%;">설명</td>
    </tr>
    <tr>
    <td style="width: 9.6124%;">.</td>
    <td style="width: 11.3565%;">dot</td>
    <td style="width: 79.031%;">모든 문자와 일치</td>
    </tr>
    <tr>
    <td style="width: 9.6124%;">|</td>
    <td style="width: 11.3565%;">or</td>
    <td style="width: 79.031%;">대체 문자를 구분</td>
    </tr>
    <tr>
    <td style="width: 9.6124%;">\</td>
    <td style="width: 11.3565%;">backslash</td>
    <td style="width: 79.031%;">다음 문자를 일반 문자로 취급</td>
    </tr>
    </tbody>
    </table>


2. 앵커
    <div class="table_wrap"><table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
    <tbody>
    <tr>
    <td style="width: 11.3954%;">연산자</td>
    <td style="width: 13.0232%;">영문</td>
    <td style="width: 75.5813%;">설명</td>
    </tr>
    <tr>
    <td style="width: 11.3954%;">^</td>
    <td style="width: 13.0232%;">carrot</td>
    <td style="width: 75.5813%;">문자열의 시작</td>
    </tr>
    <tr>
    <td style="width: 11.3954%;">$</td>
    <td style="width: 13.0232%;">dollar</td>
    <td style="width: 75.5813%;">문자열의 끝</td>
    </tr>
    </tbody>
    </table></div>


3. 수량사
    <div class="table_wrap"><table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
    <tbody>
    <tr>
    <td style="width: 16.1628%;">연산자</td>
    <td style="width: 83.8372%;">설명</td>
    </tr>
    <tr>
    <td style="width: 16.1628%;">?</td>
    <td style="width: 83.8372%;">0회 혹은 1회 일치</td>
    </tr>
    <tr>
    <td style="width: 16.1628%;">*</td>
    <td style="width: 83.8372%;">0회 혹은 그 이상의 횟수로 일치</td>
    </tr>
    <tr>
    <td style="width: 16.1628%;">+</td>
    <td style="width: 83.8372%;">1회 또는 그 이상의 횟수로 일치</td>
    </tr>
    <tr>
    <td style="width: 16.1628%;">{m}</td>
    <td style="width: 83.8372%;">m회 일치</td>
    </tr>
    <tr>
    <td style="width: 16.1628%;">{m,}</td>
    <td style="width: 83.8372%;">최소 m회 일치</td>
    </tr>
    <tr>
    <td style="width: 16.1628%;">{,m}</td>
    <td style="width: 83.8372%;">최대 m회 일치</td>
    </tr>
    <tr>
    <td style="width: 16.1628%;">{m,n}</td>
    <td style="width: 83.8372%;">최소 m회, 최대 n회 일치</td>
    </tr>
    </tbody>
    </table></div>



4. 서브표현식
    <div class="table_wrap"><table style="border-collapse: collapse;" border="1" data-ke-align="alignLeft">
    <tbody>
    <tr style="height: 20px;">
    <td style="width: 19.6512%; height: 20px;">연산자</td>
    <td style="width: 80.3488%; height: 20px;">설명</td>
    </tr>
    <tr style="height: 20px;">
    <td style="width: 19.6512%; height: 20px;">(expr)</td>
    <td style="width: 80.3488%; height: 20px;">괄호 안의 표현식을 하나의 단위로 취급</td>
    </tr>
    </tbody>
    </table></div>

5. 역참조
    <div class="table_wrap"><table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
    <tbody>
    <tr>
    <td style="width: 11.2791%;">연산자</td>
    <td style="width: 88.7209%;">설명</td>
    </tr>
    <tr>
    <td style="width: 11.2791%;">\n</td>
    <td style="width: 88.7209%;">n번째 서브 표현식과 일치, n은 1~9까지의 정수</td>
    </tr>
    </tbody>
    </table></div>


6. 문자 리스트
    <div class="table_wrap"><table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
    <tbody>
    <tr>
    <td style="width: 13.5659%;">연산자</td>
    <td style="width: 32.9844%;">설명</td>
    <td style="width: 53.4496%;">동일</td>
    </tr>
    <tr>
    <td style="width: 13.5659%;">[:digit:]</td>
    <td style="width: 32.9844%;">숫자</td>
    <td style="width: 53.4496%;">[0-9]</td>
    </tr>
    <tr>
    <td style="width: 13.5659%;">[:lower:]</td>
    <td style="width: 32.9844%;">소문자</td>
    <td style="width: 53.4496%;">[a-z]</td>
    </tr>
    <tr>
    <td style="width: 13.5659%;">[:upper:]</td>
    <td style="width: 32.9844%;">대문자</td>
    <td style="width: 53.4496%;">[A-Z]</td>
    </tr>
    <tr>
    <td style="width: 13.5659%;">[:alpha:]</td>
    <td style="width: 32.9844%;">영문자</td>
    <td style="width: 53.4496%;">[a-zA-Z]</td>
    </tr>
    <tr>
    <td style="width: 13.5659%;">[:alnum:]</td>
    <td style="width: 32.9844%;">영문자와 숫자</td>
    <td style="width: 53.4496%;">[0-9a-zA-Z]</td>
    </tr>
    <tr>
    <td style="width: 13.5659%;">[:xdigit:]</td>
    <td style="width: 32.9844%;">16진수</td>
    <td style="width: 53.4496%;">[0-9a-fA-F]</td>
    </tr>
    <tr>
    <td style="width: 13.5659%;">[:punct:]</td>
    <td style="width: 32.9844%;">구두점 기호</td>
    <td style="width: 53.4496%;">[^[:alnum:][:cntrl:]]</td>
    </tr>
    <tr>
    <td style="width: 13.5659%;">[:blank:]</td>
    <td style="width: 32.9844%;">공백 문자</td>
    <td style="width: 53.4496%;">&nbsp;</td>
    </tr>
    <tr>
    <td style="width: 13.5659%;">[:space:]</td>
    <td style="width: 32.9844%;">공간문자 (스페이스,엔터,탭)</td>
    <td style="width: 53.4496%;">&nbsp;</td>
    </tr>
    </tbody>
    </table></div>


# Perl REGEX: meta char
<div class="table_wrap"><table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
<tbody>
<tr>
<td style="width: 13.4496%;">연산자</td>
<td style="width: 32.9845%;">설명</td>
<td style="width: 53.5658%;">동일</td>
</tr>
<tr>
<td style="width: 13.4496%;">\d</td>
<td style="width: 32.9845%;">숫자</td>
<td style="width: 53.5658%;">[[:digit:]]</td>
</tr>
<tr>
<td style="width: 13.4496%;">\D</td>
<td style="width: 32.9845%;">숫자가 아닌 모든 문자</td>
<td style="width: 53.5658%;">[^[:digit:]]</td>
</tr>
<tr>
<td style="width: 13.4496%;">\w</td>
<td style="width: 32.9845%;">숫자와 영문자(언더바 포함)</td>
<td style="width: 53.5658%;">[[:alnum:]_]</td>
</tr>
<tr>
<td style="width: 13.4496%;">\W</td>
<td style="width: 32.9845%;">숫자와 영문자가 아닌 모든 문자<br>(언더바 제외)</td>
<td style="width: 53.5658%;">[^[:alnum:]_]</td>
</tr>
<tr>
<td style="width: 13.4496%;">\s</td>
<td style="width: 32.9845%;">공백 문자</td>
<td style="width: 53.5658%;">[[:space:]]</td>
</tr>
<tr>
<td style="width: 13.4496%;">\S</td>
<td style="width: 32.9845%;">공백 문자가 아닌 모든 문자</td>
<td style="width: 53.5658%;">[^[:space:]]</td>
</tr>
</tbody>
</table></div>

<div class="table_wrap"><table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
<tbody>
<tr style="height: 20px;">
<td style="width: 8.13949%; height: 20px;">연산자</td>
<td style="width: 58.527%; height: 20px;">설명</td>
</tr>
<tr style="height: 20px;">
<td style="width: 8.13949%; height: 20px;">??</td>
<td style="width: 58.527%; height: 20px;">0회 또는 1회 일치</td>
</tr>
<tr style="height: 20px;">
<td style="width: 8.13949%; height: 20px;">*?</td>
<td style="width: 58.527%; height: 20px;">0회 또는 그 이상 일치</td>
</tr>
<tr style="height: 20px;">
<td style="width: 8.13949%; height: 20px;">+?</td>
<td style="width: 58.527%; height: 20px;">1회 또는 그 이상 일치</td>
</tr>
<tr style="height: 20px;">
<td style="width: 8.13949%; height: 20px;">{m}?</td>
<td style="width: 58.527%; height: 20px;">m회 일치</td>
</tr>
<tr style="height: 20px;">
<td style="width: 8.13949%; height: 20px;">{m,}?</td>
<td style="width: 58.527%; height: 20px;">최소 m회 일치&nbsp;</td>
</tr>
<tr style="height: 20px;">
<td style="width: 8.13949%; height: 20px;">{,m}?</td>
<td style="width: 58.527%; height: 20px;">최대 m회 일치</td>
</tr>
<tr style="height: 20px;">
<td style="width: 8.13949%; height: 20px;">{m,n}?</td>
<td style="width: 58.527%; height: 20px;">최소 m, 최대 n회 일치</td>
</tr>
</tbody>
</table></div>