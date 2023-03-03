def solution(n):
    answer = 0
    result = ''
    while n > 0:
        n, mod = divmod(n, 3)
        result += str(mod)
    for i in range(len(result)):
        answer += int(result[-(i+1)]) * (3 ** (i))
    return answer