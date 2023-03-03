def solution(arr1, arr2):
    answer = []
    column = 0
    while column < len(arr1):
        temp = []
        for i in range(len(arr1[column])):
            temp.append(arr1[column][i] + arr2[column][i])
        answer.append(temp)
        column += 1
    return answer