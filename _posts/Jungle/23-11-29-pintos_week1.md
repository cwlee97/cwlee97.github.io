---
layout: single
title: Pintos 1주차 WIL
categories: Jungle
---

## Alarm clock

### Key words
1. busy waits
<hr>

### Problem
1. Busy waiting 코드에서는 ticks만큼 시간이 흐를 때 까지 스레드의 실행 중단
	- while문 내에서 CPU자원을 계속 소비하고 있음

2. 시스템이 idle 상태가 아닌 이상 스레드는 ticks시간 후에 깨어날 필요가 없다?
	- while문을 ticks동안 굴릴 필요가 없음
    - 적절한 시간을 기다린 후에(?) 준비 대기열에 넣기만 하면됨


<hr>

### Solution
1. sleep하는 thread의 wake up time에 대한 정보, sleep하는 thread 저장

2. scheduler에서 current thread의 정보 삭제

3. current thread를 wake up time에 ready_list에 저장

    -> thread_unblock에서 수행하는데, wakeup_ticks에 모든 스레드를 깨워주는 구현 필요

4. 인터럽트 정보를 해당 thread에 다시 넘겨주기


### Implement

1. thread를 재우려면 깨어날 시간을 저장할 구조체 변수와 자고있는 thread를 담은 리스트 필요

    ```c
    /* thread.h */
    struct thread {
        /* Owned by thread.c. */
        tid_t tid;                          /* Thread identifier. */
        enum thread_status status;          /* Thread state. */
        char name[16];                      /* Name (for debugging purposes). */
        int priority;                       /* Priority. */

        /* project alarm*/
        int64_t wakeup_ticks;				/* Wake up Ticks */


    /* thread.c */
    static struct list sleeping_list;

    void
    thread_init (void) {
        list_init (&sleeping_list);
    }

    ```
    <br>

    - 왜 wakeup_ticks 자료형이 int64_t인가?
        - timer.c에서 현재 ticks를 반환하는 timer_ticks()함수의 반환값과 자료형을 맞춤

    <br>


2. thread를 재우는 함수 구현

    - thread를 sleeping list에 wakeup_ticks 기준으로 오름차순으로 정렬하여 삽입

    ```c
    /* thread.c */
    void
    thread_sleep (int64_t ticks) {
        struct thread *curr = thread_current ();
        enum intr_level old_level;

        ASSERT(curr != idle_thread);

        old_level = intr_disable ();

        curr->wakeup_ticks = ticks;

        list_insert_ordered (&sleeping_list, &(curr->elem), dec_function, NULL);
        thread_block ();
        
        intr_set_level (old_level);
    }

    static bool 
    dec_function(const struct list_elem *a, const struct list_elem *b, void *aux) {
        return list_entry(a, struct thread, elem)->wakeup_ticks < list_entry(b, struct thread, elem)->wakeup_ticks;
    }
    ```

    <br>

3. timer_sleep 함수를 기존 Busy waiting 방식에서 sleep & wakeup 형식으로 재구현

    <br>

    ```c
    /* timer.c */
    void
    timer_sleep (int64_t duration) {
        int64_t start = timer_ticks ();
        ASSERT (intr_get_level () == INTR_ON);
        thread_sleep (start + duration);
    }
    ```

    <br>

4. wake up ticks가 된 thread들을 깨우는 함수 구현
    
    * sleeping list 의 맨 앞에는 wake up ticks가 가장 작은 thread가 들어있음
    * front부터 비교하면서 현재 ticks보다 wake up ticks가 큰 경우 iter break

    <br>

    ```c
    /* thread.c */
    void
    thread_wakeup(int64_t ticks) {
        if (list_empty(&sleeping_list))
            return;
        
        while (!list_empty(&sleeping_list)) {
            struct thread *curr = list_entry(list_front(&sleeping_list), struct thread, elem);
            if (curr->wakeup_ticks <= ticks) {
                list_remove(list_front(&sleeping_list));
                thread_unblock(curr);
            } else {
                break;
            }
        }
    }
    ```

    <br>

5. timer interrupt마다 thread_wakeup을 실행하도록 구현

    <br>


    ```c
    /* timer.c */
    timer_interrupt (struct intr_frame *args UNUSED) {
        ticks++;
        thread_tick ();
        thread_wakeup (ticks);
    }
    ```

<hr>

## Priority Scheduling

### Key words

1. priority donation

2. priority inversion

3. Priority inheritance

4. multiple donation

5. nested donation

<hr>

### Problem

1. thread yield는 언제 발생하는가?

2. priority donation은 언제 발생하는가?

3. priority donation이 진행된 thread에서 set_priority함수는 어떻게 동작해야 하는가?

4. donated priority값을 list에 모두 담을 것인가? 최종적으로 받은 donated priority값 만을 저장 할 것인가?

<hr>

### Solution

1. thread yield는 thread_create, set_priority, sema_up에서 발생할 수 있음
    - 말 그대로 '발생할 수' 있으므로 발생이 가능한지 확인이 필요

2. semaphore를 기다리는 waiter