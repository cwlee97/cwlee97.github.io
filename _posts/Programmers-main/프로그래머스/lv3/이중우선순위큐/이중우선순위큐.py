def solution(operations):
    answer = []
    for i in operations:
        x, y = map(str, i.split(" "))
        if x == "I":
            answer.append(int(y))
        else:
            if y == '1' and len(answer) > 0:
                answer.remove(max(answer))
            elif y == '-1' and len(answer) > 0:
                answer.remove(min(answer))
    if len(answer) == 0:
        answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]
    return answer