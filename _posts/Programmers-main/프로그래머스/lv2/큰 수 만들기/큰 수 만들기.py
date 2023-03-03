def solution(number, k):
    answer = ''

    while k > 0:
        pos = 0
        length = len(number) - k
        maximum = 0

        if k >= len(number):
            return answer
        for i in range(len(number) - length + 1):
            if int(number[i]) == 9:
                maximum, pos = 9, i
                break
                
            elif int(number[i]) > maximum:
                maximum, pos = int(number[i]), i
           
        answer += str(maximum)
        number = number[pos+1:]
        if pos != 0:
            k -= pos

    for i in number:
        answer += i
    answer = str(int(answer))
    return answer