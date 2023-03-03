def solution(price, money, count):
    answer = -1
    total = 0
    for i in range(1, count + 1):
        total += price * i
    if total > money:
        answer = total - money
    else:
        answer = 0
    return answer