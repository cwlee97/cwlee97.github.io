from itertools import combinations

def solution(numbers):
    answer = []
    data = list(combinations(numbers, 2))
    for i in range(len(data)):
        if sum(data[i]) not in answer:
            answer.append(sum(data[i]))
    answer.sort()
    return answer