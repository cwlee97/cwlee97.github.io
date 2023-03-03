def solution(s):
    answer = 0
    if s[0] in ['+', '-']:
        if s[0] == '-':
            answer = int(s[1:]) * -1
        else:
            answer = int(s[1:])
    else:
        answer = int(s)    
    return answer