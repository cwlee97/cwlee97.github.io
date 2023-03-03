def solution(n):
    answer = [[] for _ in range(n)]
    result = []
    x = 0
    temp = 0
    if n == 1:
        result = [1]
        return result
    while n > 0:
        for i in range(temp, temp + 3*(n-1)):
            if (i-temp+1) <= n-1:
                answer[2*x + (i-temp) % n].insert(x, i+1)
            elif (i-temp+1) <= 2 * (n-1):
                answer[-(x+1)].insert(len(answer[-(x+1)])-x, i+1)
            elif (i-temp+1) <= 3 * (n-1):
                answer[-(x+1)-((i-temp) % (n-1))].insert(len(answer[-(x+1)-((i-temp) % (n-1))])-x, i+1)
        temp += 3 * (n-1)
        x += 1
        n -= 3
    if n == -2:
        for i in range(len(answer)-1):
            if len(answer[i]) == len(answer[i+1]):
                answer[i+1].insert(len(answer[i+1])//2, temp+1)
    for i in answer:
        result += i
    return result