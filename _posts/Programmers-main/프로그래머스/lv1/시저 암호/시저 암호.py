def solution(s, n):
    answer = ''
    s = list(s)
    Upper = [chr(x) for x in range(90, 64, -1)]
    Lower = [chr(x) for x in range(122, 96, -1)]
    
    for i in range(len(s)):
        if s[i] in Upper:
            s[i] = Upper[Upper.index(s[i]) - n]
        elif s[i] in Lower:
            s[i] = Lower[Lower.index(s[i]) - n]
    for i in s:
        answer += i
    return answer