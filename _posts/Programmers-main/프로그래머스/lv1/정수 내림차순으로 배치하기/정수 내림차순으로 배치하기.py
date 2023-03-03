def solution(n):
    answer = 0
    n_list = list(str(int(n)))
    n_list.sort(reverse = True)
    
    for i in range(len(n_list)):
        answer += int(n_list[-(i+1)]) * 10 ** i

    return answer