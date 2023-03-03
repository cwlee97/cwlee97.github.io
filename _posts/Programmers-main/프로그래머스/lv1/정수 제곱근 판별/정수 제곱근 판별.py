import math

def solution(n):
    answer = -1
    if math.sqrt(n) in range(7071067 + 1):
        answer = (math.sqrt(n)+1) ** 2
    return answer