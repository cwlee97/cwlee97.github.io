def solution(n):
    answer = ''
    char = ['수', '박']
    for i in range(n):
        answer += char[i%2]
    return answer