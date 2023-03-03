def solution(n, m):
    answer = []
    count = 1
    
    for i in range(min(m, n), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    while len(answer) < 2:
        temp = max(n, m) * count
        if temp % n == 0 and temp % m == 0:
            answer.append(temp)
        count += 1
    return answer