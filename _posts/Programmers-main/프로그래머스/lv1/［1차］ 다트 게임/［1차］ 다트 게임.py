def solution(dartResult):
    answer = []
    result = list(dartResult)
    integer = [str(x) for x in range(0, 10+1)]
    for i in range(len(result)-1):
        
        if result[i] in integer:
            if result[i + 1] in integer:
              result[i + 1] = result[i] + result[i + 1]
              continue
            if result[i + 1] == 'S':
                answer.append(int(result[i]))
            elif result[i + 1] == 'D':
                answer.append(int(result[i]) ** 2)
            elif result[i + 1] == 'T':
                answer.append(int(result[i]) ** 3)
            if i < len(result) - 2:
                if result[i + 2] == '*':
                    if i == 0:
                        answer[-1] = answer[-1] * 2
                    else:
                        answer[-2] = answer[-2] * 2
                        answer[-1] = answer[-1] * 2
                elif result[i + 2] == '#':
                    answer[-1] = answer[-1] * -1
    answer = sum(answer)
    return answer