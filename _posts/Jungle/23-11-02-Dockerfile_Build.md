---
layout: single
title: Dockerfile build
categories: Jungle
---

도커 설치 후 DockerFile 빌드 과정입니다.

## Dockerfile
```
From ubuntu:20.04

RUN apt-get update
RUN apt-get install -y gcc make valgrind gdb
RUN apt-get install -y gcc-multilib
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install -y gnupg
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 23F3D4EA75716059
RUN mkdir -p /ws
WORKDIR /ws
```

## DockerFile 빌드
1. docker build
```
docker build -t [이미지 이름:버전] [DockerFile 경로]
```

```
<예시>
docker build -t ubuntu:20.04 C:\Users\HP\Desktop\
```

2. docker run
```
docker run -v <local storage>:/ws --name <image_name> containername:version
```

```
docker run -it -v C:\Users\HP\Desktop\ws\jungle\rbtree:/ws --name ubuntu_20.04 ubuntu:20.04
```

## 실행
1. 시작
```
docker start ubuntu_20.04
docker exec -it ubuntu_20.04 /bin/bash
```

2. 종료
```
$exit
```

## git 설정
```
$ git config --global user.name "<user_id>"
$ git config --global user.email "<user_email>"
```

token 비밀번호 정책관련 오류가 발생한다면 https://shortcuts.tistory.com/12 해당 블로그 포스팅을 참고하여 토근 발급 후 비밀번호 란에 토큰번호 입력<br>
토큰 번호는 발행시에만 확인 가능하므로 저장해두는것을 추천
