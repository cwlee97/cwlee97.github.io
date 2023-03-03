def solution(s):
    answer = ''
    s = list(s)
    for i in range(len(s)):
        s[i] = ord(s[i])
    s.sort(reverse = True)
    
    for i in range(len(s)):
        s[i] = chr(s[i])
        answer += s[i]
    return answer