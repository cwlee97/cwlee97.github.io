def solution(n, m, section):
    answer = 0
    n_bool = [True for _ in range(n)]
    for x in section:
        n_bool[x - 1] = False
    for idx in range(n):
        if n_bool[idx] == False:
            n_bool[idx:idx+m] = [True for _ in range(m)]
            answer += 1
        
    return answer