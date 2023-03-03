def solution(arr1, arr2):
    answer = [[]for _ in range(len(arr1))]
    temp = 0
    column, axis = 0, 0
    while column < len(arr1):
        temp = 0
        for i in range(len(arr2)):
            temp += arr1[column][i] * arr2[i][axis]
        answer[column].append(temp)
        axis += 1
        if axis == len(arr2[0]):
            axis = 0
            column += 1
    return answer