def solution(jobs):
    answer = 0
    jobs = sorted(jobs, key = lambda x: (x[0], x[1]))
    le = len(jobs)
    time = jobs[0][0]
    while len(jobs) > 0:
        temp = list()
        for x, y in jobs:
            if x <= time:
                temp.append(y)
        if len(temp) == 0:
            time = jobs[0][0]
            continue
        for x, y in jobs:
            if y == min(temp):
                answer += (time - x + y)
                time += y
                jobs.remove([x, y])
                break
    answer = answer // le
    return answer