from itertools import combinations
def solution(number):
    answer = 0
    n = 1
    len_number = len(number)
    for arr in combinations(number, 3):
        if sum(list(arr)) == 0:
            answer += 1
    return answer