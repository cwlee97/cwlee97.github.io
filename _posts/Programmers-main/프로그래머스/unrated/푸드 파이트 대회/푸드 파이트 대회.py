def solution(food):
    answer = ''
    for i in range(1, len(food)):
        num = food[i] // 2
        for j in range(num):
            answer += "{}".format(i)
    temp = answer[::-1]
    answer = answer + '0' + temp
    return answer