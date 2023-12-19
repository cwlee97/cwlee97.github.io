---
layout: single
title: Pintos Project3 1. Lazy load
categories: Jungle
---

## load segment
```c
static bool
load_segment (struct file *file, off_t ofs, uint8_t *upage,
		uint32_t read_bytes, uint32_t zero_bytes, bool writable) {
	ASSERT ((read_bytes + zero_bytes) % PGSIZE == 0);
	ASSERT (pg_ofs (upage) == 0);
	ASSERT (ofs % PGSIZE == 0);

	while (read_bytes > 0 || zero_bytes > 0) {
		/* Do calculate how to fill this page.
		 * We will read PAGE_READ_BYTES bytes from FILE
		 * and zero the final PAGE_ZERO_BYTES bytes. */
		size_t page_read_bytes = read_bytes < PGSIZE ? read_bytes : PGSIZE;
		size_t page_zero_bytes = PGSIZE - page_read_bytes;

		/* TODO: Set up aux to pass information to the lazy_load_segment. */
		void *aux = NULL;
		if (!vm_alloc_page_with_initializer (VM_ANON, upage,
					writable, lazy_load_segment, aux))
			return false;

		/* Advance. */
		read_bytes -= page_read_bytes;
		zero_bytes -= page_zero_bytes;
		upage += PGSIZE;
	}
	return true;
}
```

lazy load에서 사용할 aux인자부터 시작해보자.<br>
```c
/* project 3 */
struct file_info {
    struct file *file;
    off_t ofs;
    uint32_t read_bytes;
    bool writable;
}
```

aux에 사용할 file_info 구조체를 만들어보았다. 이는 임시이며 작성하면서 필요한 정보는 추가하며 진행할 것이다.

```c
/* TODO: Set up aux to pass information to the lazy_load_segment. */
		struct file_info *file_info  = (struct file_info *)malloc(sizeof(struct file_info);
		if (file_info == NULL) {
			return false;
		}

		file_info->file = file;
		file_info->ofs = ofs;
		file_info->read_bytes = read_bytes;
		file_info->writable = writable;

		void *aux = (void *)file_info;

		if (!vm_alloc_page_with_initializer (VM_ANON, upage,
					writable, lazy_load_segment, aux))
			return false;
		
		/* Advance. */
		read_bytes -= page_read_bytes;
		zero_bytes -= page_zero_bytes;
		upage += PGSIZE;
		ofs += page_read_bytes;
```

## lazy_load_segment

```c
/* TODO: Load the segment from the file */
/* TODO: This called when the first page fault occurs on address VA. */
/* TODO: VA is available when calling this function. 
```

PF가 처음으로 발생할 때 va주소에서 호출되며, 이 함수를 거쳐 va는 사용가능하게 된다고 나와있다.

#### va를 사용 가능하게 하는 법은 무엇인가?

1. file의 segment(data, metadata)를 읽어 물리 메모리에 로드
2. 해당 페이지의 va, pa 정보를 페이지 테이블에 매핑

#### 여기서 file에 대한 페이지를 찾지 않고 바로 disk에서 segment를 로드하는 이유는 뭘까?

lazy load는 vm_alloc_page_with_initializer함수에서 호출이 된다. 이는 새로 페이지를 할당하는 함수.

Lazy load의 주요 특징은 필요한 시점에만 데이터를 로드하고, 그 이전까지는 디스크에서 읽어오지 않는다는 것. 이를 통해 메모리 사용을 최적화할 수 있다.

따라서, 처음 페이지 폴트가 발생했을 때, 바로 디스크에서 세그먼트를 로드하지 않고, 세그먼트의 데이터와 메타데이터를 파일에서 읽어와 메모리에 올리는 작업은 나중에 실제로 그 페이지에 접근할 때까지 미루어짐. 이것이 lazy load의 핵심 아이디어. 페이지 폴트가 발생하면 해당 페이지를 디스크에서 읽어와 메모리에 로드하고, 페이지 테이블을 업데이트하여 가상 주소와 물리 주소 간의 매핑을 수행.

이러한 방식을 통해 시스템은 실제로 필요한 데이터만을 메모리에 로드하고, 불필요한 디스크 I/O를 최소화하여 효율적으로 메모리를 관리할 수 있다.

