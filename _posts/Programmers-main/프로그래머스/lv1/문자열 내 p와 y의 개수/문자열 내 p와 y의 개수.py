def solution(s):
    answer = True
    s = s.lower()
    count_p, count_y = 0, 0
    
    count_p = s.count('p')
    count_y = s.count('y')
    
    if count_p != count_y:
        answer = False

    return answer