def solution(num):
    answer, count = 0, 0
    if num == 1:
        return answer
    while True:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        count += 1
        if num == 1:
            answer = count
            break
        if count == 500:
            answer = -1
            break
    return answer