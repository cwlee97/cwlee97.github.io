def solution(s):
    answer = ''
    s = list(map(int,s.split(" ")))
    max_num = max(s)
    min_num = min(s)
    answer += str(min_num) + " " + str(max_num)
    return answer