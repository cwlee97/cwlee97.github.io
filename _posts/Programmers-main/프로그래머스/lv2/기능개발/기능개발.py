from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses, speeds = deque(progresses), deque(speeds)
    count = 0
    while True:
        if progresses[0] >= 100:
            count += 1
            progresses.popleft()
            speeds.popleft()
            if len(progresses) == 0 and count > 0:
                answer.append(count)
                break
        else:
            if count > 0:
                answer.append(count)
                count = 0
            for i in range(len(progresses)):
                progresses[i]+=speeds[i]
    return answer