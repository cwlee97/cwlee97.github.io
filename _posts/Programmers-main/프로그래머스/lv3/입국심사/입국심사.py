def solution(n, times):
    answer = 0
    low, high = 0, max(times) * n
    while(True):
        temp = []
        mid = (low + high) // 2
        if low + 1 < high:
            for time in times:
                temp.append(mid // time)
            if sum(temp) > n:
                high = mid
            elif sum(temp) < n:
                low = mid
            else:
                high = mid
        elif low + 1 == high:
            break
        answer = high
    return answer