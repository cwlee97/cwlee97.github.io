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

/* Returns a hash value for page p. */
unsigned
page_hash (const struct hash_elem *p_, void *aux UNUSED) {
  const struct page *p = hash_entry (p_, struct page, page_elem);
  return hash_bytes (&p->va, sizeof p->va);
}

/* Returns true if page a precedes page b. */
bool
page_less (const struct hash_elem *a_,
           const struct hash_elem *b_, void *aux UNUSED) {
  const struct page *a = hash_entry (a_, struct page, page_elem);
  const struct page *b = hash_entry (b_, struct page, page_elem);

  return a->va < b->va;
}

/* Returns the page containing the given virtual address, or a null pointer if no such page exists. */
/* Find VA from spt and return page. On error, return NULL. */
struct page *
spt_find_page (struct supplemental_page_table *spt UNUSED, void *va UNUSED) {
	struct page *page;
	/* TODO: Fill this function. */
	struct hash_elem *e;

	page->va = va;
	e = hash_find (&spt->spt_ht, &page->page_elem);
	return e != NULL ? hash_entry (e, struct page, page_elem) : NULL;
}

/* Insert PAGE into spt with validation. */
bool
spt_insert_page (struct supplemental_page_table *spt UNUSED,
		struct page *page UNUSED) {
	/* TODO: Fill this function. */
	return hash_insert (&spt->spt_ht, &page->page_elem) ? true : false;
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

## vm_alloc_page_with_initializer

다음 순서를 찾기 위해 args-none test case를 디버깅해본 결과 vm_alloc_page_with_initializer 함수 구현이 필요했다.<br>
해당 함수에 대한 구현 설명은 gitbook - Anonymous page 부분에 실려 있다.

Implement vm_alloc_page_with_initializer(). You should fetch an appropriate initializer according to the passed vm_type and call uninit_new with it.

```c
bool vm_alloc_page_with_initializer (enum vm_type type, void *va,
        bool writable, vm_initializer *init, void *aux);
```

Create an uninitialized page with the given type. The swap_in handler of uninit page automatically initializes the page according to the type, and calls INIT with given AUX. Once you have the page struct, insert the page into the process's supplementary page table. Using VM_TYPE macro defined in vm.h can be handy.


The page fault handler follows its call chain, and finally reaches uninit_intialize when it calls swap_in. We gives the complete implementation for it. Although, you may need to modify the uninit_initialize according to your design.

먼저 함수에서 입력으로 받은 인자들에 대해 살펴보자.

1. type

	virtual memory type에 관한 열거형 변수이다. 
	```c
	enum vm_type {
		/* page not initialized */
		VM_UNINIT = 0,
		/* page not related to the file, aka anonymous page */
		VM_ANON = 1,
		/* page that realated to the file */
		VM_FILE = 2,
		/* page that hold the page cache, for project 4 */
		VM_PAGE_CACHE = 3,

		/* Bit flags to store state */

		/* Auxillary bit flag marker for store information. You can add more
		* markers, until the value is fit in the int. */
		VM_MARKER_0 = (1 << 3),
		VM_MARKER_1 = (1 << 4),

		/* DO NOT EXCEED THIS VALUE. */
		VM_MARKER_END = (1 << 31),
	};
	```

	각 상수들에 대한 설명은 주석으로 잘 나타나 있는 듯 하다.

2. upage

	새로운 페이지가 할당 될 가상 주소
3. writable

	페이지 쓰기 권한에 대한 값
4. init

	페이지를 초기화하는 데 사용할 함수

새로 page를 만들어 spt에 추가하면 되는데, 해당 함수 구현만으로는 아직 initializer부분이 부족한 것 같다. 첫 번째 문제는 함수에 인자로 들어오는 vm_initializer - lazy_load_segment가 구현이 되어있지 않다. 이 부분부터 이어나가자.

```c
/* Create the pending page object with initializer. If you want to create a
 * page, do not create it directly and make it through this function or
 * `vm_alloc_page`. */
bool
vm_alloc_page_with_initializer (enum vm_type type, void *upage, bool writable,
		vm_initializer *init, void *aux) {

	ASSERT (VM_TYPE(type) != VM_UNINIT)

	struct supplemental_page_table *spt = &thread_current ()->spt;

	/* Check wheter the upage is already occupied or not. */
	if (spt_find_page (spt, upage) == NULL) {
		/* TODO: Create the page, fetch the initialier according to the VM type,
		 * TODO: and then create "uninit" page struct by calling uninit_new. You
		 * TODO: should modify the field after calling the uninit_new. */
		struct page *new_page = (struct page *)malloc(sizeof(struct page));;
		if (new_page == NULL)
            goto err;

		void *va = pg_round_down(upage);

		switch (VM_TYPE(type)) {
            case VM_ANON:
                uninit_new(new_page, va, init, type, aux, anon_initializer);
                break;
            case VM_FILE:
                uninit_new(new_page, va, init, type, aux, file_backed_initializer);
                break;
            default:
                NOT_REACHED();
                break;
        }

		/* TODO: Insert the page into the spt. */
		if (!spt_insert_page(spt, new_page)) {
			goto err;
		}
	}
	return true;
err:
	return false;
}
```