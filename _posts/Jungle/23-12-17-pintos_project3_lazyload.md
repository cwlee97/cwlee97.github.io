---
layout: single
title: Pintos Project3 1. Implement anonymous page
categories: Jungle
---

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

static bool
lazy_load_segment (struct page *page, void *aux) {
	/* TODO: Load the segment from the file */
	/* TODO: This called when the first page fault occurs on address VA. */
	/* TODO: VA is available when calling this function. */
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
    bool valid_bit;
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
		file_info->valid_bit = false;

		void *aux = (void *)file_info;

		if (!vm_alloc_page_with_initializer (VM_ANON, upage,
					writable, lazy_load_segment, aux))
			return false;
```

load_segment에서 aux 인자를 넘겨주는 부분을 위와 같이 수정해주고,
