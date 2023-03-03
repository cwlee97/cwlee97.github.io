from math import sqrt, trunc

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        temp = 0
        if i == 1:
            temp += 1
        elif i % 2 == 0:
            for j in range(1, trunc(sqrt(i))+1):
                if i % j == 0:
                    if j ** 2 == i:
                        temp += 1
                    else:
                        temp += 2
        else:
            for j in range(1, trunc(sqrt(i))+2):
                if i % j == 0:
                    if j ** 2 == i:
                        temp += 1
                    else:
                        temp += 2 
        if temp > limit:
            temp = power
        answer += temp
    return answer