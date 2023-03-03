def solution(x, y, n):
    answer = 0
    listt = [y]
    while x not in listt:
        temp = []
        for i in listt:
            if i % 3 == 0:
                temp.append(i / 3)
            if i % 2 == 0:
                temp.append(i / 2)
            if i-n >= x:
                temp.append(i-n)
        answer += 1
        listt = temp
        if len(temp) == 0:
            answer = -1
            break
    return answer