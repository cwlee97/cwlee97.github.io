def solution(array, commands):
    answer = []
    for x, y, z in commands:
        temp_arr = array[x-1:y]
        temp_arr.sort()
        answer.append(temp_arr[z-1])
    
    return answer