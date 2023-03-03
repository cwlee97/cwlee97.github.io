def solution(survey, choices):
    answer = ''
    temp = dict()
    a = 'RTCFJMAN'
    
    for i in a:
        temp[i] = 0
        
    for i in range(len(survey)):
        score = choices[i] - 4
        if  score < 0:
            temp[survey[i][0]] += abs(score)
        elif score > 0:
            temp[survey[i][1]] += abs(score)
            
    if temp['R'] >= temp['T']:
        answer += 'R'
    else:
        answer += 'T'
    if temp['C'] >= temp['F']:
        answer += 'C'
    else:
        answer += 'F'
    if temp['J'] >= temp['M']:
        answer += 'J'
    else:
        answer += 'M'
    if temp['A'] >= temp['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer