def solution(d, budget):
    answer = 0
    total = 0
    d.sort()
    for i in range(len(d)):
        if total + d[i] > budget:
            answer = i
            break
        total += d[i]
        if i == len(d) - 1:
            answer = len(d)
    return answer