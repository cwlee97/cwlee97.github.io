def solution(n):
    answer = 0
    if n == 1:
        answer = 1
        return answer
    while n > 0:
        if n % 2 == 1:
            n -= 1
            answer += 1
        else:
            n = n // 2
    return answer