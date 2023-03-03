---
layout: single
title: "Paxnet Web Crawling"
categories: TIL
---
```python
import requests
from bs4 import BeautifulSoup as BS
```


```python
url = "http://www.paxnet.co.kr/stock/report/report?menuCode=2222"
response = requests.get(url)
html = response.content
html = BS(html)
```


```python
div = html.find("div", attrs = {"class" : "board-type"})
li_list = div.find_all("li")
```


```python
print(li_list[0])
```

    <li class="board-list-th">
    <div>종목</div>
    <div>제목</div>
    <div class="right">적정가격</div>
    <div>투자의견</div>
    <div>제공출처</div>
    <div class="cent">작성일</div>
    </li>
    


```python
li_list[1]
```




    <li>
    <div><strong class="color-cate"><span class="bracket">[</span><a href="http://www.paxnet.co.kr/stock/analysis/main?wlog_rpt=list_jm&amp;abbrSymbol=036090">위지트</a><span class="bracket">]</span></strong></div>
    <div>
    <p>
    <a href="javascript:selectView('139094');">반도체 소모성 부품업체로 변신 중</a>
    </p>
    </div>
    <div class="line3">
    <span>적정가격</span>
    	 								
    										
    										
    											-원
    										
    									
    								</div>
    <div class="line3 color-black">
    									-
    								</div>
    <div class="line3">한국IR협의회</div>
    <div class="line3">2022.12.01</div>
    </li>




```python
li_list[-1]
```




    <li><a href="#" onclick="linkPage(5); return false;">5</a></li>




```python
check_str = '<strong class="color-cate"><span class="bracket">'
```


```python
print(check_str in str(li_list[1]))
print(check_str in str(li_list[0]))
print(check_str in str(li_list[-1]))
```

    True
    False
    False
    


```python
stock = li_list[1].find_all("a")[0].text
print(stock)
```

    위지트
    


```python
title = li_list[1].find_all("a")[1].text
print(title)
```

    반도체 소모성 부품업체로 변신 중
    


```python
price = li_list[1].find("div", attrs = {"class" : "line3"}).text
display(price)
```


    '\n적정가격\r\n\t \t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t-원\r\n\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t'



```python
price = price.replace("\r", "").replace("\t", "").replace("\n", "")
price = price.split(" ")[1].replace(",", "")[:-1]
display(price)
```


    '-'



```python
opinion = li_list[1].find_all("div", attrs = {"class" : "line3"})[1].text
display(opinion)
```


    '\r\n\t\t\t\t\t\t\t\t\t-\r\n\t\t\t\t\t\t\t\t'



```python
opinion = opinion.replace("\t", "").replace("\n", "").replace("\r", "")
display(opinion)
```


    '-'



```python
trading_firm = li_list[1].find_all("div", attrs = {"class" : "line3"})[2].text
display(trading_firm)
```


    '한국IR협의회'



```python
date = li_list[1].find_all("div", attrs = {"class" : "line3"})[3].text
display(date)
```


    '2022.12.01'



```python
import pandas as pd
date = pd.to_datetime(date)
display(date)
```


    Timestamp('2022-12-01 00:00:00')


# 단일 리포트 파싱


```python
def parsing_li(li):
  stock = li.find_all("a")[0].text  # 종목
  title = li.find_all("a")[1].text  # 리포트 제목
  price = li.find("div", attrs = {"class" : "line3"}).text # 적정 가격
  price = price.replace("\r", "").replace("\t", "").replace("\n", "")
  price = price.split(" ")[1].replace(",", "")[:-1]
  opinion = li.find_all("div", attrs = {"class" : "line3"})[1].text # 의견
  opinion = opinion.replace("\t", "").replace("\n", "").replace("\r", "")
  trading_firm = li.find_all("div", attrs = {"class" : "line3"})[2].text  #증권사
  date = li.find_all("div", attrs = {"class" : "line3"})[3].text  # 날짜
  date = pd.to_datetime(date)

  return [stock, title, price, opinion, trading_firm, date]
```


```python
print(parsing_li(li_list[1]))
```

    ['위지트', '반도체 소모성 부품업체로 변신 중', '-', '-', '한국IR협의회', Timestamp('2022-12-01 00:00:00')]
    

# 리포트 수집 및 출력


```python
data = list()
for li in li_list:
  if check_str in str(li):
    record = parsing_li(li)
    data.append(record)
  
data = pd.DataFrame(data, columns = ["종목명", "리포트제목", "적정가격", "의견", "증권사", "날짜"])
```


