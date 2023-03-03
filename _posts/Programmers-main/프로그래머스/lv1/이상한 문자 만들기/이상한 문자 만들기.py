def solution(s):
    answer = ''
    s = list(map(str, s.split(" ")))
    for i in range(len(s)):
        temp = ''
        for j in range(len(s[i])):
            if j % 2 == 0:
                temp += s[i][j].upper()
            else:
                temp += s[i][j].lower()
        s[i] = temp
    for i in range(len(s)):
        if i == 0:
            answer += s[i]
        else:
            answer += " " + s[i]
    return answer