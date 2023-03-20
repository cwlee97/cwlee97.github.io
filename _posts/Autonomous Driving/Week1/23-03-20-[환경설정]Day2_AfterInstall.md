---
layout: single
title: 설치 후 작업
categories: Autonomous_Driving_course
---

이번에는 우분투 설치 후 쾌적한 사용을 위해 몇 가지 설치들을 진행해보고자 한다.
1. open vm tools 설치
    * 해당 과정은 화면 크기 및 다른 설정들을 가능하게 해준다. VMWare 설치 후 우분투 창을 보면 크기 설정은 반드시 필요하다는 생각이 들 것이다. 
2. Daily 서비스 Disabled로 전환
    * daily로 실행되는 패키지 유지보수 서비스는 가상 시스템 사용시, 시스템의 기동을 느리게 하거나 펜딩이 걸리게 한다. 해당 서비스를 끄는 법을 알아보도록 하자.
3. root 유저 암호 설정

# open vm tools
해당 툴에서 제공하는 기능에 대해 알아보자
<table class="table">
<thead><tr>
<th>제공 기능</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>화면 조절</td>
<td>화면 크기의 조절이 가능해지며, 그래픽 가속으로 속도를 빠르게 한다.</td>
</tr>
<tr>
<td>클립 보드</td>
<td>윈도에서 "CTRL-C"로 복사한 텍스트를 리눅스에서 "Shift-Insert"로 붙이기가 가능하며,<br> 반대로 리눅스에서 복사한 텍스트는 윈도우에서 "CTRL-V"로 붙이기가 가능하다.</td>
</tr>
<tr>
<td>파일 복사</td>
<td>윈도우 탐색기에서 파일을 끌어다가 X Window에 넣으면 복사가 된다.<br>
단, 드래그한 뒤에 바로 놓지 말고, 잠깐 기다렸다가 '+'기호가 보일 때 놓아야 한다.</td>
</tr>
</tbody>
</table>

설치 방법은 터미널에
```
sudo apt install open-vm-tools{,-desktop}
```
을 입력하자.<br><br>

# 데일리 서비스 비활성화
## 패키지 자동 관리 유닛, 타이머를 비활성화 한다.

<table class="table">
<thead><tr>
<th>Unit 이름</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>apt-daily.service</td>
<td>데일리 패키지 관리 서비스</td>
</tr>
<tr>
<td>apt-daily.timer</td>
<td>타이머(동명의 unit을 주기적으로 자동실행하도록 하는 기능)</td>
</tr>
<tr>
<td>apt-daily-upgrade.service</td>
<td>데일리 패키지 업그레이드 관리 서비스</td>
</tr>
<tr>
<td>apt-daily-upgrade.timer</td>
<td>타이머(동명의 unit을 주기적으로 자동실행하도록 하는 기능)</td>
</tr>
</tbody>
</table>

위 표에서 두 개의 타이머 기능을 비활성화 할 것이다.
Ubuntu 터미널 창에 다음 명령어를 입력해주자.
```
$ sudo systemctl disable --now apt-daily.timer
$ sudo systemctl disable --now apt-daily-upgrade.timer
```
비활성화가 잘 이루어졌는지 다음 명령어를 통해 disabled/ inactive상태인지 확인해보자.
```
$ sudo systemctl status apt-daily.timer
$ sudo systemctl status apt-daily-upgrade.timer
```

# Root 유저 암호 설정
```
$ sudo passwd
```
명령어를 사용하면 루트 유저 암호를 설정할 수 있다.
이후
```
$ su -
```
위의 명령어를 통해 변경한 루트 유저 암호를 입력하면 root@로 바뀌며 루트 유저로 교체된 것을 확인할 수 있다.

# VMWare Setting

## VT : 가상화 가속 기능(활성화 해야만 VMWare가 빨라진다.)
### Windows10의 VT 활성화 확인 방법
1. cmd에서 powershell 실행
2. systeminfo 명령어 실행

* Hypter-V 요구 사항 항목이 모두 "예"로 되어있으면 켜져있는 상태이다.
* BIOS에서 off로 되어있다면 펌웨어에 가상화 사용이 아니오로 표시된다.

### VT 설정은 2가지 단계를 거친다.
1. BIOS에서 VT기능이 enabled로 되어있어야 한다.
2. VMWare 소프트웨어의 VM세팅의 Processor에서도 켜줘야 한다.
