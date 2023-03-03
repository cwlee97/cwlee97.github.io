---
layout: single
title: "Dividend Analysis Open Dart Reader"
categories: TIL
---
```python
!pip install OpenDartReader
```

    Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
    Collecting OpenDartReader
      Downloading OpenDartReader-0.2.1-py3-none-any.whl (27 kB)
    Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.8/dist-packages (from OpenDartReader) (4.6.3)
    Collecting requests-file
      Downloading requests_file-1.5.1-py2.py3-none-any.whl (3.7 kB)
    Requirement already satisfied: pandas>=0.19.2 in /usr/local/lib/python3.8/dist-packages (from OpenDartReader) (1.3.5)
    Requirement already satisfied: requests>=2.3.0 in /usr/local/lib/python3.8/dist-packages (from OpenDartReader) (2.23.0)
    Requirement already satisfied: lxml in /usr/local/lib/python3.8/dist-packages (from OpenDartReader) (4.9.1)
    Requirement already satisfied: numpy>=1.17.3 in /usr/local/lib/python3.8/dist-packages (from pandas>=0.19.2->OpenDartReader) (1.21.6)
    Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.8/dist-packages (from pandas>=0.19.2->OpenDartReader) (2.8.2)
    Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.8/dist-packages (from pandas>=0.19.2->OpenDartReader) (2022.6)
    Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.8/dist-packages (from python-dateutil>=2.7.3->pandas>=0.19.2->OpenDartReader) (1.15.0)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.8/dist-packages (from requests>=2.3.0->OpenDartReader) (1.24.3)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.8/dist-packages (from requests>=2.3.0->OpenDartReader) (2022.9.24)
    Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.8/dist-packages (from requests>=2.3.0->OpenDartReader) (3.0.4)
    Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.8/dist-packages (from requests>=2.3.0->OpenDartReader) (2.10)
    Installing collected packages: requests-file, OpenDartReader
    Successfully installed OpenDartReader-0.2.1 requests-file-1.5.1
    


```python
import OpenDartReader
my_api = "***************************************"
dart = OpenDartReader(my_api)
```


```python
# SK하이닉스
SK_report = dart.report("SK하이닉스", "배당", 2020, "11011")
display(SK_report)
```



  <div id="df-dfdc71fa-33c0-41a1-8198-42d3c8a1ef16">
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
      <th>rcept_no</th>
      <th>corp_cls</th>
      <th>corp_code</th>
      <th>corp_name</th>
      <th>se</th>
      <th>thstrm</th>
      <th>frmtrm</th>
      <th>lwfr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>주당액면가액(원)</td>
      <td>5,000</td>
      <td>5,000</td>
      <td>5,000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>(연결)당기순이익(백만원)</td>
      <td>4,755,102</td>
      <td>2,005,975</td>
      <td>15,540,111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>(별도)당기순이익(백만원)</td>
      <td>4,217,841</td>
      <td>1,476,981</td>
      <td>15,407,086</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>(연결)주당순이익(원)</td>
      <td>6,952</td>
      <td>2,933</td>
      <td>22,255</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>현금배당금총액(백만원)</td>
      <td>800,282</td>
      <td>684,002</td>
      <td>1,026,003</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>주식배당금총액(백만원)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>(연결)현금배당성향(%)</td>
      <td>16.80</td>
      <td>34.10</td>
      <td>6.60</td>
    </tr>
    <tr>
      <th>7</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>현금배당수익률(%)</td>
      <td>1.00</td>
      <td>1.10</td>
      <td>2.50</td>
    </tr>
    <tr>
      <th>8</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>현금배당수익률(%)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>주식배당수익률(%)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>주식배당수익률(%)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>11</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>주당 현금배당금(원)</td>
      <td>1,170</td>
      <td>1,000</td>
      <td>1,500</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>주당 현금배당금(원)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>주당 주식배당(주)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20210330000776</td>
      <td>Y</td>
      <td>00164779</td>
      <td>SK하이닉스</td>
      <td>주당 주식배당(주)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-dfdc71fa-33c0-41a1-8198-42d3c8a1ef16')"
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
          document.querySelector('#df-dfdc71fa-33c0-41a1-8198-42d3c8a1ef16 button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-dfdc71fa-33c0-41a1-8198-42d3c8a1ef16');
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
# 삼성전자
SAMSUNG_report = dart.report("삼성전자", "배당", 2020, "11011")
display(SAMSUNG_report)
```



  <div id="df-ff48bc4c-5626-448e-b4ba-b9f2f5aa076e">
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
      <th>rcept_no</th>
      <th>corp_cls</th>
      <th>corp_code</th>
      <th>corp_name</th>
      <th>se</th>
      <th>thstrm</th>
      <th>frmtrm</th>
      <th>lwfr</th>
      <th>stock_knd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>주당액면가액(원)</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>(연결)당기순이익(백만원)</td>
      <td>26,090,846</td>
      <td>21,505,054</td>
      <td>43,890,877</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>(별도)당기순이익(백만원)</td>
      <td>15,615,018</td>
      <td>15,353,323</td>
      <td>32,815,127</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>(연결)주당순이익(원)</td>
      <td>3,841</td>
      <td>3,166</td>
      <td>6,461</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>현금배당금총액(백만원)</td>
      <td>20,338,075</td>
      <td>9,619,243</td>
      <td>9,619,243</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>주식배당금총액(백만원)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>(연결)현금배당성향(%)</td>
      <td>78.00</td>
      <td>44.70</td>
      <td>21.90</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>현금배당수익률(%)</td>
      <td>4.00</td>
      <td>2.60</td>
      <td>3.70</td>
      <td>보통주</td>
    </tr>
    <tr>
      <th>8</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>현금배당수익률(%)</td>
      <td>4.20</td>
      <td>3.10</td>
      <td>4.50</td>
      <td>우선주</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>주식배당수익률(%)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>보통주</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>주식배당수익률(%)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>우선주</td>
    </tr>
    <tr>
      <th>11</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>주당 현금배당금(원)</td>
      <td>2,994</td>
      <td>1,416</td>
      <td>1,416</td>
      <td>보통주</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>주당 현금배당금(원)</td>
      <td>2,995</td>
      <td>1,417</td>
      <td>1,417</td>
      <td>우선주</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>주당 주식배당(주)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>보통주</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20210309000744</td>
      <td>Y</td>
      <td>00126380</td>
      <td>삼성전자</td>
      <td>주당 주식배당(주)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>우선주</td>
    </tr>
  </tbody>
</table>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-ff48bc4c-5626-448e-b4ba-b9f2f5aa076e')"
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
          document.querySelector('#df-ff48bc4c-5626-448e-b4ba-b9f2f5aa076e button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-ff48bc4c-5626-448e-b4ba-b9f2f5aa076e');
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
# 3S
threeS_report = dart.report("3S", "배당", 2020, "11011")
display(threeS_report)
```



  <div id="df-1cdb6b07-bdc0-4fcd-bf63-1794cbb02eea">
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
      <th>rcept_no</th>
      <th>corp_cls</th>
      <th>corp_code</th>
      <th>corp_name</th>
      <th>se</th>
      <th>thstrm</th>
      <th>frmtrm</th>
      <th>lwfr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>주당액면가액(원)</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>(연결)당기순이익(백만원)</td>
      <td>-1,080</td>
      <td>1,411</td>
      <td>-1,432</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>(별도)당기순이익(백만원)</td>
      <td>-728</td>
      <td>1,184</td>
      <td>-2,052</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>(연결)주당순이익(원)</td>
      <td>-24</td>
      <td>32</td>
      <td>-34</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>현금배당금총액(백만원)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>주식배당금총액(백만원)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>(연결)현금배당성향(%)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>7</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>현금배당수익률(%)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>8</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>현금배당수익률(%)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>주식배당수익률(%)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>주식배당수익률(%)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>11</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>주당 현금배당금(원)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>주당 현금배당금(원)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>주당 주식배당(주)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20210419000001</td>
      <td>K</td>
      <td>00378363</td>
      <td>3S</td>
      <td>주당 주식배당(주)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-1cdb6b07-bdc0-4fcd-bf63-1794cbb02eea')"
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
          document.querySelector('#df-1cdb6b07-bdc0-4fcd-bf63-1794cbb02eea button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-1cdb6b07-bdc0-4fcd-bf63-1794cbb02eea');
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
import numpy as np
def find_div_and_EPS(stock, year):
  report = dart.report(stock, "배당", year, "11011")
  output = dict()
  if report is None:
    output["주식배당금"] = np.nan, np.nan, np.nan
    output["주당순이익"] = np.nan, np.nan, np.nan

  else:
    div_row = report.loc[(report['se']) == '주당 현금배당금(원)'].iloc[0]
    
    cur_div = int(div_row['thstrm'].replace('-', '0').replace(',', ''))
    pre_div = int(div_row['frmtrm'].replace('-', '0').replace(',', ''))
    spre_div = int(div_row['lwfr'].replace('-', '0').replace(',', ''))
    output['주당배당금'] = spre_div, pre_div, cur_div

    EPS_row = report.loc[(report['se'].str.contains('주당순이익'))].iloc[0]

    cur_EPS = int(EPS_row['thstrm'].replace('-', '0').replace(',', ''))
    pre_EPS = int(EPS_row['frmtrm'].replace('-', '0').replace(',', ''))
    spre_EPS = int(EPS_row['lwfr'].replace('-', '0').replace(',', ''))
    output['주당순이익'] = spre_EPS, pre_EPS, cur_EPS

  return output
