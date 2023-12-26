---
layout: single
title: Pintos Project3 Mmap & Munmap
categories: Jungle
---

## mmap()

이번 구현 순서는 file backed page의 mmap, munmap이다. mmap은 이전에 process.c에 구현했던 load_segment와 비슷한 역할을 하고, lazy_loading방식을 사용하기에 mmap을 위한 lazy_load function도 필요했다.
먼저 system call에서 입력 인자의 validation을 판단하고, do_mmap을 호출해 진행하는 방식으로 구현하였다. 검증하는 기준은 git book과 test case를 종합하여 적어두었다.

```c
void *
mmap (void *addr, size_t length, int writable, int fd, off_t offset) {
	struct thread *curr = thread_current();
	struct file *file = curr->fd_table[fd];

	// mmap may fail if the file opened as fd has a length of zero bytes.
	if (file == NULL || file_length(file) == 0 || is_kernel_vaddr(addr)) {
		return NULL;
	}
	
	// It must fail if addr is not page-aligned or 
	// if the range of pages mapped overlaps any existing set of mapped pages
	if (addr != pg_round_down(addr) || spt_find_page(&curr->spt, pg_round_down(addr+length))) {
		return NULL;
	}

	// if addr is 0, it must fail, because some Pintos code assumes virtual page 0 is not mapped
	// mmap should also fail when length is zero.
	if (addr == 0 || (long)length <= 0 || is_kernel_vaddr((size_t)addr + length)) {
		return NULL;
	}

	// validate mmap over stack segment and offset value
	if (offset != pg_round_down(offset) || file_length(file) <= offset || spt_find_page(&thread_current()->spt, addr)) {
		return NULL;
	}	

	// the file descriptors representing console input and output are not mappable.
	if (fd <= 1 || fd > FD_MAX) {
		return NULL;
	}
	
	return do_mmap(addr, length, writable, file, offset);
}
```

```c
/* Do the mmap */
void *
do_mmap (void *addr, size_t length, int writable,
		struct file *file, off_t offset) {
	// length bytes the file open as fd starting from offset byte 
	// into the process's virtual address space at addr

	// You should use the file_reopen function to obtain a separate and 
	// independent reference to the file for each of its mappings
	struct file *reopen_file = file_reopen(file);
	if (reopen_file == NULL) {
        return NULL;
    }

	// Memory-mapped pages should be also allocated in a lazy manner 
	// just like anonymous pages. 
	// You can use vm_alloc_page_with_initializer or 
	// vm_alloc_page to make a page object.
	size_t read_bytes = file_length(reopen_file) < length ? file_length(reopen_file) : length;
	size_t zero_bytes = file_length(reopen_file) < length ? pg_round_up(length) - file_length(reopen_file) : PGSIZE - (length % PGSIZE);
	void *upage = addr;

	while (read_bytes > 0 || zero_bytes > 0) {
		/* Do calculate how to fill this page.
		 * We will read PAGE_READ_BYTES bytes from FILE
		 * and zero the final PAGE_ZERO_BYTES bytes. */
		size_t page_read_bytes = read_bytes < PGSIZE ? read_bytes : PGSIZE;
		size_t page_zero_bytes = PGSIZE - page_read_bytes;

		/* TODO: Set up aux to pass information to the lazy_load_segment. */
		struct mmap_info *aux  = (struct mmap_info *)malloc(sizeof(struct mmap_info));
		if (aux == NULL) {
			return false;
		}

		aux->file = reopen_file;
		aux->ofs = offset;
		aux->read_bytes = page_read_bytes;
		aux->length = length;

		if (!vm_alloc_page_with_initializer (VM_FILE, upage,
					writable, mmap_lazy_load, aux)) {
						file_close(reopen_file);
						free(aux);
						return false;
					}

		/* Advance. */
		read_bytes -= page_read_bytes;
		zero_bytes -= page_zero_bytes;
		upage += PGSIZE;
		offset += PGSIZE;
	}
	return addr;
}
```

구현한 mmap은 위와 같은데, 대부분의 코드는 load_segment함수와 비슷하지만, git book에서 권장한 reopen을 사용하였고 file length와 입력 인자 length를 비교하여 read byte를 설정하는 부분이 추가되었다.


