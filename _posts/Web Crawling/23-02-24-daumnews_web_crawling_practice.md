---
layout: single
title: "Daum news Web Crawling"
categories: TIL
---
```python
import requests
url = 'https://news.daum.net/'
agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
response = requests.get(url = url, headers = {"User-Agent":agent})
```


```python
print(type(response))
```

    <class 'requests.models.Response'>
    


```python
response.status_code
```




    200




```python
res_text = response.text
res_content = response.content
print(res_text[:200])
print("\n")
print(res_content[:200])
```

    
    <!DOCTYPE html>
    
    
    
    <html lang="ko" class="os_linux chrome pc version_99_0_4844_74 ">
    <head>
    <meta charset="utf-8">
    <meta name="referrer" content="always" />
    
    <meta property="og:author" content="Daum 
    
    
    b'\n<!DOCTYPE html>\n\n\n\n<html lang="ko" class="os_linux chrome pc version_99_0_4844_74 ">\n<head>\n<meta charset="utf-8">\n<meta name="referrer" content="always" />\n\n<meta property="og:author" content="Daum '
    


```python
from bs4 import BeautifulSoup as BS
```


```python
parsed_res_text = BS(res_text)
print(type(parsed_res_text))
```

    <class 'bs4.BeautifulSoup'>
    


```python
print(parsed_res_text.find("ul"))
```

    <ul class="doc-relate" data-tiara-layer="GNB service">
    <li><a class="link_services" data-tiara-layer="enter" href="https://entertain.daum.net">연예</a></li>
    <li><a class="link_services" data-tiara-layer="sports" href="https://sports.daum.net">스포츠</a></li>
    </ul>
    


