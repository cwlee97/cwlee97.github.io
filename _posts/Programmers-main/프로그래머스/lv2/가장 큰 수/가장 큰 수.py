def solution(numbers):
    answer = ''
    max_len = 0
    numbers = list(map(str, numbers))
    
    for i in range(len(numbers)):
        numbers[i] = [numbers[i], numbers[i], len(numbers[i])]

    for l in range(len(numbers)):
        if numbers[l][2] != 4:
            while(len(numbers[l][0]) < 4):
                for char in numbers[l][1]:
                    numbers[l][0] += char
                    if len(numbers[l][0]) == 4:
                        break
                        
    numbers.sort(reverse = True)
    for x, y, z in numbers:
        answer += y
    answer = str(int(answer))
    return answer