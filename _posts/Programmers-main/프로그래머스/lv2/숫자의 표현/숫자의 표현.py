def solution(n):
    answer = 1
    total = 0
    i, j = 1, 0
    while i < n//2+1:
        total += i + j
        if total < n:
            j += 1
        if total == n:
            answer += 1
            i += 1
            j, total = 0, 0
        elif total > n:
            i += 1
            j, total = 0, 0
    return answer