## mmap lazy load function
해당 함수를 구현하면서 이전 uninit page의 lazy load와 큰 차이는 mmap을 통해 여러 페이지를 연속적으로 할당받는 경우가 추가되었다는 것인데, 이를 위해 file_page 구조체에 list_elem을 추가하여 생성된 페이지들을 관리할 수 있는 리스트를 thread struct에 넣어주었다.

file_read_at함수를 사용해서 여러 테스트 케이스를 쉽게 넘어간 것을 확인했던 기억이 있는데, file_read를 통해 file의 pos값이 변경되어 해당 함수를 사용한 다른 분들은 pos값 설정이 잘못되어 실패한 케이스들이 있었다.

```c
static bool
mmap_lazy_load (struct page *page, void *aux) {
	/* TODO: Load the segment from the file */
	/* TODO: This called when the first page fault occurs on address VA. */
	/* TODO: VA is available when calling this function. */
	struct mmap_info *mmap_info = (struct mmap_info *)aux;
	struct file_page *file_page = &page->file;
	list_push_back(&(thread_current()->mmap_info_list), &(file_page->file_elem));
	
	off_t res = file_read_at (mmap_info->file, page->va, 
					mmap_info->read_bytes, mmap_info->ofs);

	if (res != mmap_info->read_bytes) {
		return false;
	}

	memset((char *)page->va + mmap_info->read_bytes, 0, PGSIZE-mmap_info->read_bytes);

	file_page->page = page;
	file_page->file = mmap_info->file;
	file_page->ofs = mmap_info->ofs;
	file_page->read_bytes = mmap_info->read_bytes;
	file_page->length = mmap_info->length;

	pml4_set_dirty(thread_current()->pml4, page->va, false);
	free(aux);

	return true;
}
```

## munmap

munmap의 경우는 크게 문제가 된 적이 없었다. 코드 내용에 있어서도 어려운 부분이 없으니 넘어가자.

```c
/* Do the munmap */
void
do_munmap (void *addr) {
	// all pages written to by the process are written back to the file
	// pages not written must not be
	// The pages are then removed from the process's list of virtual pages.
	struct thread *curr = thread_current();
	struct page *page = spt_find_page(&curr->spt, addr);
	struct file_page *file_page = &page->file;
	struct file *file = file_page->file;
	void *upage = addr;

	uint32_t write_bytes = 0;
	uint32_t length = file_page->length;

	while (write_bytes < length) {
        struct page *m_page = spt_find_page(&curr->spt, upage);
		struct file_page *m_file_page = &m_page->file;

        if (pml4_is_dirty(curr->pml4, upage)) {
			file_write_at(m_file_page->file, upage, m_file_page->read_bytes, m_file_page->ofs);
		}

        hash_delete(&(curr->spt), &(m_page->page_elem));
        spt_remove_page(&curr->spt, m_page);

        upage += PGSIZE;
		write_bytes += PGSIZE;
    }

	file_close(file);
}

```

## file_backed_destroy

mmap -> close -> read의 작업이 이루어지면 munmap의 write back이 없어 read시에 buffer가 비어있는 테스트 케이스가 있었다. 그렇다면 어디서 처리해야할지 고민하던 중 supplemental_page_table_kill -> hash_clear -> spt_destroy -> vm_dealloc_page -> destroy(file_backed_destroy)로 이어지는 과정에서 write back을 하면 되지 않을까 하는 의견을 다른 정글러분에게 받아 해결했던 함수이다.

```c
/* Destory the file backed page. PAGE will be freed by the caller. */
static void
file_backed_destroy (struct page *page) {
	struct file_page *file_page = &page->file;
	struct thread *curr = thread_current();

	if (pml4_is_dirty(curr->pml4, page->va)) {
		file_write_at(file_page->file, page->va, file_page->read_bytes, file_page->ofs);
		pml4_set_dirty(thread_current()->pml4, page->va, false);
	}

	if (page->frame != NULL) {
		free(page->frame);
	}

}
```
