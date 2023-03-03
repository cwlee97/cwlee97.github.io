def solution(brown, yellow):
    answer = []
    total = brown + yellow
    temp = []
    for i in range(1, total+1):
        if total % i == 0:
            temp.append(i)
    for i in range(len(temp)//2+1):
        if (temp[i]-2) * (temp[-(i+1)]-2) == yellow:
            answer.append(temp[-(i+1)])
            answer.append(temp[i])
            break
    return answer