def solution(numbers, target):
    result = [0]

    for i in range(len(numbers)):
        temp = []
        for j in result:
            temp.append(j + numbers[i])
            temp.append(j - numbers[i])
        result = temp
    result_dic = {x:0 for x in result}
    for x in result:
        result_dic[x] += 1
    answer = result_dic[target]
    return answer