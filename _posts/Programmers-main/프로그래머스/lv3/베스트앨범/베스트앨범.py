def solution(genres, plays):
    count_list, data, answer = [], [], []
    gen_set = list(set(genres))
    
    for i in range(len(genres)):
        data += [[plays[i], i, genres[i]]]
        
    data = sorted(data, key = lambda x: (-x[0], x[1]))
    
    for uni in gen_set:
        count = 0
        for x, y, z in data:
            if z == uni:
                count += x
        count_list += [[count, uni]]
        
    count_list.sort(reverse = True)
    
    for m, n in count_list:
        temp = []
        for x, y, z in data:
            if n == z:
                temp.append(y)
            if len(temp) == 2:
                break
        answer += temp
    return answer