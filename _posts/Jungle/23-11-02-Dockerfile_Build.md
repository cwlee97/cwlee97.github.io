

도커 설치 후 DockerFile 빌드 과정입니다.

## Dockerfile
파일명: Dockerfile(확장자 없음!)

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
docker run --security-opt seccomp=unconfined -it <local storage>:/ws --name <container_name> imagename:version
```

```
docker run --security-opt seccomp=unconfined -it -v C:\Users\HP\Desktop\ws\jungle\rbtree:/ws --name rbtree ubuntu:20.04
```

## 실행
1. 시작

```
docker start <container_name>
docker exec -it <container_name>/bin/bash
```

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
$ type -p curl >/dev/null || (apt-get update && apt-get install curl -y)
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update \
    && apt-get install gh -y

$ gh auth login
```

### 명령어 이후 해당 포스팅 참조
https://velog.io/@daelkdev/SOLUTION-GitHub-%ED%86%A0%ED%81%B0-%EA%B4%80%EB%A6%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-gh-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EB%A1%9C%EA%B7%B8%EC%9D%B8