```python
display(data.head(10))
```



  <div id="df-8f4c68a7-fe63-4475-8c36-1a9746d8ad18">
    <div class="colab-df-container">
      <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>종목명</th>
      <th>리포트제목</th>
      <th>적정가격</th>
      <th>의견</th>
      <th>증권사</th>
      <th>날짜</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>위지트</td>
      <td>반도체 소모성 부품업체로 변신 중</td>
      <td>-</td>
      <td>-</td>
      <td>한국IR협의회</td>
      <td>2022-12-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>하이브</td>
      <td>조커 카드가 될 유료 구독 모델 도입</td>
      <td>210000</td>
      <td>매수</td>
      <td>유안타증권</td>
      <td>2022-12-01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>로체시스템즈</td>
      <td>견조한 성장세에도 매력적인 Valuation 주목</td>
      <td>-</td>
      <td>-</td>
      <td>키움증권</td>
      <td>2022-12-01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>원텍</td>
      <td>블록버스터 등극을 예고하는 올리지오</td>
      <td>-</td>
      <td>-</td>
      <td>키움증권</td>
      <td>2022-12-01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>제이브이엠</td>
      <td>해외 약국의 디지털화 수혜 지속 전망</td>
      <td>-</td>
      <td>-</td>
      <td>키움증권</td>
      <td>2022-12-01</td>
    </tr>
    <tr>
      <th>5</th>
      <td>두산퓨얼셀</td>
      <td>길었던 인고의 시간, 끝이 보인다</td>
      <td>-</td>
      <td>-</td>
      <td>키움증권</td>
      <td>2022-12-01</td>
    </tr>
    <tr>
      <th>6</th>
      <td>아이디스홀딩스</td>
      <td>비대면 무인시대 4륜구동 르네상스</td>
      <td>-</td>
      <td>-</td>
      <td>한국IR협의회</td>
      <td>2022-11-30</td>
    </tr>
    <tr>
      <th>7</th>
      <td>아이패밀리에스씨</td>
      <td>위기에도 성장을 기대할 수 있는 이유</td>
      <td>-</td>
      <td>-</td>
      <td>한국IR협의회</td>
      <td>2022-11-30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>LG에너지솔루션</td>
      <td>2023 년 질적 성장의 토대 마련</td>
      <td>-</td>
      <td>-</td>
      <td>메리츠증권</td>
      <td>2022-11-30</td>
    </tr>
    <tr>
      <th>9</th>
      <td>현대건설</td>
      <td>업황 둔화 우려에도 기대 요인은 여전</td>
      <td>55000</td>
      <td>매수</td>
      <td>유안타증권</td>
      <td>2022-11-30</td>
    </tr>
  </tbody>
</table>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-8f4c68a7-fe63-4475-8c36-1a9746d8ad18')"
              title="Convert this dataframe to an interactive table."
              style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
  </svg>
      </button>

  <style>
    .colab-df-container {
      display:flex;
      flex-wrap:wrap;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

      <script>
        const buttonEl =
          document.querySelector('#df-8f4c68a7-fe63-4475-8c36-1a9746d8ad18 button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-8f4c68a7-fe63-4475-8c36-1a9746d8ad18');
          const dataTable =
            await google.colab.kernel.invokeFunction('convertToInteractive',
                                                     [key], {});
          if (!dataTable) return;

          const docLinkHtml = 'Like what you see? Visit the ' +
            '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
            + ' to learn more about interactive tables.';
          element.innerHTML = '';
          dataTable['output_type'] = 'display_data';
          await google.colab.output.renderOutput(dataTable, element);
          const docLink = document.createElement('div');
          docLink.innerHTML = docLinkHtml;
          element.appendChild(docLink);
        }
      </script>
    </div>
  </div>




```python
import time
base_url = "http://www.paxnet.co.kr/stock/report/report?menuCode=2222&currentPageNo={}&reportId=0&searchKey=stock&searchValue="
data = []

for page_no in range(1, 563):
  url = base_url.format(page_no)
  while(True):
    response = requests.get(url)
    if response.status_code == 200:
      time.sleep(1)
      break
    else:
      time.sleep(10 * 60)
  html = response.content
  html = BS(html)

  div = html.find("div", attrs = {"class":"board-type"})
  li_list = div.find_all("li")
  for li in li_list:
    if check_str in str(li):
      record = parsing_li(li)
      data.append(record)

data = pd.DataFrame(data, columns = ["종목명", "리포트제목", "적정가격", "의견", "증권사", "날짜"])
```


```python
import time
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
data.to_csv("../{}종목리포트.txt".format(today), sep = "\t", encoding = "euc-kr", index = False)
```


```python

```