```c
/* From here, codes will be used after project 3.
 * If you want to implement the function for only project 2, implement it on the
 * upper block. */

static bool
lazy_load_segment (struct page *page, void *aux) {
	/* TODO: Load the segment from the file */
	/* TODO: This called when the first page fault occurs on address VA. */
	/* TODO: VA is available when calling this function. */
	// Lazy load의 주요 특징은 필요한 시점에만 데이터를 로드하고,
	// 그 이전까지는 디스크에서 읽어오지 않는다는 것
	// 이를 통해 메모리 사용을 최적화할 수 있다.
	struct file_info *file_info = (struct file_info *)aux;

	// 페이지 폴트가 발생하면 해당 페이지를 디스크에서 읽어와 
	// 메모리에 로드하고, 페이지 테이블을 업데이트하여 
	// 가상 주소와 물리 주소 간의 매핑을 수행
	off_t res = file_read_at (file_info->file, page->va, 
					file_info->read_bytes, file_info->ofs);
	memset((char *)page->va + file_info->read_bytes, 0, PGSIZE-file_info->read_bytes);

	if (res != file_info->read_bytes) {
		return false;
	}

	return true;
}
```

## setup_stack
이번 포스팅에서는 process.c에서 남은 함수인 setup_stack까지 구현할 것이다.

vm project 이전에 사용했던 setup_stack에 대해 살펴보자

```c
/* Create a minimal stack by mapping a zeroed page at the USER_STACK */
static bool
setup_stack (struct intr_frame *if_) {
	uint8_t *kpage;
	bool success = false;

	kpage = palloc_get_page (PAL_USER | PAL_ZERO);
	if (kpage != NULL) {
		success = install_page (((uint8_t *) USER_STACK) - PGSIZE, kpage, true);
		if (success)
			if_->rsp = USER_STACK;
		else
			palloc_free_page (kpage);
	}
	return success;
}

static bool
install_page (void *upage, void *kpage, bool writable) {
	struct thread *t = thread_current ();

	/* Verify that there's not already a page at that virtual
	 * address, then map our page there. */
	return (pml4_get_page (t->pml4, upage) == NULL
			&& pml4_set_page (t->pml4, upage, kpage, writable));
}
```

1. kpage에 user영역의 0으로 초기화 된 페이지를 할당
2. user_stack-pgsize(rsp라 칭하자)가 unmapped 상태인지 확인
3. rsp에 kpage를 mapping
4. 성공시 rsp를 위의 rsp로 업데이트

```c
/* Create a PAGE of stack at the USER_STACK. Return true on success. */
static bool
setup_stack (struct intr_frame *if_) {
	bool success = false;
	void *stack_bottom = (void *) (((uint8_t *) USER_STACK) - PGSIZE);

	/* TODO: Map the stack on stack_bottom and claim the page immediately.
	 * TODO: If success, set the rsp accordingly.
	 * TODO: You should mark the page is stack. */
	/* TODO: Your code goes here */
    return success;
}
```

#### 이번에 구현할 함수와 차이는 뭘까?
- palloc, malloc

	이번 구현에 page는 palloc이 아닌 malloc으로 구현하였다. 이유는 페이지 할 수 없는 곳에 이들을 위치시킴으로써
	접근하는 과정에서 페이지 폴트가 발생할 확률을 줄여 설계를 간소화 할 수 있다는 gitbook의 의견 때문이다.

그럼 이제 새로운 kpage를 만들어야 하는데 pintos에서 제시한 방법은 두 가지가 있다.
1. vm_alloc_page_with_initializer
2. vm_alloc_page

1번 방법은 우리가 구현한 함수이니 설명은 생략하고, vm_alloc_page에 대해 알아보고 결정하자.

```c
#define vm_alloc_page(type, upage, writable) \
	vm_alloc_page_with_initializer ((type), (upage), (writable), NULL, NULL)
```

vm.h 헤더 파일에 정의된 매크로 함수인데, 결국 vm_alloc_page_with_initializer를 사용하는것은 똑같다. 그 뒤에 lazy_load나 aux인자를 NULL로 처리하는 부분만 바뀌어 있다.

불필요한 부분은 넣지 않는것이 좋으니 2번 방식을 채택하여 구현한 stack_setup함수는 다음과 같다.

```c
/* Create a PAGE of stack at the USER_STACK. Return true on success. */
static bool
setup_stack (struct intr_frame *if_) {
	bool success = false;
	void *stack_bottom = (void *) (((uint8_t *) USER_STACK) - PGSIZE);

	/* TODO: Map the stack on stack_bottom and claim the page immediately.
	 * TODO: If success, set the rsp accordingly.
	 * TODO: You should mark the page is stack. */
	/* TODO: Your code goes here */
	success = vm_alloc_page(VM_ANON, stack_bottom, true);
    if (success) {
        struct page *page = spt_find_page(&thread_current()->spt, stack_bottom);

        if (vm_claim_page(stack_bottom))
            if_->rsp = USER_STACK;
    }

    return success;
}
```