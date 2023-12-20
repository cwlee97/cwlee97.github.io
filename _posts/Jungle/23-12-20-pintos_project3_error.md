---
layout: single
title: Pintos Project3 Error
categories: Jungle
---

본 포스팅은 프로젝트 3 - vm 진행 간 발생한 오류에 대해 적어둘 생각이다.

1. vm_get_frame -> palloc_get_page error
```bash
Translation of call stack:
0x000000800421857c: debug_panic (lib/kernel/debug.c:32)
0x000000800420d44a: pml4_activate (threads/mmu.c:206)
0x000000800421c2d1: process_activate (userprog/process.c:354)
0x0000008004207e84: schedule (threads/thread.c:705)
0x0000008004207d36: do_schedule (threads/thread.c:673)
0x0000008004207390: thread_yield (threads/thread.c:360)
0x000000800420954f: intr_handler (threads/interrupt.c:375)
0x0000008004209816: intr_entry (threads/intr-stubs.o:?)
0x000000800420bc53: palloc_get_multiple (threads/palloc.c:278)
0x000000800420bcbb: palloc_get_page (threads/palloc.c:297)
0x0000008004221467: vm_get_frame (vm/vm.c:172)
0x00000080042217a1: vm_do_claim_page (vm/vm.c:271)
0x00000080042216d9: vm_try_handle_fault (vm/vm.c:249)
0x000000800421d391: page_fault (userprog/exception.c:148)
0x00000080042093f8: intr_handler (threads/interrupt.c:352)
0x0000008004209816: intr_entry (threads/intr-stubs.o:?)
0x000000800421c837: load (userprog/process.c:548 (discriminator 3))
0x000000800421c01d: process_exec (userprog/process.c:248)
0x000000800421bc23: initd (userprog/process.c:81)
0x0000008004207863: kernel_thread (threads/thread.c:514)
```

본 back trace 결과만 보고 당연히 get_frame, do_claim_page에 문제가 있는줄알고 하루를 해당 내용을 디버깅하는데 보냈다.
최종적으로 다른 분들의 코드와 비교하는 작업을 거치고 있었는데, 

```c
vm_do_claim_page(struct page *page) {
    ...
    /* Insert page table entry to map page's VA to frame's PA - implemented project 3 */
	
	// Error 1
	// pml4_set_page(&curr->pml4, page->va, frame->kva, page->writable);
	if (pml4_set_page(curr->pml4, page->va, frame->kva, page->writable) == false)
        return false;

    ...
}
```

위 코드 작업으로 해당 에러를 벗어났다. 체크해보니 pml4_set_page의 bool값이 false인 곳이 없었는데 말이다. 매번 프로젝트를 진행하면서 느끼지만 함수 인자를 잘보자...

2. thread name 사라짐
초기 테스트들에서 

```bash
Acceptable output:
  (args) begin
  (args) argc = 2
  (args) argv[0] = 'args-single'
  (args) argv[1] = 'onearg'
  (args) argv[2] = null
  (args) end
  args-single: exit(0)
Differences in `diff -u' format:
  (args) begin
  (args) argc = 2
  (args) argv[0] = 'args-single'
  (args) argv[1] = 'onearg'
  (args) argv[2] = null
  (args) end
- args-single: exit(0)
+ : exit(0)
```

분명 스레드를 만들어줄 때 디버깅을 모두 했음에도 exit system call에서 스레드 이름을 못찾는 상황이었다.
thread_current()의 name을 모든 함수에서 디버깅하며 어느 함수에서 지워지는지 테스트를 해보았는데, spt_find_page 전, 후로 thread_name에 쓰레기값이 들어가는 현상을 확인해서 디버깅하는 과정에서 해결이 되었다.

문제는 이 해결이 된 과정이다.
```c
/* Returns the page containing the given virtual address, or a null pointer if no such page exists. */
/* Find VA from spt and return page. On error, return NULL. */
struct page *
spt_find_page (struct supplemental_page_table *spt, void *va) {
	// struct thread *t = thread_current();
	struct page *page;
	/* Find page in supplement page table - implemented project 3 */
	struct hash_elem *e;

	page->va =  pg_round_down(va);
	struct thread *t_2 = thread_current();
	e = hash_find (&spt->spt_ht, &page->page_elem);
	return e != NULL ? hash_entry (e, struct page, page_elem) : NULL;
}
```

위 함수에서 디버깅을 위해 쓴 struct thread *t = thread_current();를 추가하게 되면 쓰레기 값이 덮어씌워지는 과정이 사라진다. 해당 함수에서는 스레드 구조체에 대한 정보가 전혀 필요하지 않은데 이유가 뭘까?
개인적인 뇌피셜로는 초기화되지 않은 page를 사용하는 과정에서 thread의 name부분의 메모리를 사용한 것 같다는 생각으로 malloc & free를 사용해 메모리를 사용한 결과 뇌피셜이 맞았다.

```c
/* Returns the page containing the given virtual address, or a null pointer if no such page exists. */
/* Find VA from spt and return page. On error, return NULL. */
struct page *
spt_find_page (struct supplemental_page_table *spt, void *va) {
	struct page *page = (struct page *)malloc(sizeof(struct page));
	/* Find page in supplement page table - implemented project 3 */
	struct hash_elem *e;

	page->va =  pg_round_down(va);
	e = hash_find (&spt->spt_ht, &page->page_elem);

	free(page);
	return e != NULL ? hash_entry (e, struct page, page_elem) : NULL;
}
```