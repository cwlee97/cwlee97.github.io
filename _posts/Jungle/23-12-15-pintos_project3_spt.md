---
layout: single
title: Pintos Project3 1. Implement spt
categories: Jungle
---


3번째 pintos 프로젝트 시작<br>
처음 마주하는 문제는 spt 구현이다.<br>
2번째 pintos 프로젝트를 시작하면서 process.c에 pml4를 자식 프로세스에게 복제하는 등의 작업을 하고, page fault는 구현하지 않을 것이니 exit(-1)을 넣어서 테스트 케이스들을 패스하고 넘어왔다.<br>
이번 프로젝트에서는 pml4만으로는 충분하지 않았던 virtual memory 부분을 보완하여 page fault와 자원을 관리하게 되는 것 같다.<br><br>

## suppplement page table
``` 그래서 spt가 뭔데? ```

위에서 말한 프로젝트의 목적인 page fault, 메모리 관리를 위한 정보를 들고있는 페이지 테이블이다. 기존 우리가 다루었던 pml4(multi level page table)과는 다른 것

stanford의 pintos ppt에는 다음과 같이 묘사되어 있다.

Supplemental Page Table [4.1.4]
Supplements the page table with additional information about each page.
Why not just change page table directly? Limitations on page table format.
Two purposes:
1. On page fault, kernel looks up virtual page in supplemental page table to
find what data should be there.
2. When a process terminates, kernel determines what resources to free.

추가적인 spt에 대한 정보는 구현을 하면서 채워가도록 하겠다.

## Initialize spt
처음으로 고민한 문제는 어떤 자료구조를 사용해서 spt를 구현할 것인가?에 관한 것이다.<br>
이 부분은 팀원과 맞추어 진행하는 것이 좋을 것 같아

1. 배열(array)
2. 연결리스트(linked list)
3. 해시 테이블(Hash table)
4. 비트맵(Bitmap)

중 의견을 구해 해시 테이블 자료구조를 활요해 구현하기로 하였다.

그럼 spt를 초기화하는 작업부터 진행해보자.

thread.h의 thread struct에는 다음과 같이 이미 spt가 선언되어 있다.
```c
#ifdef VM
	/* Table for whole virtual memory owned by thread. */
	struct supplemental_page_table spt;
#endif
```

thread마다 spt를 선언하는 작업은 되어있으니, 이제 spt struct를 구현해보자.
```c
/* vm.h */
/* Representation of current process's memory space.
 * We don't want to force you to obey any specific design for this struct.
 * All designs up to you for this. */
struct supplemental_page_table {
	struct hash spt_hash_table;
};
```

hash table를 사용해 구현하기로 했으니 hash 구조체를 하나 넣어주었다. hash table관련 자료구조는 pintos 프로젝트 내애 이미 구현되어 있으니 include하여 사용하도록 하자

pintos-kaist의 git-book을 보면, page구조체의 va, hash_elem을 활용해 page를 다루는 작업들이 나와있다. 이 부분을 읽고 작업하는것을 추천한다.

```c
/* The representation of "page".
 * This is kind of "parent class", which has four "child class"es, which are
 * uninit_page, file_page, anon_page, and page cache (project4).
 * DO NOT REMOVE/MODIFY PREDEFINED MEMBER OF THIS STRUCTURE. */
struct page {
    ...
    /* Your implementation */
	struct hash_elem hash_elem; /* Hash table element. */
    ...
}
```

제공받은 함수를 사용하기 위해 page sturct에 hash_elem을 추가해주었다.

```c
void
supplemental_page_table_init (struct supplemental_page_table *spt UNUSED) {
	hash_init(&spt->spt_hash_table, page_hash, page_less, NULL);
}
```

첫 구현 함수인 supplemental_page_table_init이다. 선언한 hash table을 넣어주고, page_hash와 page_less는 위에서 말한 git-book에 있는 함수들을 사용하였다.

다음 순서를 찾기 위해 args-none test case를 디버깅해본 결과 vm_alloc_page_with_initializer 함수 구현이 필요했다.