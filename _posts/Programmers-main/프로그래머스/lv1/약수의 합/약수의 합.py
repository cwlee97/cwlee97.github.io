def solution(n):
    answer = n
    if n > 1:
        for i in range(1, n//2 + 2):
            if n % i == 0:
                answer += i
    return answer