```python
print(parsed_res_text.find_all("ul")[3])
```

    <ul class="list_todayseries">
    <li>
    <div class="item_todayseries">
    <div class="subtxt_thumb">
    <a class="info_cp" data-tiara-custom="contentUniqueKey=hamny-20221201200904154&amp;clusterId=5139529,5079747,5150091,821758,5151790,5599922,5121256&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,사회,정면승부,[승인취소] 연예스포츠 이슈,[품질검수] 뉴스 필터링,[승인] 라디오 원본&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200904154" data-tiara-layer="series" data-tiara-ordnum="1" data-tiara-type="harmony" href="/series/821758"><span class="screen_out">출처
                                    </span>정면승부</a>
    </div>
    <a class="wrap_thumb" data-tiara-custom="contentUniqueKey=hamny-20221201200904154&amp;clusterId=5139529,5079747,5150091,821758,5151790,5599922,5121256&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,사회,정면승부,[승인취소] 연예스포츠 이슈,[품질검수] 뉴스 필터링,[승인] 라디오 원본&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200904154" data-tiara-layer="article_thumb" data-tiara-ordnum="1" data-tiara-type="harmony" href="https://v.daum.net/v/20221201200904154">
    <img alt='[정면승부] "연예계 불공정 계약 반복되는 이유, 소속사가 절대적 우위에 있기 때문"' class="thumb_g" src="https://img1.daumcdn.net/thumb/S112x70ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202212%2F01%2FYTN%2F20221201200904730qjzl.jpg&amp;scode=media"/>
    </a>
    <div class="cont_thumb">
    <strong class="tit_g">
    <a class="link_txt" data-tiara-custom="contentUniqueKey=hamny-20221201200904154&amp;clusterId=5139529,5079747,5150091,821758,5151790,5599922,5121256&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,사회,정면승부,[승인취소] 연예스포츠 이슈,[품질검수] 뉴스 필터링,[승인] 라디오 원본&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200904154" data-tiara-layer="article" data-tiara-ordnum="1" data-tiara-type="harmony" href="https://v.daum.net/v/20221201200904154">
                                        [정면승부] "연예계 불공정 계약 반복되는 이유, 소속사가 절대적 우위에 있기 때문"
                                    </a>
    </strong>
    <span class="info_thumb">
    <span class="txt_info">YTN</span>
    </span>
    </div>
    </div>
    </li>
    <li>
    <div class="item_todayseries">
    <div class="subtxt_thumb">
    <a class="info_cp" data-tiara-custom="contentUniqueKey=hamny-20221201200639117&amp;clusterId=5150091,5139529,1691288,410,5111131,1691294,5653560,5599922&amp;clusterTitle=사회,[랭크업] 유레이더 1 OR 2 추가점수,강원도,KBS,여기는 강릉,강원도 속초시,여기는 강릉,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200639117" data-tiara-layer="series" data-tiara-ordnum="2" data-tiara-type="harmony" href="/series/5111131"><span class="screen_out">출처
                                    </span>여기는 강릉</a>
    </div>
    <a class="wrap_thumb" data-tiara-custom="contentUniqueKey=hamny-20221201200639117&amp;clusterId=5150091,5139529,1691288,410,5111131,1691294,5653560,5599922&amp;clusterTitle=사회,[랭크업] 유레이더 1 OR 2 추가점수,강원도,KBS,여기는 강릉,강원도 속초시,여기는 강릉,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200639117" data-tiara-layer="article_thumb" data-tiara-ordnum="2" data-tiara-type="harmony" href="https://v.daum.net/v/20221201200639117">
    <img alt='[여기는 강릉] 분수 공사 추진에 물고기 떼죽음…"행정 편의주의"' class="thumb_g" src="https://img1.daumcdn.net/thumb/S112x70ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202212%2F01%2Fkbs%2F20221201200641900rvxr.jpg&amp;scode=media"/>
    </a>
    <div class="cont_thumb">
    <strong class="tit_g">
    <a class="link_txt" data-tiara-custom="contentUniqueKey=hamny-20221201200639117&amp;clusterId=5150091,5139529,1691288,410,5111131,1691294,5653560,5599922&amp;clusterTitle=사회,[랭크업] 유레이더 1 OR 2 추가점수,강원도,KBS,여기는 강릉,강원도 속초시,여기는 강릉,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200639117" data-tiara-layer="article" data-tiara-ordnum="2" data-tiara-type="harmony" href="https://v.daum.net/v/20221201200639117">
                                        [여기는 강릉] 분수 공사 추진에 물고기 떼죽음…"행정 편의주의"
                                    </a>
    </strong>
    <span class="info_thumb">
    <span class="txt_info">KBS</span>
    </span>
    </div>
    </div>
    </li>
    <li>
    <div class="item_todayseries">
    <div class="subtxt_thumb">
    <a class="info_cp" data-tiara-custom="contentUniqueKey=hamny-20221201200503089&amp;clusterId=5150091,5139529,5637001,5648478,5599922&amp;clusterTitle=사회,[랭크업] 유레이더 1 OR 2 추가점수,키우다,육퇴한 밤,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200503089" data-tiara-layer="series" data-tiara-ordnum="3" data-tiara-type="harmony" href="/series/5637001"><span class="screen_out">출처
                                    </span>키우다</a>
    </div>
    <a class="wrap_thumb" data-tiara-custom="contentUniqueKey=hamny-20221201200503089&amp;clusterId=5150091,5139529,5637001,5648478,5599922&amp;clusterTitle=사회,[랭크업] 유레이더 1 OR 2 추가점수,키우다,육퇴한 밤,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200503089" data-tiara-layer="article_thumb" data-tiara-ordnum="3" data-tiara-type="harmony" href="https://v.daum.net/v/20221201200503089">
    <img alt="수능 영어 비법이요? 독해 또 독해입니다. [육퇴한 밤]" class="thumb_g" src="https://img1.daumcdn.net/thumb/S112x70ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202212%2F01%2Fhani%2F20221201200509320zovl.jpg&amp;scode=media"/>
    </a>
    <div class="cont_thumb">
    <strong class="tit_g">
    <a class="link_txt" data-tiara-custom="contentUniqueKey=hamny-20221201200503089&amp;clusterId=5150091,5139529,5637001,5648478,5599922&amp;clusterTitle=사회,[랭크업] 유레이더 1 OR 2 추가점수,키우다,육퇴한 밤,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200503089" data-tiara-layer="article" data-tiara-ordnum="3" data-tiara-type="harmony" href="https://v.daum.net/v/20221201200503089">
                                        수능 영어 비법이요? 독해 또 독해입니다. [육퇴한 밤]
                                    </a>
    </strong>
    <span class="info_thumb">
    <span class="txt_info">한겨레</span>
    </span>
    </div>
    </div>
    </li>
    <li>
    <div class="item_todayseries">
    <div class="subtxt_thumb">
    <a class="info_cp" data-tiara-custom="contentUniqueKey=hamny-20221201200259065&amp;clusterId=5139529,5079747,5575289,5150099,5599922&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,데이터링,IT,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200259065" data-tiara-layer="series" data-tiara-ordnum="4" data-tiara-type="harmony" href="/series/5575289"><span class="screen_out">출처
                                    </span>데이터링</a>
    </div>
    <a class="wrap_thumb" data-tiara-custom="contentUniqueKey=hamny-20221201200259065&amp;clusterId=5139529,5079747,5575289,5150099,5599922&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,데이터링,IT,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200259065" data-tiara-layer="article_thumb" data-tiara-ordnum="4" data-tiara-type="harmony" href="https://v.daum.net/v/20221201200259065">
    <img alt="'전송요구권' 대상 개인정보는?…&quot;상시 운영 협의체서 설정해야&quot; [데이터링]" class="thumb_g" src="https://img1.daumcdn.net/thumb/S112x70ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202212%2F01%2Finews24%2F20221201200301828cbol.jpg&amp;scode=media"/>
    </a>
    <div class="cont_thumb">
    <strong class="tit_g">
    <a class="link_txt" data-tiara-custom="contentUniqueKey=hamny-20221201200259065&amp;clusterId=5139529,5079747,5575289,5150099,5599922&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,데이터링,IT,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200259065" data-tiara-layer="article" data-tiara-ordnum="4" data-tiara-type="harmony" href="https://v.daum.net/v/20221201200259065">
                                        '전송요구권' 대상 개인정보는?…"상시 운영 협의체서 설정해야" [데이터링]
                                    </a>
    </strong>
    <span class="info_thumb">
    <span class="txt_info">아이뉴스24</span>
    </span>
    </div>
    </div>
    </li>
    <li>
    <div class="item_todayseries">
    <div class="subtxt_thumb">
    <a class="info_cp" data-tiara-custom="contentUniqueKey=hamny-20221201200016015&amp;clusterId=5150091,5085535,5139529,5079747,5557203,5203406,5599922&amp;clusterTitle=사회,[사용] 2500자 이상 (기획기사 참조),[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,WEEKLY BIZ,WEEKLY BIZ,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200016015" data-tiara-layer="series" data-tiara-ordnum="5" data-tiara-type="harmony" href="/series/5203406"><span class="screen_out">출처
                                    </span>WEEKLY BIZ</a>
    </div>
    <a class="wrap_thumb" data-tiara-custom="contentUniqueKey=hamny-20221201200016015&amp;clusterId=5150091,5085535,5139529,5079747,5557203,5203406,5599922&amp;clusterTitle=사회,[사용] 2500자 이상 (기획기사 참조),[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,WEEKLY BIZ,WEEKLY BIZ,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200016015" data-tiara-layer="article_thumb" data-tiara-ordnum="5" data-tiara-type="harmony" href="https://v.daum.net/v/20221201200016015">
    <img alt="‘현대판 방주’ 해상부유 도시… 온난화로 바다 잠길 2억명 피난처될까" class="thumb_g" src="https://img1.daumcdn.net/thumb/S112x70ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202212%2F01%2Fchosun%2F20221201200020568yjyb.jpg&amp;scode=media"/>
    </a>
    <div class="cont_thumb">
    <strong class="tit_g">
    <a class="link_txt" data-tiara-custom="contentUniqueKey=hamny-20221201200016015&amp;clusterId=5150091,5085535,5139529,5079747,5557203,5203406,5599922&amp;clusterTitle=사회,[사용] 2500자 이상 (기획기사 참조),[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,WEEKLY BIZ,WEEKLY BIZ,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201200016015" data-tiara-layer="article" data-tiara-ordnum="5" data-tiara-type="harmony" href="https://v.daum.net/v/20221201200016015">
                                        ‘현대판 방주’ 해상부유 도시… 온난화로 바다 잠길 2억명 피난처될까
                                    </a>
    </strong>
    <span class="info_thumb">
    <span class="txt_info">조선일보</span>
    </span>
    </div>
    </div>
    </li>
    <li>
    <div class="item_todayseries">
    <div class="subtxt_thumb">
    <a class="info_cp" data-tiara-custom="contentUniqueKey=hamny-20221201195804974&amp;clusterId=5139529,5079747,191589,410,5647072,173893,5030619,5150092,168706,5599922,5121256&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,윤석열,KBS,주진우 라이브,주진우,주진우 라이브,정치,윤여준,[품질검수] 뉴스 필터링,[승인] 라디오 원본&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201195804974" data-tiara-layer="series" data-tiara-ordnum="6" data-tiara-type="harmony" href="/series/5030619"><span class="screen_out">출처
                                    </span>주진우 라이브</a>
    </div>
    <a class="wrap_thumb" data-tiara-custom="contentUniqueKey=hamny-20221201195804974&amp;clusterId=5139529,5079747,191589,410,5647072,173893,5030619,5150092,168706,5599922,5121256&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,윤석열,KBS,주진우 라이브,주진우,주진우 라이브,정치,윤여준,[품질검수] 뉴스 필터링,[승인] 라디오 원본&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201195804974" data-tiara-layer="article_thumb" data-tiara-ordnum="6" data-tiara-type="harmony" href="https://v.daum.net/v/20221201195804974">
    <img alt="[주진우 라이브] 윤여준 “尹, 약한 말이 무거운 짐 져…해 바뀌면 지금 내각으로 국정 끌기 쉽지 않을 것”" class="thumb_g" src="https://img1.daumcdn.net/thumb/S112x70ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202212%2F01%2Fkbs%2F20221201195807284ywzm.jpg&amp;scode=media"/>
    </a>
    <div class="cont_thumb">
    <strong class="tit_g">
    <a class="link_txt" data-tiara-custom="contentUniqueKey=hamny-20221201195804974&amp;clusterId=5139529,5079747,191589,410,5647072,173893,5030619,5150092,168706,5599922,5121256&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,[랭크업] 1800자 이상 OR 유레이더2 이상,윤석열,KBS,주진우 라이브,주진우,주진우 라이브,정치,윤여준,[품질검수] 뉴스 필터링,[승인] 라디오 원본&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201195804974" data-tiara-layer="article" data-tiara-ordnum="6" data-tiara-type="harmony" href="https://v.daum.net/v/20221201195804974">
                                        [주진우 라이브] 윤여준 “尹, 약한 말이 무거운 짐 져…해 바뀌면 지금 내각으로 국정 끌기 쉽지 않을 것”
                                    </a>
    </strong>
    <span class="info_thumb">
    <span class="txt_info">KBS</span>
    </span>
    </div>
    </div>
    </li>
    <li>
    <div class="item_todayseries">
    <div class="subtxt_thumb">
    <a class="info_cp" data-tiara-custom="contentUniqueKey=hamny-20221201195808979&amp;clusterId=5139529,5150091,1453,601024,421,419,5186669,5186687,541497,5122368,5599922&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,사회,팩트체크,JTBC 팩트체크,JTBC 뉴스룸,JTBC,전체,JTBC,JTBC 팩트체크,[승인] 팩트체크,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201195808979" data-tiara-layer="series" data-tiara-ordnum="7" data-tiara-type="harmony" href="/series/1453"><span class="screen_out">출처
                                    </span>팩트체크</a>
    </div>
    <a class="wrap_thumb" data-tiara-custom="contentUniqueKey=hamny-20221201195808979&amp;clusterId=5139529,5150091,1453,601024,421,419,5186669,5186687,541497,5122368,5599922&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,사회,팩트체크,JTBC 팩트체크,JTBC 뉴스룸,JTBC,전체,JTBC,JTBC 팩트체크,[승인] 팩트체크,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201195808979" data-tiara-layer="article_thumb" data-tiara-ordnum="7" data-tiara-type="harmony" href="https://v.daum.net/v/20221201195808979">
    <img alt="[팩트체크] 파업 쟁점 '안전운임제' 시행하는 나라 없다?" class="thumb_g" src="https://img1.daumcdn.net/thumb/S112x70ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202212%2F01%2FJTBC%2F20221201195809317isvp.jpg&amp;scode=media"/>
    </a>
    <div class="cont_thumb">
    <strong class="tit_g">
    <a class="link_txt" data-tiara-custom="contentUniqueKey=hamny-20221201195808979&amp;clusterId=5139529,5150091,1453,601024,421,419,5186669,5186687,541497,5122368,5599922&amp;clusterTitle=[랭크업] 유레이더 1 OR 2 추가점수,사회,팩트체크,JTBC 팩트체크,JTBC 뉴스룸,JTBC,전체,JTBC,JTBC 팩트체크,[승인] 팩트체크,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201195808979" data-tiara-layer="article" data-tiara-ordnum="7" data-tiara-type="harmony" href="https://v.daum.net/v/20221201195808979">
                                        [팩트체크] 파업 쟁점 '안전운임제' 시행하는 나라 없다?
                                    </a>
    </strong>
    <span class="info_thumb">
    <span class="txt_info">JTBC</span>
    </span>
    </div>
    </div>
    </li>
    <li>
    <div class="item_todayseries">
    <div class="subtxt_thumb">
    <a class="info_cp" data-tiara-custom="contentUniqueKey=hamny-20221201195644955&amp;clusterId=5150091,5139529,477,478,5039481,5599922&amp;clusterTitle=사회,[랭크업] 유레이더 1 OR 2 추가점수,채널A,채널A 뉴스A,여인선이 간다,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201195644955" data-tiara-layer="series" data-tiara-ordnum="8" data-tiara-type="harmony" href="/series/5039481"><span class="screen_out">출처
                                    </span>여인선이 간다</a>
    </div>
    <a class="wrap_thumb" data-tiara-custom="contentUniqueKey=hamny-20221201195644955&amp;clusterId=5150091,5139529,477,478,5039481,5599922&amp;clusterTitle=사회,[랭크업] 유레이더 1 OR 2 추가점수,채널A,채널A 뉴스A,여인선이 간다,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201195644955" data-tiara-layer="article_thumb" data-tiara-ordnum="8" data-tiara-type="harmony" href="https://v.daum.net/v/20221201195644955">
    <img alt="[여인선이 간다]결혼해야만 축하? 비혼 축의금 시대" class="thumb_g" src="https://img1.daumcdn.net/thumb/S112x70ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202212%2F01%2FChannela%2F20221201195646146xvcu.jpg&amp;scode=media"/>
    </a>
    <div class="cont_thumb">
    <strong class="tit_g">
    <a class="link_txt" data-tiara-custom="contentUniqueKey=hamny-20221201195644955&amp;clusterId=5150091,5139529,477,478,5039481,5599922&amp;clusterTitle=사회,[랭크업] 유레이더 1 OR 2 추가점수,채널A,채널A 뉴스A,여인선이 간다,[품질검수] 뉴스 필터링&amp;keywordType=NONE,NONE,NONE,NONE,NONE,NONE" data-tiara-id="20221201195644955" data-tiara-layer="article" data-tiara-ordnum="8" data-tiara-type="harmony" href="https://v.daum.net/v/20221201195644955">
                                        [여인선이 간다]결혼해야만 축하? 비혼 축의금 시대
                                    </a>
    </strong>
    <span class="info_thumb">
    <span class="txt_info">채널A</span>
    </span>
    </div>
    </div>
    </li>
    </ul>
    


