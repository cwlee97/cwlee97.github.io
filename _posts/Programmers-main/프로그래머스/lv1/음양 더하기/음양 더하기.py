def solution(absolutes, signs):
    answer = 0
    i = 0
    while i < len(absolutes):
        if signs[i] == True:
            answer += absolutes[i]
        elif signs[i] == False:
            answer -= absolutes[i]
        i += 1
    return answer