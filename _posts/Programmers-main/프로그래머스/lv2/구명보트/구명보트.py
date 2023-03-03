def solution(people, limit):
    answer = 0
    i = 0
    people.sort()
    for j in range(len(people)-1, 0, -1):
        if i == j:
            answer += 1
            break
        elif j == i+1:
            if people[i] + people[j] > limit:
                answer += 2
            else:
                answer += 1
            break
        if people[i] + people[j] > limit:
            answer += 1
        else:
            i += 1
            answer += 1
    return answer