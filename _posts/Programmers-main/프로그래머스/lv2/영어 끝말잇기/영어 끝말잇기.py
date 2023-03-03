def solution(n, words):
    answer = []
    used = [words[0]]
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1]:
            x, y = divmod(i+1, n)
            if y == 0:
                y += n
                x -= 1
            answer = [y, x+1]
            break
            
        elif words[i] not in used:
            used.append(words[i])
            if i == len(words) - 1:
                answer = [0, 0]
        else:
            x, y = divmod(i+1, n)
            if y == 0:
                y += n
                x -= 1
            answer = [y, x+1]
            break
    return answer