def solution(priorities, location):
    answer = 0
    result = []
    pri= [[priorities[i], i] for i in range(len(priorities))]
    while len(pri) > 1:
        for i in range(1, len(pri)):
            if pri[0][0] < pri[i][0]:
                pri.append(pri.pop(0))
                break
        if pri[0][0] == max(priorities):
            result.append(pri.pop(0))
            priorities.remove(max(priorities))
    result.append(pri[0])
    for i in range(len(result)):
        if result[i][1] == location:
            answer = i + 1
    return answer