```python
print(parsed_res_text.find("span", attrs = {"class":"info_news"}))
```

    None
    


```python
print(parsed_res_text.find("span"))
```

    <span class="ir_wa">뉴스</span>
    


```python
print(parsed_res_text.find_all("span"))
```

    [<span class="ir_wa">뉴스</span>, <span class="txt_gnb">홈</span>, <span class="txt_gnb">사회</span>, <span class="txt_gnb">정치</span>, <span class="txt_gnb">경제</span>, <span class="txt_gnb">국제</span>, <span class="txt_gnb">문화</span>, <span class="txt_gnb">IT</span>, <span class="txt_gnb">연재</span>, <span class="txt_gnb">포토</span>, <span class="txt_gnb">팩트체크</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="KBS" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_kbs.gif"/>
    </span>
    <span class="txt_category">사회</span>
    </span>, <span class="logo_cp">
    <img alt="KBS" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_kbs.gif"/>
    </span>, <span class="txt_category">사회</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="KBS" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_kbs.gif"/>
    </span>
    <span class="txt_category">사회</span>
    </span>, <span class="logo_cp">
    <img alt="KBS" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_kbs.gif"/>
    </span>, <span class="txt_category">사회</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="아이뉴스24" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_inews24.gif"/>
    </span>
    <span class="txt_category">정치</span>
    </span>, <span class="logo_cp">
    <img alt="아이뉴스24" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_inews24.gif"/>
    </span>, <span class="txt_category">정치</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="아이뉴스24" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_inews24.gif"/>
    </span>
    <span class="txt_category">정치</span>
    </span>, <span class="logo_cp">
    <img alt="아이뉴스24" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_inews24.gif"/>
    </span>, <span class="txt_category">정치</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="SBS" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_sbsi.gif"/>
    </span>
    <span class="txt_category">경제</span>
    </span>, <span class="logo_cp">
    <img alt="SBS" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_sbsi.gif"/>
    </span>, <span class="txt_category">경제</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="오마이뉴스" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_ohmynews.gif"/>
    </span>
    <span class="txt_category">정치</span>
    </span>, <span class="logo_cp">
    <img alt="오마이뉴스" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_ohmynews.gif"/>
    </span>, <span class="txt_category">정치</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="MBC" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_imbc.gif"/>
    </span>
    <span class="txt_category">사회</span>
    </span>, <span class="logo_cp">
    <img alt="MBC" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_imbc.gif"/>
    </span>, <span class="txt_category">사회</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="MBC" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_imbc.gif"/>
    </span>
    <span class="txt_category">경제</span>
    </span>, <span class="logo_cp">
    <img alt="MBC" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_imbc.gif"/>
    </span>, <span class="txt_category">경제</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="디지털타임스" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_dt.gif"/>
    </span>
    <span class="txt_category">정치</span>
    </span>, <span class="logo_cp">
    <img alt="디지털타임스" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_dt.gif"/>
    </span>, <span class="txt_category">정치</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="뉴스1" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_news1.gif"/>
    </span>
    <span class="txt_category">경제</span>
    </span>, <span class="logo_cp">
    <img alt="뉴스1" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_news1.gif"/>
    </span>, <span class="txt_category">경제</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="한국경제" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_ked.gif"/>
    </span>
    <span class="txt_category">경제</span>
    </span>, <span class="logo_cp">
    <img alt="한국경제" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_ked.gif"/>
    </span>, <span class="txt_category">경제</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="한국경제" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_ked.gif"/>
    </span>
    <span class="txt_category">사회</span>
    </span>, <span class="logo_cp">
    <img alt="한국경제" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_ked.gif"/>
    </span>, <span class="txt_category">사회</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="연합뉴스" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_yonhap.gif"/>
    </span>
    <span class="txt_category">국제</span>
    </span>, <span class="logo_cp">
    <img alt="연합뉴스" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_yonhap.gif"/>
    </span>, <span class="txt_category">국제</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="MBN" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_mbn2019.gif"/>
    </span>
    <span class="txt_category">사회</span>
    </span>, <span class="logo_cp">
    <img alt="MBN" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_mbn2019.gif"/>
    </span>, <span class="txt_category">사회</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="MBN" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_mbn2019.gif"/>
    </span>
    <span class="txt_category">정치</span>
    </span>, <span class="logo_cp">
    <img alt="MBN" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_mbn2019.gif"/>
    </span>, <span class="txt_category">정치</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="SBS Biz" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_sbsbiz.gif"/>
    </span>
    <span class="txt_category">문화</span>
    </span>, <span class="logo_cp">
    <img alt="SBS Biz" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_sbsbiz.gif"/>
    </span>, <span class="txt_category">문화</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="SBS Biz" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_sbsbiz.gif"/>
    </span>
    <span class="txt_category">경제</span>
    </span>, <span class="logo_cp">
    <img alt="SBS Biz" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_sbsbiz.gif"/>
    </span>, <span class="txt_category">경제</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="MBN" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_mbn2019.gif"/>
    </span>
    <span class="txt_category">사회</span>
    </span>, <span class="logo_cp">
    <img alt="MBN" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_mbn2019.gif"/>
    </span>, <span class="txt_category">사회</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="코메디닷컴" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_KorMedi.gif"/>
    </span>
    <span class="txt_category">문화</span>
    </span>, <span class="logo_cp">
    <img alt="코메디닷컴" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_KorMedi.gif"/>
    </span>, <span class="txt_category">문화</span>, <span class="info_thumb">
    <span class="logo_cp">
    <img alt="문화일보" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_munhwa.gif"/>
    </span>
    <span class="txt_category">정치</span>
    </span>, <span class="logo_cp">
    <img alt="문화일보" class="thumb_g" onerror="this.style.display='none';" src="https://t1.daumcdn.net/media/news/news2016/cp/cp_munhwa.gif"/>
    </span>, <span class="txt_category">정치</span>, <span class="screen_out">출처
                                    </span>, <span class="info_thumb">
    <span class="txt_info">YTN</span>
    </span>, <span class="txt_info">YTN</span>, <span class="screen_out">출처
                                    </span>, <span class="info_thumb">
    <span class="txt_info">KBS</span>
    </span>, <span class="txt_info">KBS</span>, <span class="screen_out">출처
                                    </span>, <span class="info_thumb">
    <span class="txt_info">한겨레</span>
    </span>, <span class="txt_info">한겨레</span>, <span class="screen_out">출처
                                    </span>, <span class="info_thumb">
    <span class="txt_info">아이뉴스24</span>
    </span>, <span class="txt_info">아이뉴스24</span>, <span class="screen_out">출처
                                    </span>, <span class="info_thumb">
    <span class="txt_info">조선일보</span>
    </span>, <span class="txt_info">조선일보</span>, <span class="screen_out">출처
                                    </span>, <span class="info_thumb">
    <span class="txt_info">KBS</span>
    </span>, <span class="txt_info">KBS</span>, <span class="screen_out">출처
                                    </span>, <span class="info_thumb">
    <span class="txt_info">JTBC</span>
    </span>, <span class="txt_info">JTBC</span>, <span class="screen_out">출처
                                    </span>, <span class="info_thumb">
    <span class="txt_info">채널A</span>
    </span>, <span class="txt_info">채널A</span>, <span class="rate_stock rate_up">
    <!-- 상승 rate_up, 하락 rate_down 클래스 추가 -->
    <span class="num_stock">2,479.84</span>
    <span class="num_change">
    <span class="num_prev">
    <!-- 상승 ico_up, 하락 ico_down, 보합 ico_same 클래스 적용 -->
    <span class="screen_out">전일비</span><span class="ico_up">상승</span>
                                                 7.31
                                        </span>
    <span class="num_rate">
    <span class="screen_out">등락률</span>(0.30%)
                                        </span>
    </span>
    </span>, <span class="num_stock">2,479.84</span>, <span class="num_change">
    <span class="num_prev">
    <!-- 상승 ico_up, 하락 ico_down, 보합 ico_same 클래스 적용 -->
    <span class="screen_out">전일비</span><span class="ico_up">상승</span>
                                                 7.31
                                        </span>
    <span class="num_rate">
    <span class="screen_out">등락률</span>(0.30%)
                                        </span>
    </span>, <span class="num_prev">
    <!-- 상승 ico_up, 하락 ico_down, 보합 ico_same 클래스 적용 -->
    <span class="screen_out">전일비</span><span class="ico_up">상승</span>
                                                 7.31
                                        </span>, <span class="screen_out">전일비</span>, <span class="ico_up">상승</span>, <span class="num_rate">
    <span class="screen_out">등락률</span>(0.30%)
                                        </span>, <span class="screen_out">등락률</span>, <span class="rate_stock rate_up">
    <span class="num_stock">740.60</span>
    <span class="num_change">
    <span class="num_prev">
    <span class="screen_out">전일비</span><span class="ico_up">하락</span>
                                                 11.06
                                        </span>
    <span class="num_rate">
    <span class="screen_out">등락률</span>(1.52%)
                                        </span>
    </span>
    </span>, <span class="num_stock">740.60</span>, <span class="num_change">
    <span class="num_prev">
    <span class="screen_out">전일비</span><span class="ico_up">하락</span>
                                                 11.06
                                        </span>
    <span class="num_rate">
    <span class="screen_out">등락률</span>(1.52%)
                                        </span>
    </span>, <span class="num_prev">
    <span class="screen_out">전일비</span><span class="ico_up">하락</span>
                                                 11.06
                                        </span>, <span class="screen_out">전일비</span>, <span class="ico_up">하락</span>, <span class="num_rate">
    <span class="screen_out">등락률</span>(1.52%)
                                        </span>, <span class="screen_out">등락률</span>, <span class="time_stock">
    <span class="screen_out">기준시간</span>
                    장마감
                </span>, <span class="screen_out">기준시간</span>, <span class="ico_news ico_photo">포토갤러리</span>, <span class="screen_out">출처 </span>, <span class="ico_news ico_photo">포토갤러리</span>, <span class="screen_out">출처 </span>, <span class="ico_news ico_photo">포토갤러리</span>, <span class="screen_out">출처 </span>, <span class="ico_news ico_photo">포토갤러리</span>, <span class="screen_out">출처 </span>, <span class="ico_news ico_arr"> 바로가기</span>, <span class="ico_news ico_arr"> 바로가기</span>, <span class="ico_news ico_arr"> 바로가기</span>, <span class="ico_news">바로가기 링크 더보기/접기</span>, <span class="txt_dot"> ・ </span>, <span class="txt_dot"> ・ </span>, <span class="txt_dot"> ・ </span>, <span class="txt_dot"> ・ </span>, <span class="txt_dot"> ・ </span>, <span class="txt_dot"> ・ </span>, <span class="txt_dot"> ・ </span>, <span class="txt_dot"> ・ </span>, <span class="txt_dot"> ・ </span>, <span class="txt_dot"> ・ </span>, <span class="link_info">기사배열책임자 : 황유지</span>, <span class="txt_dot"> ・ </span>, <span class="link_info">청소년보호책임자 : 정현주</span>]
    


```python

```
