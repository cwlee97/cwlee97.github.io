def solution(sizes):
    answer = 0
    weight, height = [], []
    for x, y in sizes:
        weight.append(max(x, y))
        height.append(min(x, y))
    
    answer = max(weight) * max(height)
    
    return answer