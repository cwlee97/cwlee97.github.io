from collections import deque

def solution(arr):
    answer = []
    arr = deque(arr)
    answer.append(arr[0])
    while (len(arr) > 0):
        temp = arr.popleft()
        if len(arr) == 0:
            break
        if temp == arr[0]:
            pass
        else:
            temp = arr[0]
            answer.append(temp)
    return answer