```


```python
print(find_div_and_EPS("삼성전자", 2020))
print(find_div_and_EPS("SK하이닉스", 2020))
```

    {'주당배당금': (1416, 1416, 2994), '주당순이익': (6461, 3166, 3841)}
    {'주당배당금': (1500, 1000, 1170), '주당순이익': (22255, 2933, 6952)}
    

데이터 파싱


```python
from google.colab import drive
drive.mount('/content/drive')
```

    Mounted at /content/drive
    


```python
import time
import pandas as pd

stock_list = pd.read_csv("/content/drive/MyDrive/Quant_project/data/종목정보.txt", sep = "\t", encoding = "euc-kr")
stock_name_list = stock_list["Name"].values
div_data, EPS_data = list(), list()
for idx, stock_name in enumerate(stock_name_list):
  print(idx+1, "/", len(stock_name_list))
  div_record, EPS_record = [stock_name], [stock_name]
  for year in [2015, 2018, 2020]:
    while True:
      try:
        output = find_div_and_EPS(stock_name, year)
        #time.sleep(0.5)
        break
      except:
        break
    spre_divs, pre_divs, cur_divs = output["주당배당금"]
    if year != 2020:
      div_record += [spre_divs, pre_divs, cur_divs]
    else:
      div_record += [pre_divs, cur_divs]
    spre_EPS, pre_EPS, cur_EPS = output["주당순이익"]
    if year != 2020:
      EPS_record += [spre_EPS, pre_EPS, cur_EPS]
    else:
      EPS_record += [pre_EPS, cur_EPS]
  div_data.append(div_record)
  EPS_data.append(EPS_record)
