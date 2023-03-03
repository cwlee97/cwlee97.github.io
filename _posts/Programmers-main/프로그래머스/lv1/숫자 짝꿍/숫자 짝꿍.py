def solution(X, Y):
    answer = ''
    x_dic, y_dic = dict(), dict()
    for i in X:
        if i not in x_dic:
            x_dic[i] = 1
        else:
            x_dic[i] += 1
    for j in Y:
        if j not in y_dic:
            y_dic[j] = 1
        else:
            y_dic[j] += 1
    for key in x_dic.keys():
        if key in y_dic:
            answer += key * min(x_dic[key], y_dic[key])
    answer = "".join(sorted(answer, reverse = True))
    if answer == "":
        answer = "-1"
    elif answer.count("0") == len(answer):
        answer = "0"
    return answer