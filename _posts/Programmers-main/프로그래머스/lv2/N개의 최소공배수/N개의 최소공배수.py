def solution(arr):
    answer = 0
    count = 1
    while True:
        answer = max(arr) * count
        temp = []
        for num in arr:
            if answer % num != 0:
                count += 1
                break
            else:
                temp.append(num)
        if len(temp) == len(arr):
            return answer