def solution(x):
    answer = True
    ele_sum = 0
    y = str(x)
    for i in y:
        ele_sum += int(i)
    if x % ele_sum != 0:
        answer = False
    return answer