```

    1 / 2554
    2 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    3 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    4 / 2554
    5 / 2554
    6 / 2554
    7 / 2554
    8 / 2554
    9 / 2554
    10 / 2554
    11 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    12 / 2554
    13 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    14 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    15 / 2554
    16 / 2554
    17 / 2554
    18 / 2554
    19 / 2554
    20 / 2554
    21 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    22 / 2554
    23 / 2554
    24 / 2554
    25 / 2554
    26 / 2554
    27 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    28 / 2554
    29 / 2554
    30 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    31 / 2554
    32 / 2554
    33 / 2554
    34 / 2554
    35 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    36 / 2554
    37 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    38 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    39 / 2554
    40 / 2554
    41 / 2554
    42 / 2554
    43 / 2554
    44 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    45 / 2554
    46 / 2554
    47 / 2554
    48 / 2554
    49 / 2554
    50 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    51 / 2554
    52 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    53 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    54 / 2554
    55 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    56 / 2554
    57 / 2554
    58 / 2554
    59 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    60 / 2554
    61 / 2554
    62 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    63 / 2554
    64 / 2554
    65 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    66 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    67 / 2554
    68 / 2554
    69 / 2554
    70 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    71 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    72 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    73 / 2554
    74 / 2554
    75 / 2554
    76 / 2554
    77 / 2554
    78 / 2554
    79 / 2554
    80 / 2554
    81 / 2554
    82 / 2554
    83 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    84 / 2554
    85 / 2554
    86 / 2554
    87 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    88 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    89 / 2554
    90 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    91 / 2554
    92 / 2554
    93 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    94 / 2554
    95 / 2554
    96 / 2554
    97 / 2554
    98 / 2554
    99 / 2554
    100 / 2554
    101 / 2554
    102 / 2554
    103 / 2554
    104 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    105 / 2554
    106 / 2554
    107 / 2554
    108 / 2554
    109 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    110 / 2554
    111 / 2554
    112 / 2554
    113 / 2554
    114 / 2554
    115 / 2554
    116 / 2554
    117 / 2554
    118 / 2554
    119 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    120 / 2554
    121 / 2554
    122 / 2554
    123 / 2554
    124 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    125 / 2554
    126 / 2554
    127 / 2554
    128 / 2554
    129 / 2554
    130 / 2554
    131 / 2554
    132 / 2554
    133 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    134 / 2554
    135 / 2554
    136 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    137 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    138 / 2554
    139 / 2554
    140 / 2554
    141 / 2554
    142 / 2554
    143 / 2554
    144 / 2554
    145 / 2554
    146 / 2554
    147 / 2554
    148 / 2554
    149 / 2554
    150 / 2554
    151 / 2554
    152 / 2554
    153 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    154 / 2554
    155 / 2554
    156 / 2554
    157 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    158 / 2554
    159 / 2554
    160 / 2554
    161 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    162 / 2554
    163 / 2554
    164 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    165 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    166 / 2554
    167 / 2554
    168 / 2554
    169 / 2554
    170 / 2554
    171 / 2554
    172 / 2554
    173 / 2554
    174 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    175 / 2554
    176 / 2554
    177 / 2554
    178 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    179 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    180 / 2554
    181 / 2554
    182 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    183 / 2554
    184 / 2554
    185 / 2554
    186 / 2554
    187 / 2554
    188 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    189 / 2554
    190 / 2554
    191 / 2554
    192 / 2554
    193 / 2554
    194 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    195 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    196 / 2554
    197 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    198 / 2554
    199 / 2554
    200 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    201 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    202 / 2554
    203 / 2554
    204 / 2554
    205 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    206 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    207 / 2554
    208 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    209 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    210 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    211 / 2554
    212 / 2554
    213 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    214 / 2554
    215 / 2554
    216 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    217 / 2554
    218 / 2554
    219 / 2554
    220 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    221 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    222 / 2554
    223 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    224 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    225 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    226 / 2554
    227 / 2554
    228 / 2554
    229 / 2554
    230 / 2554
    231 / 2554
    232 / 2554
    233 / 2554
    234 / 2554
    235 / 2554
    236 / 2554
    237 / 2554
    238 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    239 / 2554
    240 / 2554
    241 / 2554
    242 / 2554
    243 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    244 / 2554
    245 / 2554
    246 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    247 / 2554
    248 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    249 / 2554
    250 / 2554
    251 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    252 / 2554
    253 / 2554
    254 / 2554
    255 / 2554
    256 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    257 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    258 / 2554
    259 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    260 / 2554
    261 / 2554
    262 / 2554
    263 / 2554
    264 / 2554
    265 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    266 / 2554
    267 / 2554
    268 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    269 / 2554
    270 / 2554
    271 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    272 / 2554
    273 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    274 / 2554
    275 / 2554
    276 / 2554
    277 / 2554
    278 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    279 / 2554
    280 / 2554
    281 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    282 / 2554
    283 / 2554
    284 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    285 / 2554
    286 / 2554
    287 / 2554
    288 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    289 / 2554
    290 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    291 / 2554
    292 / 2554
    293 / 2554
    294 / 2554
    295 / 2554
    296 / 2554
    297 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    298 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    299 / 2554
    300 / 2554
    301 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    302 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    303 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    304 / 2554
    305 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    306 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    307 / 2554
    308 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    309 / 2554
    310 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    311 / 2554
    312 / 2554
    313 / 2554
    314 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    315 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    316 / 2554
    317 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    318 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    319 / 2554
    320 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    321 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    322 / 2554
    323 / 2554
    324 / 2554
    325 / 2554
    326 / 2554
    327 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    328 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    329 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    330 / 2554
    331 / 2554
    332 / 2554
    333 / 2554
    334 / 2554
    335 / 2554
    336 / 2554
    337 / 2554
    338 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    339 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    340 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    341 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    342 / 2554
    343 / 2554
    344 / 2554
    345 / 2554
    346 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    347 / 2554
    348 / 2554
    349 / 2554
    350 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    351 / 2554
    352 / 2554
    353 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    354 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    355 / 2554
    356 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    357 / 2554
    358 / 2554
    359 / 2554
    360 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    361 / 2554
    362 / 2554
    363 / 2554
    364 / 2554
    365 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    366 / 2554
    367 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    368 / 2554
    369 / 2554
    370 / 2554
    371 / 2554
    372 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    373 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    374 / 2554
    375 / 2554
    376 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    377 / 2554
    378 / 2554
    379 / 2554
    380 / 2554
    381 / 2554
    382 / 2554
    383 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    384 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    385 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    386 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    387 / 2554
    388 / 2554
    389 / 2554
    390 / 2554
    391 / 2554
    392 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    393 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    394 / 2554
    395 / 2554
    396 / 2554
    397 / 2554
    398 / 2554
    399 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    400 / 2554
    401 / 2554
    402 / 2554
    403 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    404 / 2554
    405 / 2554
    406 / 2554
    407 / 2554
    408 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    409 / 2554
    410 / 2554
    411 / 2554
    412 / 2554
    413 / 2554
    414 / 2554
    415 / 2554
    416 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    417 / 2554
    418 / 2554
    419 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    420 / 2554
    421 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    422 / 2554
    423 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    424 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    425 / 2554
    426 / 2554
    427 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    428 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    429 / 2554
    430 / 2554
    431 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    432 / 2554
    433 / 2554
    434 / 2554
    435 / 2554
    436 / 2554
    437 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    438 / 2554
    439 / 2554
    440 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    441 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    442 / 2554
    443 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    444 / 2554
    445 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    446 / 2554
    447 / 2554
    448 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    449 / 2554
    450 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    451 / 2554
    452 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    453 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    454 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    455 / 2554
    456 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    457 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    458 / 2554
    459 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    460 / 2554
    461 / 2554
    462 / 2554
    463 / 2554
    464 / 2554
    465 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    466 / 2554
    467 / 2554
    468 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    469 / 2554
    470 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    471 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    472 / 2554
    473 / 2554
    474 / 2554
    475 / 2554
    476 / 2554
    477 / 2554
    478 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    479 / 2554
    480 / 2554
    481 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    482 / 2554
    483 / 2554
    484 / 2554
    485 / 2554
    486 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    487 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    488 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    489 / 2554
    490 / 2554
    491 / 2554
    492 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    493 / 2554
    494 / 2554
    495 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    496 / 2554
    497 / 2554
    498 / 2554
    499 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    500 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    501 / 2554
    502 / 2554
    503 / 2554
    504 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    505 / 2554
    506 / 2554
    507 / 2554
    508 / 2554
    509 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    510 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    511 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    512 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    513 / 2554
    514 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    515 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    516 / 2554
    517 / 2554
    518 / 2554
    519 / 2554
    520 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    521 / 2554
    522 / 2554
    523 / 2554
    524 / 2554
    525 / 2554
    526 / 2554
    527 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    528 / 2554
    529 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    530 / 2554
    531 / 2554
    532 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    533 / 2554
    534 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    535 / 2554
    536 / 2554
    537 / 2554
    538 / 2554
    539 / 2554
    540 / 2554
    541 / 2554
    542 / 2554
    543 / 2554
    544 / 2554
    545 / 2554
    546 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    547 / 2554
    548 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    549 / 2554
    550 / 2554
    551 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    552 / 2554
    553 / 2554
    554 / 2554
    555 / 2554
    556 / 2554
    557 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    558 / 2554
    559 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    560 / 2554
    561 / 2554
    562 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    563 / 2554
    564 / 2554
    565 / 2554
    566 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    567 / 2554
    568 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    569 / 2554
    570 / 2554
    571 / 2554
    572 / 2554
    573 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    574 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    575 / 2554
    576 / 2554
    577 / 2554
    578 / 2554
    579 / 2554
    580 / 2554
    581 / 2554
    582 / 2554
    583 / 2554
    584 / 2554
    585 / 2554
    586 / 2554
    587 / 2554
    588 / 2554
    589 / 2554
    590 / 2554
    591 / 2554
    592 / 2554
    593 / 2554
    594 / 2554
    595 / 2554
    596 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    597 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    598 / 2554
    599 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    600 / 2554
    601 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    602 / 2554
    603 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    604 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    605 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    606 / 2554
    607 / 2554
    608 / 2554
    609 / 2554
    610 / 2554
    611 / 2554
    612 / 2554
    613 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    614 / 2554
    615 / 2554
    616 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    617 / 2554
    618 / 2554
    619 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    620 / 2554
    621 / 2554
    622 / 2554
    623 / 2554
    624 / 2554
    625 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    626 / 2554
    627 / 2554
    628 / 2554
    629 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    630 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    631 / 2554
    632 / 2554
    633 / 2554
    634 / 2554
    635 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    636 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    637 / 2554
    638 / 2554
    639 / 2554
    640 / 2554
    641 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    642 / 2554
    643 / 2554
    644 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    645 / 2554
    646 / 2554
    647 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    648 / 2554
    649 / 2554
    650 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    651 / 2554
    652 / 2554
    653 / 2554
    654 / 2554
    655 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    656 / 2554
    657 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    658 / 2554
    659 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    660 / 2554
    661 / 2554
    662 / 2554
    663 / 2554
    664 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    665 / 2554
    666 / 2554
    667 / 2554
    668 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    669 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    670 / 2554
    671 / 2554
    672 / 2554
    673 / 2554
    674 / 2554
    675 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    676 / 2554
    677 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    678 / 2554
    679 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    680 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    681 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    682 / 2554
    683 / 2554
    684 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    685 / 2554
    686 / 2554
    687 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    688 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    689 / 2554
    690 / 2554
    691 / 2554
    692 / 2554
    693 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    694 / 2554
    695 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    696 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    697 / 2554
    698 / 2554
    699 / 2554
    700 / 2554
    701 / 2554
    702 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    703 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    704 / 2554
    705 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    706 / 2554
    707 / 2554
    708 / 2554
    709 / 2554
    710 / 2554
    711 / 2554
    712 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    713 / 2554
    714 / 2554
    715 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    716 / 2554
    717 / 2554
    718 / 2554
    719 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    720 / 2554
    721 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    722 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    723 / 2554
    724 / 2554
    725 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    726 / 2554
    727 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    728 / 2554
    729 / 2554
    730 / 2554
    731 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    732 / 2554
    733 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    734 / 2554
    735 / 2554
    736 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    737 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    738 / 2554
    739 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    740 / 2554
    741 / 2554
    742 / 2554
    743 / 2554
    744 / 2554
    745 / 2554
    746 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    747 / 2554
    748 / 2554
    749 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    750 / 2554
    751 / 2554
    752 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    753 / 2554
    754 / 2554
    755 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    756 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    757 / 2554
    758 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    759 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    760 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    761 / 2554
    762 / 2554
    763 / 2554
    764 / 2554
    765 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    766 / 2554
    767 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    768 / 2554
    769 / 2554
    770 / 2554
    771 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    772 / 2554
    773 / 2554
    774 / 2554
    775 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    776 / 2554
    777 / 2554
    778 / 2554
    779 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    780 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    781 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    782 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    783 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    784 / 2554
    785 / 2554
    786 / 2554
    787 / 2554
    788 / 2554
    789 / 2554
    790 / 2554
    791 / 2554
    792 / 2554
    793 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    794 / 2554
    795 / 2554
    796 / 2554
    797 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    798 / 2554
    799 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    800 / 2554
    801 / 2554
    802 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    803 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    804 / 2554
    805 / 2554
    806 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    807 / 2554
    808 / 2554
    809 / 2554
    810 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    811 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    812 / 2554
    813 / 2554
    814 / 2554
    815 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    816 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    817 / 2554
    818 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    819 / 2554
    820 / 2554
    821 / 2554
    822 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    823 / 2554
    824 / 2554
    825 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    826 / 2554
    827 / 2554
    828 / 2554
    829 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    830 / 2554
    831 / 2554
    832 / 2554
    833 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    834 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    835 / 2554
    836 / 2554
    837 / 2554
    838 / 2554
    839 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    840 / 2554
    841 / 2554
    842 / 2554
    843 / 2554
    844 / 2554
    845 / 2554
    846 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    847 / 2554
    848 / 2554
    849 / 2554
    850 / 2554
    851 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    852 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    853 / 2554
    854 / 2554
    855 / 2554
    856 / 2554
    857 / 2554
    858 / 2554
    859 / 2554
    860 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    861 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    862 / 2554
    863 / 2554
    864 / 2554
    865 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    866 / 2554
    867 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    868 / 2554
    869 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    870 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    871 / 2554
    872 / 2554
    873 / 2554
    874 / 2554
    875 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    876 / 2554
    877 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    878 / 2554
    879 / 2554
    880 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    881 / 2554
    882 / 2554
    883 / 2554
    884 / 2554
    885 / 2554
    886 / 2554
    887 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    888 / 2554
    889 / 2554
    890 / 2554
    891 / 2554
    892 / 2554
    893 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    894 / 2554
    895 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    896 / 2554
    897 / 2554
    898 / 2554
    899 / 2554
    900 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    901 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    902 / 2554
    903 / 2554
    904 / 2554
    905 / 2554
    906 / 2554
    907 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    908 / 2554
    909 / 2554
    910 / 2554
    911 / 2554
    912 / 2554
    913 / 2554
    914 / 2554
    915 / 2554
    916 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    917 / 2554
    918 / 2554
    919 / 2554
    920 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    921 / 2554
    922 / 2554
    923 / 2554
    924 / 2554
    925 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    926 / 2554
    927 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    928 / 2554
    929 / 2554
    930 / 2554
    931 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    932 / 2554
    933 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    934 / 2554
    935 / 2554
    936 / 2554
    937 / 2554
    938 / 2554
    939 / 2554
    940 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    941 / 2554
    942 / 2554
    943 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    944 / 2554
    945 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    946 / 2554
    947 / 2554
    948 / 2554
    949 / 2554
    950 / 2554
    951 / 2554
    952 / 2554
    953 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    954 / 2554
    955 / 2554
    956 / 2554
    957 / 2554
    958 / 2554
    959 / 2554
    960 / 2554
    961 / 2554
    962 / 2554
    963 / 2554
    964 / 2554
    965 / 2554
    966 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    967 / 2554
    968 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    969 / 2554
    970 / 2554
    971 / 2554
    972 / 2554
    973 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    974 / 2554
    975 / 2554
    976 / 2554
    977 / 2554
    978 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    979 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    980 / 2554
    981 / 2554
    982 / 2554
    983 / 2554
    984 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    985 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    986 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    987 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    988 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    989 / 2554
    990 / 2554
    991 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    992 / 2554
    993 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    994 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    995 / 2554
    996 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    997 / 2554
    998 / 2554
    999 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1000 / 2554
    1001 / 2554
    1002 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1003 / 2554
    1004 / 2554
    1005 / 2554
    1006 / 2554
    1007 / 2554
    1008 / 2554
    1009 / 2554
    1010 / 2554
    1011 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1012 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1013 / 2554
    1014 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1015 / 2554
    1016 / 2554
    1017 / 2554
    1018 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1019 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1020 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1021 / 2554
    1022 / 2554
    1023 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1024 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1025 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1026 / 2554
    1027 / 2554
    1028 / 2554
    1029 / 2554
    1030 / 2554
    1031 / 2554
    1032 / 2554
    1033 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1034 / 2554
    1035 / 2554
    1036 / 2554
    1037 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1038 / 2554
    1039 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1040 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1041 / 2554
    1042 / 2554
    1043 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1044 / 2554
    1045 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1046 / 2554
    1047 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1048 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1049 / 2554
    1050 / 2554
    1051 / 2554
    1052 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1053 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1054 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1055 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1056 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1057 / 2554
    1058 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1059 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1060 / 2554
    1061 / 2554
    1062 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1063 / 2554
    1064 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1065 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1066 / 2554
    1067 / 2554
    1068 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1069 / 2554
    1070 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1071 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1072 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1073 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1074 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1075 / 2554
    1076 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1077 / 2554
    1078 / 2554
    1079 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1080 / 2554
    1081 / 2554
    1082 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1083 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1084 / 2554
    1085 / 2554
    1086 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1087 / 2554
    1088 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1089 / 2554
    1090 / 2554
    1091 / 2554
    1092 / 2554
    1093 / 2554
    1094 / 2554
    1095 / 2554
    1096 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1097 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1098 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1099 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1100 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1101 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1102 / 2554
    1103 / 2554
    1104 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1105 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1106 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1107 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1108 / 2554
    1109 / 2554
    1110 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1111 / 2554
    1112 / 2554
    1113 / 2554
    1114 / 2554
    1115 / 2554
    1116 / 2554
    1117 / 2554
    1118 / 2554
    1119 / 2554
    1120 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1121 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1122 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1123 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1124 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1125 / 2554
    1126 / 2554
    1127 / 2554
    1128 / 2554
    1129 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1130 / 2554
    1131 / 2554
    1132 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1133 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1134 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1135 / 2554
    1136 / 2554
    1137 / 2554
    1138 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1139 / 2554
    1140 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1141 / 2554
    1142 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1143 / 2554
    1144 / 2554
    1145 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1146 / 2554
    1147 / 2554
    1148 / 2554
    1149 / 2554
    1150 / 2554
    1151 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1152 / 2554
    1153 / 2554
    1154 / 2554
    1155 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1156 / 2554
    1157 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1158 / 2554
    1159 / 2554
    1160 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1161 / 2554
    1162 / 2554
    1163 / 2554
    1164 / 2554
    1165 / 2554
    1166 / 2554
    1167 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1168 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1169 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1170 / 2554
    1171 / 2554
    1172 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1173 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1174 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1175 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1176 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1177 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1178 / 2554
    1179 / 2554
    1180 / 2554
    1181 / 2554
    1182 / 2554
    1183 / 2554
    1184 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1185 / 2554
    1186 / 2554
    1187 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1188 / 2554
    1189 / 2554
    1190 / 2554
    1191 / 2554
    1192 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1193 / 2554
    1194 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1195 / 2554
    1196 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1197 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1198 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1199 / 2554
    1200 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1201 / 2554
    1202 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1203 / 2554
    1204 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1205 / 2554
    1206 / 2554
    1207 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1208 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1209 / 2554
    1210 / 2554
    1211 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1212 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1213 / 2554
    1214 / 2554
    1215 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1216 / 2554
    1217 / 2554
    1218 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1219 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1220 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1221 / 2554
    1222 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1223 / 2554
    1224 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1225 / 2554
    1226 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1227 / 2554
    1228 / 2554
    1229 / 2554
    1230 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1231 / 2554
    1232 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1233 / 2554
    1234 / 2554
    1235 / 2554
    1236 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1237 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1238 / 2554
    1239 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1240 / 2554
    1241 / 2554
    1242 / 2554
    1243 / 2554
    1244 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1245 / 2554
    1246 / 2554
    1247 / 2554
    1248 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1249 / 2554
    1250 / 2554
    1251 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1252 / 2554
    1253 / 2554
    1254 / 2554
    1255 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1256 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1257 / 2554
    1258 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1259 / 2554
    1260 / 2554
    1261 / 2554
    1262 / 2554
    1263 / 2554
    1264 / 2554
    1265 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1266 / 2554
    1267 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1268 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1269 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1270 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1271 / 2554
    1272 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1273 / 2554
    1274 / 2554
    1275 / 2554
    1276 / 2554
    1277 / 2554
    1278 / 2554
    1279 / 2554
    1280 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1281 / 2554
    1282 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1283 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1284 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1285 / 2554
    1286 / 2554
    1287 / 2554
    1288 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1289 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1290 / 2554
    1291 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1292 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1293 / 2554
    1294 / 2554
    1295 / 2554
    1296 / 2554
    1297 / 2554
    1298 / 2554
    1299 / 2554
    1300 / 2554
    1301 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1302 / 2554
    1303 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1304 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1305 / 2554
    1306 / 2554
    1307 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1308 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1309 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1310 / 2554
    1311 / 2554
    1312 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1313 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1314 / 2554
    1315 / 2554
    1316 / 2554
    1317 / 2554
    1318 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1319 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1320 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1321 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1322 / 2554
    1323 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1324 / 2554
    1325 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1326 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1327 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1328 / 2554
    1329 / 2554
    1330 / 2554
    1331 / 2554
    1332 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1333 / 2554
    1334 / 2554
    1335 / 2554
    1336 / 2554
    1337 / 2554
    1338 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1339 / 2554
    1340 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1341 / 2554
    1342 / 2554
    1343 / 2554
    1344 / 2554
    1345 / 2554
    1346 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1347 / 2554
    1348 / 2554
    1349 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1350 / 2554
    1351 / 2554
    1352 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1353 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1354 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1355 / 2554
    1356 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1357 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1358 / 2554
    1359 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1360 / 2554
    1361 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1362 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1363 / 2554
    1364 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1365 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1366 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1367 / 2554
    1368 / 2554
    1369 / 2554
    1370 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1371 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1372 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1373 / 2554
    1374 / 2554
    1375 / 2554
    1376 / 2554
    1377 / 2554
    1378 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1379 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1380 / 2554
    1381 / 2554
    1382 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1383 / 2554
    1384 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1385 / 2554
    1386 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1387 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1388 / 2554
    1389 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1390 / 2554
    1391 / 2554
    1392 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1393 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1394 / 2554
    1395 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1396 / 2554
    1397 / 2554
    1398 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1399 / 2554
    1400 / 2554
    1401 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1402 / 2554
    1403 / 2554
    1404 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1405 / 2554
    1406 / 2554
    1407 / 2554
    1408 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1409 / 2554
    1410 / 2554
    1411 / 2554
    1412 / 2554
    1413 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1414 / 2554
    1415 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1416 / 2554
    1417 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1418 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1419 / 2554
    1420 / 2554
    1421 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1422 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1423 / 2554
    1424 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1425 / 2554
    1426 / 2554
    1427 / 2554
    1428 / 2554
    1429 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1430 / 2554
    1431 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1432 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1433 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1434 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1435 / 2554
    1436 / 2554
    1437 / 2554
    1438 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1439 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1440 / 2554
    1441 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1442 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1443 / 2554
    1444 / 2554
    1445 / 2554
    1446 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1447 / 2554
    1448 / 2554
    1449 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1450 / 2554
    1451 / 2554
    1452 / 2554
    1453 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1454 / 2554
    1455 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1456 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1457 / 2554
    1458 / 2554
    1459 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1460 / 2554
    1461 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1462 / 2554
    1463 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1464 / 2554
    1465 / 2554
    1466 / 2554
    1467 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1468 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1469 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1470 / 2554
    1471 / 2554
    1472 / 2554
    1473 / 2554
    1474 / 2554
    1475 / 2554
    1476 / 2554
    1477 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1478 / 2554
    1479 / 2554
    1480 / 2554
    1481 / 2554
    1482 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1483 / 2554
    1484 / 2554
    1485 / 2554
    1486 / 2554
    1487 / 2554
    1488 / 2554
    1489 / 2554
    1490 / 2554
    1491 / 2554
    1492 / 2554
    1493 / 2554
    1494 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1495 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1496 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1497 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1498 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1499 / 2554
    1500 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1501 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1502 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1503 / 2554
    1504 / 2554
    1505 / 2554
    1506 / 2554
    1507 / 2554
    1508 / 2554
    1509 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1510 / 2554
    1511 / 2554
    1512 / 2554
    1513 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1514 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1515 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1516 / 2554
    1517 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1518 / 2554
    1519 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1520 / 2554
    1521 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1522 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1523 / 2554
    1524 / 2554
    1525 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1526 / 2554
    1527 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1528 / 2554
    1529 / 2554
    1530 / 2554
    1531 / 2554
    1532 / 2554
    1533 / 2554
    1534 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1535 / 2554
    1536 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1537 / 2554
    1538 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1539 / 2554
    1540 / 2554
    1541 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1542 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1543 / 2554
    1544 / 2554
    1545 / 2554
    1546 / 2554
    1547 / 2554
    1548 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1549 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1550 / 2554
    1551 / 2554
    1552 / 2554
    1553 / 2554
    1554 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1555 / 2554
    1556 / 2554
    1557 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1558 / 2554
    1559 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1560 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1561 / 2554
    1562 / 2554
    1563 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1564 / 2554
    1565 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1566 / 2554
    1567 / 2554
    1568 / 2554
    1569 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1570 / 2554
    1571 / 2554
    1572 / 2554
    1573 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1574 / 2554
    1575 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1576 / 2554
    1577 / 2554
    1578 / 2554
    1579 / 2554
    1580 / 2554
    1581 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1582 / 2554
    1583 / 2554
    1584 / 2554
    1585 / 2554
    1586 / 2554
    1587 / 2554
    1588 / 2554
    1589 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1590 / 2554
    1591 / 2554
    1592 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1593 / 2554
    1594 / 2554
    1595 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1596 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1597 / 2554
    1598 / 2554
    1599 / 2554
    1600 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1601 / 2554
    1602 / 2554
    1603 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1604 / 2554
    1605 / 2554
    1606 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1607 / 2554
    1608 / 2554
    1609 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1610 / 2554
    1611 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1612 / 2554
    1613 / 2554
    1614 / 2554
    1615 / 2554
    1616 / 2554
    1617 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1618 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1619 / 2554
    1620 / 2554
    1621 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1622 / 2554
    1623 / 2554
    1624 / 2554
    1625 / 2554
    1626 / 2554
    1627 / 2554
    1628 / 2554
    1629 / 2554
    1630 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1631 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1632 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1633 / 2554
    1634 / 2554
    1635 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1636 / 2554
    1637 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1638 / 2554
    1639 / 2554
    1640 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1641 / 2554
    1642 / 2554
    1643 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1644 / 2554
    1645 / 2554
    1646 / 2554
    1647 / 2554
    1648 / 2554
    1649 / 2554
    1650 / 2554
    1651 / 2554
    1652 / 2554
    1653 / 2554
    1654 / 2554
    1655 / 2554
    1656 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1657 / 2554
    1658 / 2554
    1659 / 2554
    1660 / 2554
    1661 / 2554
    1662 / 2554
    1663 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1664 / 2554
    1665 / 2554
    1666 / 2554
    1667 / 2554
    1668 / 2554
    1669 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1670 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1671 / 2554
    1672 / 2554
    1673 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1674 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1675 / 2554
    1676 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1677 / 2554
    1678 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1679 / 2554
    1680 / 2554
    1681 / 2554
    1682 / 2554
    1683 / 2554
    1684 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1685 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1686 / 2554
    1687 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1688 / 2554
    1689 / 2554
    1690 / 2554
    1691 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1692 / 2554
    1693 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1694 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1695 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1696 / 2554
    1697 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1698 / 2554
    1699 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1700 / 2554
    1701 / 2554
    1702 / 2554
    1703 / 2554
    1704 / 2554
    1705 / 2554
    1706 / 2554
    1707 / 2554
    1708 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1709 / 2554
    1710 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1711 / 2554
    1712 / 2554
    1713 / 2554
    1714 / 2554
    1715 / 2554
    1716 / 2554
    1717 / 2554
    1718 / 2554
    1719 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1720 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1721 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1722 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1723 / 2554
    1724 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1725 / 2554
    1726 / 2554
    1727 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1728 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1729 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1730 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1731 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1732 / 2554
    1733 / 2554
    1734 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1735 / 2554
    1736 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1737 / 2554
    1738 / 2554
    1739 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1740 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1741 / 2554
    1742 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1743 / 2554
    1744 / 2554
    1745 / 2554
    1746 / 2554
    1747 / 2554
    1748 / 2554
    1749 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1750 / 2554
    1751 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1752 / 2554
    1753 / 2554
    1754 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1755 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1756 / 2554
    1757 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1758 / 2554
    1759 / 2554
    1760 / 2554
    1761 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1762 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1763 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1764 / 2554
    1765 / 2554
    1766 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1767 / 2554
    1768 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1769 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1770 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1771 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1772 / 2554
    1773 / 2554
    1774 / 2554
    1775 / 2554
    1776 / 2554
    1777 / 2554
    1778 / 2554
    1779 / 2554
    1780 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1781 / 2554
    1782 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1783 / 2554
    1784 / 2554
    1785 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1786 / 2554
    1787 / 2554
    1788 / 2554
    1789 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1790 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1791 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1792 / 2554
    1793 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1794 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1795 / 2554
    1796 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1797 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1798 / 2554
    1799 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1800 / 2554
    1801 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1802 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1803 / 2554
    1804 / 2554
    1805 / 2554
    1806 / 2554
    1807 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1808 / 2554
    1809 / 2554
    1810 / 2554
    1811 / 2554
    1812 / 2554
    1813 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1814 / 2554
    1815 / 2554
    1816 / 2554
    1817 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1818 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1819 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1820 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1821 / 2554
    1822 / 2554
    1823 / 2554
    1824 / 2554
    1825 / 2554
    1826 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1827 / 2554
    1828 / 2554
    1829 / 2554
    1830 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1831 / 2554
    1832 / 2554
    1833 / 2554
    1834 / 2554
    1835 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1836 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1837 / 2554
    1838 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1839 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1840 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1841 / 2554
    1842 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1843 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1844 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1845 / 2554
    1846 / 2554
    1847 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1848 / 2554
    1849 / 2554
    1850 / 2554
    1851 / 2554
    1852 / 2554
    1853 / 2554
    1854 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1855 / 2554
    1856 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1857 / 2554
    1858 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1859 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1860 / 2554
    1861 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1862 / 2554
    1863 / 2554
    1864 / 2554
    1865 / 2554
    1866 / 2554
    1867 / 2554
    1868 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1869 / 2554
    1870 / 2554
    1871 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1872 / 2554
    1873 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1874 / 2554
    1875 / 2554
    1876 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1877 / 2554
    1878 / 2554
    1879 / 2554
    1880 / 2554
    1881 / 2554
    1882 / 2554
    1883 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1884 / 2554
    1885 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1886 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1887 / 2554
    1888 / 2554
    1889 / 2554
    1890 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1891 / 2554
    1892 / 2554
    1893 / 2554
    1894 / 2554
    1895 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1896 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1897 / 2554
    1898 / 2554
    1899 / 2554
    1900 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1901 / 2554
    1902 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1903 / 2554
    1904 / 2554
    1905 / 2554
    1906 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1907 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1908 / 2554
    1909 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1910 / 2554
    1911 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1912 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1913 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1914 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1915 / 2554
    1916 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1917 / 2554
    1918 / 2554
    1919 / 2554
    1920 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1921 / 2554
    1922 / 2554
    1923 / 2554
    1924 / 2554
    1925 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1926 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1927 / 2554
    1928 / 2554
    1929 / 2554
    1930 / 2554
    1931 / 2554
    1932 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1933 / 2554
    1934 / 2554
    1935 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1936 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1937 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1938 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1939 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1940 / 2554
    1941 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1942 / 2554
    1943 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1944 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1945 / 2554
    1946 / 2554
    1947 / 2554
    1948 / 2554
    1949 / 2554
    1950 / 2554
    1951 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1952 / 2554
    1953 / 2554
    1954 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1955 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1956 / 2554
    1957 / 2554
    1958 / 2554
    1959 / 2554
    1960 / 2554
    1961 / 2554
    1962 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1963 / 2554
    1964 / 2554
    1965 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1966 / 2554
    1967 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1968 / 2554
    1969 / 2554
    1970 / 2554
    1971 / 2554
    1972 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1973 / 2554
    1974 / 2554
    1975 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1976 / 2554
    1977 / 2554
    1978 / 2554
    1979 / 2554
    1980 / 2554
    1981 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1982 / 2554
    1983 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1984 / 2554
    1985 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1986 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1987 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1988 / 2554
    1989 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1990 / 2554
    1991 / 2554
    1992 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    1993 / 2554
    1994 / 2554
    1995 / 2554
    1996 / 2554
    1997 / 2554
    1998 / 2554
    1999 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2000 / 2554
    2001 / 2554
    2002 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2003 / 2554
    2004 / 2554
    2005 / 2554
    2006 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2007 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2008 / 2554
    2009 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2010 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2011 / 2554
    2012 / 2554
    2013 / 2554
    2014 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2015 / 2554
    2016 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2017 / 2554
    2018 / 2554
    2019 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2020 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2021 / 2554
    2022 / 2554
    2023 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2024 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2025 / 2554
    2026 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2027 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2028 / 2554
    2029 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2030 / 2554
    2031 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2032 / 2554
    2033 / 2554
    2034 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2035 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2036 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2037 / 2554
    2038 / 2554
    2039 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2040 / 2554
    2041 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    2042 / 2554
    {'status': '013', 'message': '조회된 데이타가 없습니다.'}
    


```python
columns = ['stock_name', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
div_data = pd.DataFrame(div_data, columns = columns)
EPS_data = pd.DataFrame(EPS_data, columns = columns)

div_data.to_csv('/content/drive/MyDrive/Quant_project/data/주당배당금.csv', encoding = 'euc-kr', index = False)
EPS_data.to_csv('/content/drive/MyDrive/Quant_project/data/주당순이익.csv', encoding = 'euc-kr', index = False)
```


```python

```
